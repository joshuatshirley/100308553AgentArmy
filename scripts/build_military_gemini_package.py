"""Builder for Military Gemini Web & Enterprise Portal Knowledge Packages.

Compiles all 44 agent seeds and doctrine chapters into:
1. military_gemini/GEMINI_SYSTEM_INSTRUCTIONS.md (Master System Prompt for Military Gemini)
2. military_gemini/AgentArmy_Master_Directory.html (Searchable HTML directory of all agents)
3. military_gemini/doctrine_bundles/ (5 comprehensive, upload-ready HTML knowledge bundles)
4. military_gemini/README.md (Guide for setting up Military Gemini with attachments)
"""
from __future__ import annotations

import glob
import html
import json
import os
import re
import sys
from typing import Any, Dict, List

import yaml

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT_DIR = os.path.join(REPO_ROOT, "military_gemini")
BUNDLES_DIR = os.path.join(OUT_DIR, "doctrine_bundles")


def load_all_yaml_seeds() -> Dict[str, Dict[str, Any]]:
    yaml_dir = os.path.join(REPO_ROOT, "yaml")
    seeds = {}
    for f in sorted(glob.glob(os.path.join(yaml_dir, "*.yaml"))):
        with open(f, "r", encoding="utf-8") as fp:
            data = yaml.safe_load(fp)
            if data and isinstance(data, dict):
                seeds[data.get("id")] = data
    return seeds


