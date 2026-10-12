"""Ingestion CLI for new USAREC and USARD messages.

Allows recruiters, policy managers, and developers to ingest new policy messages,
update catalog/usarec_message_catalog.json, handle rescissions, and automatically
link the message to affected agent seeds in yaml/*.yaml.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
from typing import Any, Dict, List, Optional

import yaml

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def load_message_catalog(repo_root: str) -> Dict[str, Any]:
    cat_path = os.path.join(repo_root, "catalog", "usarec_message_catalog.json")
    if os.path.exists(cat_path):
        with open(cat_path, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}


def save_message_catalog(repo_root: str, catalog: Dict[str, Any]) -> None:
    cat_path = os.path.join(repo_root, "catalog", "usarec_message_catalog.json")
    with open(cat_path, "w", encoding="utf-8") as f:
        json.dump(catalog, f, indent=2)


def link_message_to_agents(
    repo_root: str,
    message_number: str,
    subject: str,
    target_agents: Optional[List[str]] = None,
    amends_doc: Optional[str] = None,
    amends_para: Optional[str] = None,
) -> List[str]:
    """Scan and attach message reference into matching agent YAML seeds."""
    yaml_dir = os.path.join(repo_root, "yaml")
    linked = []
    if not os.path.exists(yaml_dir):
        return linked

    for fname in sorted(os.listdir(yaml_dir)):
        if not fname.endswith(".yaml") or fname == "00_orchestrator.yaml":
            continue

        fpath = os.path.join(yaml_dir, fname)
        try:
            with open(fpath, "r", encoding="utf-8") as f:
                data = yaml.safe_load(f)

            if not isinstance(data, dict):
                continue

            agent_id = data.get("id", "")
            should_link = False

            # 1. Explicit target agents
            if target_agents and (agent_id in target_agents or "all" in target_agents):
                should_link = True

            # 2. Check if agent cites the amended document or paragraph
            if amends_doc and not should_link:
                for s in data.get("sources", []):
                    if s.get("doc") == amends_doc:
                        if amends_para:
                            paras = s.get("paragraphs", {})
                            if amends_para in paras or amends_para.replace("–", "-") in paras:
                                should_link = True
                                break
                        else:
                            should_link = True
                            break

            # 3. Keyword heuristic on subject vs agent triggers
            if not should_link and not target_agents:
                subj_lower = subject.lower()
                triggers = data.get("routing_triggers", [])
                for trig in triggers:
                    if len(trig) > 3 and trig.lower() in subj_lower:
                        should_link = True
                        break

            if should_link:
                msgs = data.setdefault("usarec_messages", [])
                # Check if already present
                existing_nums = [
                    m.get("number") if isinstance(m, dict) else str(m) for m in msgs
                ]
                if message_number not in existing_nums:
                    msgs.append({
                        "number": message_number,
                        "subject": subject,
                        "status": "active",
                    })
                    with open(fpath, "w", encoding="utf-8") as f:
                        yaml.dump(data, f, sort_keys=False, allow_unicode=True)
                    linked.append(agent_id)

        except Exception as e:
            print(f"Error checking {fname}: {e}")

    return linked


def ingest_message(
    number: str,
    subject: str,
    body_text: Optional[str] = None,
    rescinds: Optional[List[str]] = None,
    amends_doc: Optional[str] = None,
    amends_para: Optional[str] = None,
    target_agents: Optional[List[str]] = None,
    repo_root: Optional[str] = None,
) -> Dict[str, Any]:
    root = repo_root or REPO_ROOT
    clean_num = number.replace("USAREC_MESSAGE_", "").replace("USAREC Message ", "").strip()

    catalog = load_message_catalog(root)

    # Prepare catalog entry
    entry = {
        "subject": subject,
        "rescinds": [{"number": r, "evidence": "ingested rescission"} for r in (rescinds or [])],
        "expiry_text": [],
        "cites_ar_601_210_paragraph": bool(amends_doc == "AR_601-210" and amends_para),
        "amends_doc": amends_doc,
        "amends_paragraph": amends_para,
        "rescinded_by": None,
        "newer_same_subject": None,
        "status": "no rescission found in library",
        "pdf": f"USAREC Messages/USAREC_MESSAGE_{clean_num}.pdf",
    }

    # Update any rescinded messages in the catalog
    if rescinds:
        for r_num in rescinds:
            r_clean = r_num.strip()
            if r_clean in catalog:
                catalog[r_clean]["status"] = "rescinded"
                catalog[r_clean]["rescinded_by"] = clean_num

    catalog[clean_num] = entry
    save_message_catalog(root, catalog)

    # Save message markdown if text was supplied
    if body_text:
        msg_dir = os.path.join(root, "doctrine", "Messages")
        os.makedirs(msg_dir, exist_ok=True)
        msg_file = os.path.join(msg_dir, f"USAREC_MESSAGE_{clean_num}.md")
        with open(msg_file, "w", encoding="utf-8") as f:
            f.write(f"# USAREC MESSAGE {clean_num}\n\n**Subject**: {subject}\n\n{body_text}\n")

    # Link to affected agents
    linked_agents = link_message_to_agents(
        root,
        clean_num,
        subject,
        target_agents=target_agents,
        amends_doc=amends_doc,
        amends_para=amends_para,
    )

    return {
        "number": clean_num,
        "subject": subject,
        "status": "cataloged",
        "rescinded_messages": rescinds or [],
        "linked_agents": linked_agents,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Ingest new USAREC / USARD policy messages into AgentArmy")
    parser.add_argument("--number", "-n", required=True, help="Message number, e.g. 26-025")
    parser.add_argument("--subject", "-s", required=True, help="Message subject header")
    parser.add_argument("--text-file", "-f", help="Path to text or markdown file containing message content")
    parser.add_argument("--rescinds", "-r", nargs="*", help="Previous message numbers rescinded by this message")
    parser.add_argument("--amends-doc", help="Document amended, e.g. AR_601-210")
    parser.add_argument("--amends-para", help="Paragraph amended, e.g. 2-3")
    parser.add_argument("--agents", "-a", nargs="*", help="Agent IDs to explicitly attach to (or 'all')")

    args = parser.parse_args()

    body = ""
    if args.text_file and os.path.exists(args.text_file):
        with open(args.text_file, "r", encoding="utf-8", errors="replace") as f:
            body = f.read()

    res = ingest_message(
        number=args.number,
        subject=args.subject,
        body_text=body,
        rescinds=args.rescinds,
        amends_doc=args.amends_doc,
        amends_para=args.amends_para,
        target_agents=args.agents,
    )

    print("=" * 70)
    print("USAREC MESSAGE INGESTION RESULT:")
    print(f"Message Number:   {res['number']}")
    print(f"Subject:          {res['subject']}")
    print(f"Rescinded:        {res['rescinded_messages']}")
    print(f"Linked to Agents: {res['linked_agents']}")
    print("=" * 70)


if __name__ == "__main__":
    main()
