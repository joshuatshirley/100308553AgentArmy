"""Gemini Agent Factory for AgentArmy.

Compiles the 44 declarative YAML agent seeds into an executable multi-agent web:
- Root Orchestrator (00_orchestrator)
- 43 Specialist Sub-Agents
- Grounded with DoctrineRetriever and LocationManager
- Runs live against Google Gemini API (GEMINI_API_KEY) or dry-run/mock mode.
"""
from __future__ import annotations

import glob
import json
import os
import re
import urllib.request
import urllib.error
from typing import Any, Dict, List, Optional, Tuple

import yaml

from framework.doctrine_retriever import DoctrineRetriever
from framework.location_manager import LocationManager

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class GeminiAgent:
    """Represents a compiled specialist sub-agent."""

    def __init__(self, spec: Dict[str, Any], retriever: DoctrineRetriever, location_mgr: LocationManager):
        self.spec = spec
        self.retriever = retriever
        self.location_mgr = location_mgr
        self.id: str = spec.get("id", "")
        self.name: str = spec.get("name", "")
        self.agent_type: str = spec.get("agent_type", "specialist")
        self.group: str = spec.get("group", "")
        self.description: str = spec.get("description", "")
        self.scope: List[str] = spec.get("scope", [])
        self.out_of_scope: List[str] = spec.get("out_of_scope", [])
        self.guardrails: List[str] = spec.get("guardrails", [])
        self.clarifying_questions: List[str] = spec.get("clarifying_questions", [])
        self.routing_triggers: List[str] = spec.get("routing_triggers", [])
        self.sources: List[Dict[str, Any]] = spec.get("sources", [])
        self.usarec_messages: List[Any] = spec.get("usarec_messages", [])

    def build_system_prompt(self, location_context: Optional[str] = None) -> str:
        """Build the complete, grounded system prompt for this agent."""
        lines = [
            f"# AGENT: {self.name} (`{self.id}`)",
            f"Role: {self.description}",
            "",
            "## CORE PRINCIPLES & GUARDRAILS:",
            "- You answer ONLY from the cited Army doctrine and USAREC policies provided below.",
            "- Never guess, assume, or cite from general model memory.",
            "- State what the doctrine covers and cite exact document and paragraph numbers (e.g. AR 601-210, para 2-3).",
            "- If the doctrine is silent, explicitly state: 'The cited doctrine does not address this circumstance.'",
            "- NO APPLICANT PII: Never ask for or output SSNs, full names, or dates of birth.",
            "",
            "## SCOPE (WHAT YOU OWN):",
        ]
        for s in self.scope:
            lines.append(f"- {s}")

        lines.extend(["", "## OUT OF SCOPE (HAND OFF):"])
        for o in self.out_of_scope:
            lines.append(f"- {o}")

        if self.clarifying_questions:
            lines.extend(["", "## MANDATORY CLARIFYING QUESTIONS:"])
            lines.append("If the applicant facts provided are incomplete, ask only the necessary questions below:")
            for q in self.clarifying_questions:
                lines.append(f"- {q}")

        # Check USAREC messages
        msgs = self.retriever.get_usarec_messages_info(self.usarec_messages)
        if msgs:
            lines.extend(["", "## APPLICABLE USAREC / USARD MESSAGES:"])
            for m in msgs:
                status_str = f" [Status: {m.get('status')}]"
                flag_str = " (REVIEW: Newer regulation edition may supersede)" if m.get("review_flag") else ""
                lines.append(f"- Message {m.get('number')}: {m.get('subject')}{status_str}{flag_str}")

        # Attach Location Overlays if relevant
        overlays = self.location_mgr.get_overlays_for_agent(self.id, location_context)
        if overlays:
            lines.extend(["", "## LOCAL STATION / MEPS / STATE OVERLAYS:"])
            for ov in overlays:
                lines.append(f"### Local Policy: {ov.get('title')}")
                lines.append(ov.get("body", "").strip())
                lines.append("")

        return "\n".join(lines)

    def get_grounded_context(self) -> str:
        """Extract and format the exact doctrine texts cited by this specialist."""
        doctrine_items = self.retriever.get_agent_sources_text(self.spec)
        if not doctrine_items:
            return "No specific paragraph extracts loaded."

        lines = ["# AUTHORITATIVE DOCTRINE EXTRACTS:"]
        for item in doctrine_items:
            doc_id = item.get("doc_id")
            para = item.get("paragraph", "")
            title = item.get("paragraph_title") or item.get("chapter_title", "")
            header = f"[{doc_id} {para} - {title}]" if para else f"[{doc_id} - {title}]"
            lines.append(f"\n--- BEGIN {header} ---")
            lines.append(item.get("text", "").strip())
            lines.append(f"--- END {header} ---")

        return "\n".join(lines)