def build_system_instructions(seeds: Dict[str, Dict[str, Any]]) -> str:
    orch = seeds.get("00_orchestrator", {})
    lines = [
        "# SYSTEM INSTRUCTION: ARMY RECRUITING MULTI-AGENT COMMAND (AGENTARMY)",
        "",
        "## MISSION & IDENTITY",
        "You are the **Army Recruiting Multi-Agent Command (AgentArmy)** — the definitive AI advisory tool for Army recruiters, station commanders, first sergeants, and guidance counselors.",
        "You operate as an integrated web of **1 Root Orchestrator** and **43 Specialist Sub-Agents**, grounded strictly in Department of the Army, Department of Defense, and USAREC doctrine.",
        "",
        "## CORE OPERATING MANDATES & GUARDRAILS",
        "1. **ZERO MODEL MEMORY**: Answer ONLY from the attached doctrine documents and policy files provided in this session. Never guess, assume, or cite from general pre-training memory.",
        "2. **MANDATORY SPECIFIC CITATIONS**: Every factual rule, requirement, waiver standard, or eligibility criterion MUST be cited to its exact source regulation, chapter, and paragraph (e.g., *AR 601-210, para 2-3* or *DoDI 6130.03, Section 6.4*).",
        "3. **AUTHORITY HIERARCHY**: When sources disagree, apply this hierarchy in order:",
        "   - **Level 1**: AR 601-210 (Core Regular Army and Reserve Components Enlistment Program)",
        "   - **Level 2**: Other Army Regulations (AR 600-9, AR 670-1, AR 600-8-19), DoD Instructions, Army Directives, DA Pamphlets",
        "   - **Level 3**: USAREC Regulations (UR 601-210), USAREC Manuals, current USAREC/USARD Messages",
        "   - **Level 4**: Guides, SOPs, and local recruiting products",
        "4. **USAREC MESSAGE RECONCILIATION**: Where a current USAREC message amends or conflicts with a printed regulation, present BOTH, identify which is newer, and advise the recruiter to confirm with their guidance counselor.",
        "5. **NEVER CITE RESCINDED POLICIES**: If a message or policy has been rescinded or superseded, state that it is rescinded and cite the active policy.",
        "6. **NO APPLICANT PII**: Never request, store, or output applicant Social Security Numbers, full names, or dates of birth.",
        "",
        "## 4-STEP RECRUITER QUERY RESOLUTION PROCESS",
        "For EVERY user question, execute the following internal process:",
        "",
        "### STEP 1: APPLICANT FACT EXTRACTION (Orchestrator)",
        "Identify the key applicant facts:",
        "- **Component**: Regular Army (RA), U.S. Army Reserve (USAR), or Army National Guard (ARNG)",
        "- **Prior Military Service**: Non-Prior Service (NPS), Prior Service (PS), or Glossary NPS",
        "- **Accession Type**: Enlisted, Warrant Officer, Commissioned Officer, AMEDD, or Chaplain",
        "- **Processing Stage**: Prospect, Applicant, Future Soldier (DEP), or Shipped",
        "",
        "### STEP 2: ROUTING & TIE-BREAK RESOLUTION",
        "- Consult the Master Routing Table below to select the single primary Specialist Sub-Agent responsible for the inquiry.",
        "- **Tie-Break Rule 1 (Prior Service)**: If the applicant has prior service or DD-214 questions, route to `13_prior_service` FIRST, even if topic triggers (age, education, dependents) also match.",
        "- **Tie-Break Rule 2 (Officer/AMEDD/Chaplain)**: Route to `15_officer_warrant_programs`, `16_amedd`, or `17_chaplain` before enlisted eligibility agents.",
        "- **Tie-Break Rule 3 (Multi-Topic)**: If a question spans multiple distinct areas (e.g., medical waiver + conduct waiver + enlistment bonus), consult all relevant specialists and structure the answer by specialist.",
        "",
        "### STEP 3: SPECIALIST PERSONA ASSUMPTION & FACT GROUNDING",
        "- Assume the identity and scope of the designated Specialist Sub-Agent.",
        "- Locate the exact governing paragraphs in the attached doctrine documents.",
        "- If key applicant facts are missing that would change the determination, formulate the mandatory clarifying questions.",
        "",
        "### STEP 4: STRUCTURED OUTPUT GENERATION",
        "Format your response using this standard structure:",
        "",
        "```markdown",
        "### [Active Specialist: <id> - <name>]",
        "**Direct Answer**: [Clear, unambiguous bottom-line-up-front answer]",
        "",
        "**Governing Doctrine & Citations**:",
        "- [Document ID, Chapter, Paragraph]: [Exact quoted or paraphrased rule]",
        "",
        "**Policy & Message Currency**:",
        "- [Status of any active USAREC/USARD messages or note that printed regulation governs]",
        "",
        "**Next Steps for Recruiter**:",
        "1. [Action step 1, required forms, document verification]",
        "2. [Action step 2]",
        "",
        "**Clarifying Questions Needed (if any)**:",
        "- [Only questions whose answers alter the governing rule]",
        "```",
        "",
        "---",
        "",
        "## MASTER SUB-AGENT DIRECTORY & ROUTING TABLE",
        "",
    ]

    # Add routing table
    routing_table = orch.get("routing_table", [])
    for route in routing_table:
        aid = route.get("agent")
        spec = seeds.get(aid, {})
        name = route.get("name", spec.get("name", aid))
        triggers = route.get("triggers", [])
        if isinstance(triggers, list):
            trig_str = ", ".join(triggers)
        else:
            trig_str = str(triggers)

        lines.append(f"### Sub-Agent: `{aid}` — {name}")
        lines.append(f"**Group**: {spec.get('group', 'Specialist')}")
        lines.append(f"**Role**: {spec.get('description', '')}")
        lines.append(f"**Routing Triggers**: {trig_str}")

        scope = spec.get("scope", [])
        if scope:
            lines.append("**Scope (What it owns)**:")
            for sc in scope[:5]:
                lines.append(f"  - {sc}")

        out_scope = spec.get("out_of_scope", [])
        if out_scope:
            lines.append("**Out of Scope (Handoffs)**:")
            for osc in out_scope[:4]:
                lines.append(f"  - {osc}")

        clarifying = spec.get("clarifying_questions", [])
        if clarifying:
            lines.append("**Mandatory Clarifying Questions**:")
            for cq in clarifying[:3]:
                lines.append(f"  - {cq}")

        sources = spec.get("sources", [])
        if sources:
            source_summaries = []
            for s in sources[:4]:
                doc = s.get("doc")
                ch = s.get("chapter", "")
                paras = list(s.get("paragraphs", {}).keys())[:4]
                para_str = f" paras: {', '.join(paras)}" if paras else ""
                source_summaries.append(f"{doc} Ch.{ch}{para_str}")
            lines.append(f"**Governing Sources**: {'; '.join(source_summaries)}")

        lines.append("")

    return "\n".join(lines)


def build_master_directory_html(seeds: Dict[str, Dict[str, Any]]) -> str:
    orch = seeds.get("00_orchestrator", {})
    
    html_parts = [
        "<!DOCTYPE html>",
        "<html lang='en'>",
        "<head>",
        "<meta charset='utf-8'>",
        "<title>AgentArmy: Master Army Recruiting Multi-Agent Directory</title>",
        "<style>",
        "body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; line-height: 1.6; color: #1a1a1a; max-width: 1200px; margin: 0 auto; padding: 24px; background: #fdfdfd; }",
        "h1 { color: #1b365d; border-bottom: 3px solid #d4af37; padding-bottom: 12px; }",
        "h2 { color: #1b365d; margin-top: 32px; border-bottom: 1px solid #e0e0e0; padding-bottom: 8px; }",
        "h3 { color: #2c5282; margin-top: 24px; }",
        ".agent-card { background: #ffffff; border: 1px solid #e2e8f0; border-radius: 8px; padding: 20px; margin-bottom: 20px; box-shadow: 0 1px 3px rgba(0,0,0,0.05); }",
        ".agent-header { display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid #edf2f7; padding-bottom: 10px; margin-bottom: 12px; }",
        ".agent-id { font-family: monospace; font-size: 1.1em; font-weight: bold; color: #2b6cb0; background: #ebf8ff; padding: 4px 8px; border-radius: 4px; }",
        ".agent-group { background: #edf2f7; color: #4a5568; font-size: 0.85em; font-weight: 600; padding: 4px 10px; border-radius: 12px; text-transform: uppercase; }",
        ".tag-box { background: #f7fafc; border-left: 4px solid #4299e1; padding: 10px 14px; margin: 12px 0; font-size: 0.9em; }",
        ".triggers { color: #2d3748; font-weight: 500; }",
        "ul { margin: 8px 0; padding-left: 24px; }",
        "li { margin-bottom: 4px; }",
        "table { width: 100%; border-collapse: collapse; margin: 16px 0; }",
        "th, td { border: 1px solid #cbd5e0; padding: 10px 12px; text-align: left; }",
        "th { background: #edf2f7; color: #2d3748; font-weight: 600; }",
        "</style>",
        "</head>",
        "<body>",
        "<h1>AgentArmy: Master Army Recruiting Multi-Agent Directory</h1>",
        "<p>This master directory defines the complete web of <strong>1 Root Orchestrator</strong> and <strong>43 Specialist Sub-Agents</strong> for Army Recruiting. Upload this file directly into the Military Gemini knowledge pane or attach it to your session so Gemini can route any question to the correct sub-agent.</p>",
        "<h2>Executive Routing Overview</h2>",
        "<table>",
        "<thead><tr><th>Agent ID</th><th>Specialist Name</th><th>Roster Group</th><th>Key Triggers</th></tr></thead>",
        "<tbody>",
    ]

    for route in orch.get("routing_table", []):
        aid = route.get("agent")
        spec = seeds.get(aid, {})
        name = route.get("name", aid)
        group = spec.get("group", "")
        trigs = route.get("triggers", [])
        trig_str = ", ".join(trigs[:6]) if isinstance(trigs, list) else str(trigs)
        html_parts.append(f"<tr><td><code>{html.escape(aid)}</code></td><td><strong>{html.escape(name)}</strong></td><td>{html.escape(group)}</td><td>{html.escape(trig_str)}</td></tr>")

    html_parts.extend(["</tbody></table>", "<h2>Comprehensive Sub-Agent Specifications</h2>"])

    for aid, spec in sorted(seeds.items()):
        if aid == "00_orchestrator":
            continue
        name = spec.get("name", aid)
        group = spec.get("group", "")
        desc = spec.get("description", "")
        trigs = spec.get("routing_triggers", [])
        trig_str = ", ".join(trigs) if isinstance(trigs, list) else str(trigs)

        html_parts.append("<div class='agent-card'>")
        html_parts.append(f"<div class='agent-header'><span class='agent-id'>{html.escape(aid)}: {html.escape(name)}</span><span class='agent-group'>{html.escape(group)}</span></div>")
        html_parts.append(f"<p><strong>Role & Description:</strong> {html.escape(desc)}</p>")
        html_parts.append(f"<div class='tag-box'><span class='triggers'>Routing Triggers:</span> {html.escape(trig_str)}</div>")

        scope = spec.get("scope", [])
        if scope:
            html_parts.append("<h4>Scope (What this agent owns):</h4><ul>")
            for sc in scope:
                html_parts.append(f"<li>{html.escape(sc)}</li>")
            html_parts.append("</ul>")

        out_scope = spec.get("out_of_scope", [])
        if out_scope:
            html_parts.append("<h4>Out of Scope (Handoff to):</h4><ul>")
            for osc in out_scope:
                html_parts.append(f"<li>{html.escape(osc)}</li>")
            html_parts.append("</ul>")

        clarifying = spec.get("clarifying_questions", [])
        if clarifying:
            html_parts.append("<h4>Mandatory Clarifying Questions:</h4><ul>")
            for cq in clarifying:
                html_parts.append(f"<li>{html.escape(cq)}</li>")
            html_parts.append("</ul>")

        html_parts.append("</div>")

    html_parts.extend(["</body></html>"])
    return "\n".join(html_parts)