class GeminiOrchestrator:
    """The Root Supervisor Agent that routes and synthesizes queries across the 43 specialists."""

    def __init__(self, spec: Dict[str, Any], specialists: Dict[str, GeminiAgent]):
        self.spec = spec
        self.specialists = specialists
        self.id = spec.get("id", "00_orchestrator")
        self.name = spec.get("name", "Army Recruiting Orchestrator")
        self.routing_table = spec.get("routing_table", [])
        self.applicant_facts = spec.get("applicant_facts_that_decide_routing", [])
        self.tie_break_rules = spec.get("tie_break_rules", [])

    def route_query(self, query: str) -> List[Tuple[str, int, str]]:
        """Determine which specialist agent(s) should answer this question based on triggers."""
        q_lower = query.lower()
        matches = []

        # Check routing table
        for route in self.routing_table:
            agent_id = route.get("agent", "")
            raw_triggers = route.get("triggers", [])
            if isinstance(raw_triggers, str):
                triggers = [t.strip().lower() for t in raw_triggers.split(",") if t.strip()]
            elif isinstance(raw_triggers, list):
                triggers = [str(t).strip().lower() for t in raw_triggers if str(t).strip()]
            else:
                triggers = []

            score = 0
            matched_trigger = ""
            for trig in triggers:
                if trig in q_lower:
                    # Longer phrase matches get higher priority
                    trig_score = len(trig.split()) * 5 + len(trig)
                    if trig_score > score:
                        score = trig_score
                        matched_trigger = trig

            if score > 0 and agent_id in self.specialists:
                matches.append((agent_id, score, matched_trigger))

        # Check applicant facts: Non-Prior Service vs Prior Service
        is_explicit_nps = any(
            phrase in q_lower
            for phrase in ["without prior service", "no prior service", "non-prior service", "non prior service", "nps"]
        )
        is_ps = (not is_explicit_nps) and any(
            w in q_lower
            for w in ["prior service", "veteran", "re-entry", "reentry", "dd 214", "dd-214", "glossary nps"]
        )

        filtered_matches = []
        for aid, score, trig in matches:
            if is_explicit_nps and aid == "13_prior_service":
                continue  # Skip prior service agent if query explicitly says without prior service
            if is_ps and aid == "13_prior_service":
                score += 50
            filtered_matches.append((aid, score, trig))

        matches = filtered_matches
        matches.sort(key=lambda x: x[1], reverse=True)
        if not matches:
            # Fallback to 01_basic_eligibility for general questions
            matches.append(("01_basic_eligibility", 1, "default basic eligibility"))

        return matches


class GeminiFactory:
    """Compiler and runtime factory for the entire AgentArmy on Gemini.
    
    Supports:
    1. Google Cloud Vertex AI (Government & Military Cloud / FedRAMP / DoD IL4/IL5) via IAM / ADC
    2. Google AI Studio (Commercial developer API key via GEMINI_API_KEY)
    3. Dry-run mode for local validation without cloud credentials
    """

    def __init__(
        self,
        repo_root: Optional[str] = None,
        api_key: Optional[str] = None,
        project: Optional[str] = None,
        location: Optional[str] = None,
    ):
        self.repo_root = repo_root or REPO_ROOT
        self.api_key = api_key or os.environ.get("GEMINI_API_KEY", "")
        self.project = project or os.environ.get("GOOGLE_CLOUD_PROJECT") or os.environ.get("VERTEX_PROJECT", "")
        self.location = location or os.environ.get("GOOGLE_CLOUD_LOCATION") or os.environ.get("VERTEX_LOCATION", "us-central1")

        self.retriever = DoctrineRetriever(self.repo_root)
        self.location_mgr = LocationManager(self.repo_root)
        self.specialists: Dict[str, GeminiAgent] = {}
        self.orchestrator: Optional[GeminiOrchestrator] = None

        # Determine cloud provider mode
        self.mode = "dry_run"
        self.credentials = None

        # Check for Google Cloud / GovCloud ADC credentials
        try:
            import google.auth
            creds, detected_proj = google.auth.default(scopes=["https://www.googleapis.com/auth/cloud-platform"])
            if creds:
                self.credentials = creds
                if not self.project and detected_proj:
                    self.project = detected_proj
                if self.project:
                    self.mode = "vertex_ai"
        except Exception:
            pass

        if self.mode != "vertex_ai" and self.api_key:
            self.mode = "gemini_api"

        self._compile_agents()

    def _compile_agents(self) -> None:
        yaml_dir = os.path.join(self.repo_root, "yaml")
        if not os.path.exists(yaml_dir):
            return

        yaml_files = glob.glob(os.path.join(yaml_dir, "*.yaml"))
        orchestrator_spec = None

        for yf in sorted(yaml_files):
            try:
                with open(yf, "r", encoding="utf-8") as f:
                    spec = yaml.safe_load(f)
                if not spec or not isinstance(spec, dict):
                    continue

                agent_id = spec.get("id", "")
                if agent_id == "00_orchestrator":
                    orchestrator_spec = spec
                else:
                    self.specialists[agent_id] = GeminiAgent(spec, self.retriever, self.location_mgr)
            except Exception as e:
                print(f"Warning: Failed loading {yf}: {e}")

        if orchestrator_spec:
            self.orchestrator = GeminiOrchestrator(orchestrator_spec, self.specialists)

    def _get_vertex_token(self) -> str:
        """Fetch or refresh OAuth2 Bearer token for Google Cloud Vertex AI."""
        if not self.credentials:
            return ""
        from google.auth.transport.requests import Request
        if not self.credentials.valid:
            self.credentials.refresh(Request())
        return self.credentials.token

    def call_gemini_api(self, system_instruction: str, user_content: str, model: str = "gemini-2.0-flash") -> str:
        """Call Gemini API via REST (Vertex AI GovCloud or Google AI Studio)."""
        if self.mode == "dry_run":
            return (
                "[DRY RUN / NO CLOUD CREDENTIALS SET]\n\n"
                "System Instruction and Grounded Doctrine successfully generated.\n"
                "To run live inference in GovCloud / Vertex AI: set GOOGLE_CLOUD_PROJECT and authenticate via gcloud/service account.\n"
                "To run live inference via Google AI Studio: set GEMINI_API_KEY.\n\n"
                f"--- Prompt Preview ---\n{user_content[:500]}..."
            )

        payload = {
            "contents": [
                {
                    "role": "user",
                    "parts": [{"text": user_content}],
                }
            ],
            "system_instruction": {
                "parts": [{"text": system_instruction}]
            },
            "generationConfig": {
                "temperature": 0.1,
                "topP": 0.95,
                "maxOutputTokens": 2048,
            },
        }

        headers = {"Content-Type": "application/json"}

        if self.mode == "vertex_ai":
            token = self._get_vertex_token()
            headers["Authorization"] = f"Bearer {token}"
            url = (
                f"https://{self.location}-aiplatform.googleapis.com/v1/"
                f"projects/{self.project}/locations/{self.location}/publishers/google/models/{model}:generateContent"
            )
        else:
            url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={self.api_key}"

        req = urllib.request.Request(
            url,
            data=json.dumps(payload).encode("utf-8"),
            headers=headers,
            method="POST",
        )

        try:
            with urllib.request.urlopen(req, timeout=30) as resp:
                data = json.loads(resp.read().decode("utf-8"))
                candidates = data.get("candidates", [])
                if candidates:
                    parts = candidates[0].get("content", {}).get("parts", [])
                    if parts:
                        return parts[0].get("text", "")
                return "No text returned from Gemini."
        except urllib.error.HTTPError as e:
            err_body = e.read().decode("utf-8")
            return f"Gemini API Error ({e.code}): {err_body}"
        except Exception as e:
            return f"Connection error calling Gemini: {e}"

    def ask(self, query: str, location_context: Optional[str] = None) -> Dict[str, Any]:
        """Process a recruiter question through the Orchestrator and Specialist Web."""
        if not self.orchestrator:
            return {"error": "Orchestrator not compiled."}

        # 1. Routing
        routing_matches = self.orchestrator.route_query(query)
        primary_agent_id = routing_matches[0][0]
        specialist = self.specialists.get(primary_agent_id)

        if not specialist:
            return {"error": f"Specialist {primary_agent_id} not found."}

        # 2. Build Grounded Context
        system_prompt = specialist.build_system_prompt(location_context=location_context)
        doctrine_context = specialist.get_grounded_context()

        # Build prompt payload
        user_prompt = (
            f"RECRUITER QUESTION: {query}\n\n"
            f"LOCATION CONTEXT: {location_context or 'None specified'}\n\n"
            f"{doctrine_context}\n\n"
            "INSTRUCTIONS FOR ANSWER:\n"
            "1. Give a direct, plain-language answer to the recruiter's question.\n"
            "2. Cite the exact regulation, chapter, and paragraph number for every substantive rule.\n"
            "3. If any USAREC message applies or conflicts with the regulation, state both.\n"
            "4. List immediate next steps for the recruiter.\n"
            "5. If key applicant facts are missing, list the specific clarifying questions needed."
        )

        # 3. Call Gemini
        answer = self.call_gemini_api(system_instruction=system_prompt, user_content=user_prompt)

        return {
            "query": query,
            "location_context": location_context,
            "routed_agent": {
                "id": specialist.id,
                "name": specialist.name,
                "group": specialist.group,
                "trigger_match": routing_matches[0][2],
            },
            "candidate_routes": [
                {"id": aid, "score": score, "trigger": trig} for aid, score, trig in routing_matches[:3]
            ],
            "answer": answer,
        }