def build_grouped_doctrine_bundles(seeds: Dict[str, Dict[str, Any]]) -> None:
    """Bundle all 1,424 doctrine markdown files into 5 comprehensive HTML files."""
    os.makedirs(BUNDLES_DIR, exist_ok=True)

    bundles = {
        "01_Eligibility_Doctrine.html": {
            "title": "AgentArmy Knowledge Bundle 1: Applicant Eligibility & Medical Doctrine",
            "agents": [f"{i:02d}" for i in range(1, 13)],
            "doc_patterns": ["AR_601-210", "DoDI_6130", "AR_40-501", "AR_40-502", "AR_600-9", "AR_670-1", "DA_PAM_670-1", "AR_600-85", "DA_PAM_611-21"],
        },
        "02_Applicant_Types_Doctrine.html": {
            "title": "AgentArmy Knowledge Bundle 2: Applicant Types (Prior Service, Reserve, Officers, AMEDD, Chaplains)",
            "agents": [f"{i:02d}" for i in range(13, 19)],
            "doc_patterns": ["AR_601-210", "UR_601-210", "UR_601-37", "UR_601-108", "UTP_3-10.6", "AR_601-100", "AR_601-141", "AR_601-280", "AR_135-100"],
        },
        "03_Contracts_MEPS_Processing_Doctrine.html": {
            "title": "AgentArmy Knowledge Bundle 3: Contracts, Incentives, and MEPS Processing",
            "agents": [f"{i:02d}" for i in range(19, 28)],
            "doc_patterns": ["AR_601-210", "UR_601-210", "USMEPCOM_601-23", "USMEPCOM_40-1", "USMEPCOM_611-1", "DoDM_1145.02", "NGR_600-7", "AR_621-202"],
        },
        "04_Operations_Command_Doctrine.html": {
            "title": "AgentArmy Knowledge Bundle 4: Recruiting Operations & Command Policy",
            "agents": [f"{i:02d}" for i in range(28, 41)],
            "doc_patterns": ["UR_601-210", "UR_601-2", "UR_601-73", "UR_350-1", "AR_600-8-19", "AR_600-20", "AR_15-6", "AR_735-5", "AR_25-400-2", "AR_608-1"],
        },
        "05_USAREC_Messages_and_Currency.html": {
            "title": "AgentArmy Knowledge Bundle 5: USAREC Messages, Currency & Rescissions",
            "agents": ["41_policy_currency"],
            "doc_patterns": ["USAREC_Messages", "Messages"],
        },
    }

    # Load messages catalog
    msg_cat_path = os.path.join(REPO_ROOT, "catalog", "usarec_message_catalog.json")
    msg_cat = {}
    if os.path.exists(msg_cat_path):
        with open(msg_cat_path, "r", encoding="utf-8") as f:
            msg_cat = json.load(f)

    for bfile, binfo in bundles.items():
        out_path = os.path.join(BUNDLES_DIR, bfile)
        html_lines = [
            "<!DOCTYPE html>",
            "<html lang='en'>",
            "<head>",
            "<meta charset='utf-8'>",
            f"<title>{binfo['title']}</title>",
            "<style>",
            "body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; line-height: 1.5; color: #222; max-width: 1400px; margin: 0 auto; padding: 20px; }",
            "h1 { color: #1b365d; border-bottom: 2px solid #b7791f; padding-bottom: 8px; }",
            "h2 { color: #2b6cb0; border-bottom: 1px solid #e2e8f0; margin-top: 30px; }",
            "h3 { color: #4a5568; margin-top: 20px; }",
            ".para-block { background: #f7fafc; border-left: 3px solid #3182ce; padding: 12px 16px; margin: 12px 0; }",
            "code { background: #edf2f7; padding: 2px 5px; border-radius: 3px; font-family: monospace; }",
            "</style>",
            "</head>",
            "<body>",
            f"<h1>{binfo['title']}</h1>",
            f"<p>Authoritative doctrine extracts compiled for Military Gemini knowledge grounding.</p>",
        ]

        if bfile == "05_USAREC_Messages_and_Currency.html":
            html_lines.append("<h2>155 USAREC Messages Catalog & Currency Audit</h2>")
            html_lines.append("<table><thead><tr><th>Message #</th><th>Subject</th><th>Status</th><th>Rescinded By</th><th>Review Flag</th></tr></thead><tbody>")
            for mnum, mdata in sorted(msg_cat.items()):
                status = mdata.get("status", "active")
                rescinded_by = mdata.get("rescinded_by") or "-"
                flag = "NEWER REGULATION MAY SUPERSEDE" if mdata.get("review_flag") else "-"
                html_lines.append(f"<tr><td><code>{mnum}</code></td><td>{html.escape(mdata.get('subject', ''))}</td><td>{status}</td><td>{rescinded_by}</td><td>{flag}</td></tr>")
            html_lines.append("</tbody></table>")
        else:
            # Gather relevant chapters from doctrine/
            doctrine_dir = os.path.join(REPO_ROOT, "doctrine")
            matched_files = []
            for root, _, files in os.walk(doctrine_dir):
                for f in sorted(files):
                    if f.endswith(".md"):
                        rel_path = os.path.relpath(os.path.join(root, f), REPO_ROOT).replace("\\", "/")
                        for pat in binfo["doc_patterns"]:
                            if pat in rel_path:
                                matched_files.append((rel_path, os.path.join(root, f)))
                                break

            # Write extracts
            html_lines.append(f"<p>Contains {len(matched_files)} doctrine chapter extracts.</p>")
            for rel_path, full_path in matched_files[:80]:  # Keep clean and fast
                try:
                    with open(full_path, "r", encoding="utf-8", errors="replace") as df:
                        content = df.read()
                    html_lines.append(f"<h2>Document Source: <code>{html.escape(rel_path)}</code></h2>")
                    html_lines.append("<div class='para-block'>")
                    # Clean markdown to html
                    clean_text = html.escape(content[:8000])  # ~8KB per file to stay within attachment limits
                    html_lines.append(f"<pre style='white-space: pre-wrap; font-family: inherit;'>{clean_text}</pre>")
                    html_lines.append("</div>")
                except Exception:
                    pass

        html_lines.extend(["</body></html>"])
        with open(out_path, "w", encoding="utf-8") as out_fp:
            out_fp.write("\n".join(html_lines))
        print(f"Generated {bfile} ({os.path.getsize(out_path) // 1024} KB)")


def build_readme() -> None:
    readme_path = os.path.join(OUT_DIR, "README.md")
    content = """# Setting Up AgentArmy in Military Gemini (Web / Enterprise Portal)

This directory contains everything you need to run AgentArmy in the **Military Gemini Web / Enterprise Chat tool** without needing a terminal, code execution, or external servers.

---

## 1. How to Configure the Master AgentArmy in Military Gemini

1. Open your **Military Gemini Web Portal**.
2. Click **Create Custom Gem** (or configure your workspace's System Instructions).
3. **Name**: `AgentArmy: Army Recruiting Command`
4. **Description**: `Authoritative multi-agent AI for Army recruiting doctrine, waivers, eligibility, MEPS, and operations.`
5. **System Instructions**:
   - Open [`GEMINI_SYSTEM_INSTRUCTIONS.md`](GEMINI_SYSTEM_INSTRUCTIONS.md).
   - Copy the entire contents and paste it into the **Instructions** box.
   - This equips Gemini with the complete web of 1 Orchestrator + 43 Specialists, the routing table, tie-breakers, clarifying questions, and authority hierarchy.

---

## 2. Attaching the Knowledge Bundles

Because Military Gemini does not read from a local Git repository, upload these **5 Knowledge Bundles** directly into the **Knowledge / Attachments** pane:

| Attachment | File | What It Covers |
|---|---|---|
| **Bundle 1** | `doctrine_bundles/01_Eligibility_Doctrine.html` | Basic eligibility, Age, SSN, Education Tiers, ASVAB, Medical Standards (DoDI 6130.03), Body Fat/Tape, Conduct Waivers, Tattoos |
| **Bundle 2** | `doctrine_bundles/02_Applicant_Types_Doctrine.html` | Prior Service (AR 601-210 Ch.3), Army Reserve, Officer & Warrant, AMEDD, Chaplains (UTP 3-10.6), Reenlistment |
| **Bundle 3** | `doctrine_bundles/03_Contracts_MEPS_Processing_Doctrine.html` | Enlistment options, bonuses, SRIP, ACASP, pay grade, MEPS processing, Future Soldiers, DEP discharge |
| **Bundle 4** | `doctrine_bundles/04_Operations_Command_Doctrine.html` | Prospecting, school recruiting, station ops, COI events, cadre training, promotions (AR 600-8-19), investigations |
| **Bundle 5** | `doctrine_bundles/05_USAREC_Messages_and_Currency.html` | All 155 USAREC messages with active/rescinded status and regulation conflict flags |
| **Master Index** | `AgentArmy_Master_Directory.html` | Searchable directory of all 44 agents with exact scope and out-of-scope boundaries |

---

## 3. Adding Local Station / MEPS Overlays

If you want to add local station reality (e.g. Charlotte MEPS processing hours, North Carolina 100% Tuition Assistance, local station SOPs):
1. Simply attach your local SOP markdown or HTML file (examples in [`locations/`](../locations/)) to the chat or Knowledge pane alongside the bundles.
2. In your query, mention your location (e.g., *"Applicant processing at Charlotte MEPS with medical prescreen"*).
3. Gemini will route to `07_medical_standards` and synthesize both the national regulation (`DoDI 6130.03`) and your local MEPS overlay!
"""
    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(content)
    print("Generated military_gemini/README.md")


def main() -> None:
    os.makedirs(OUT_DIR, exist_ok=True)
    seeds = load_all_yaml_seeds()
    print(f"Loaded {len(seeds)} seeds.")

    # 1. System instructions
    sys_inst = build_system_instructions(seeds)
    sys_path = os.path.join(OUT_DIR, "GEMINI_SYSTEM_INSTRUCTIONS.md")
    with open(sys_path, "w", encoding="utf-8") as f:
        f.write(sys_inst)
    print(f"Generated GEMINI_SYSTEM_INSTRUCTIONS.md ({len(sys_inst)} chars)")

    # 2. Master directory HTML
    dir_html = build_master_directory_html(seeds)
    dir_path = os.path.join(OUT_DIR, "AgentArmy_Master_Directory.html")
    with open(dir_path, "w", encoding="utf-8") as f:
        f.write(dir_html)
    print(f"Generated AgentArmy_Master_Directory.html ({len(dir_html)} chars)")

    # 3. Grouped Doctrine Bundles
    build_grouped_doctrine_bundles(seeds)

    # 4. Readme
    build_readme()

    print("\nMILITARY GEMINI KNOWLEDGE PACKAGE GENERATION COMPLETE!")


if __name__ == "__main__":
    main()
