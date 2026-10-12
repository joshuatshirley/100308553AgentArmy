"""Export AgentArmy definitions for Google Cloud Vertex AI Agent Builder.

Generates structured JSON specifications for:
- 1 Root Orchestrator (Supervisor)
- 43 Specialist Sub-Agents
- Tool definitions and Grounding Data Store mappings
Compatible with Google Cloud for Government / Military Cloud (IL4/IL5 / FedRAMP).
"""
from __future__ import annotations

import argparse
import json
import os
import sys

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if REPO_ROOT not in sys.path:
    sys.path.insert(0, REPO_ROOT)

from framework.gemini_factory import GeminiFactory


def export_vertex_agent_specs(output_file: str) -> None:
    factory = GeminiFactory()
    export_data = {
        "framework": "AgentArmy",
        "cloud_target": "Google Cloud Vertex AI (Government & Military Cloud)",
        "version": "1.0.0",
        "orchestrator": {
            "id": factory.orchestrator.id,
            "name": factory.orchestrator.name,
            "role": "Supervisor / Front Door Router",
            "routing_table": factory.orchestrator.routing_table,
            "tie_break_rules": factory.orchestrator.tie_break_rules,
            "applicant_facts": factory.orchestrator.applicant_facts,
        },
        "specialists": [],
    }

    for aid, agent in factory.specialists.items():
        export_data["specialists"].append({
            "id": agent.id,
            "name": agent.name,
            "group": agent.group,
            "description": agent.description,
            "scope": agent.scope,
            "out_of_scope": agent.out_of_scope,
            "guardrails": agent.guardrails,
            "clarifying_questions": agent.clarifying_questions,
            "routing_triggers": agent.routing_triggers,
            "system_instruction": agent.build_system_prompt(),
            "sources": agent.sources,
            "usarec_messages": agent.usarec_messages,
        })

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(export_data, f, indent=2)

    print(f"Exported {len(export_data['specialists'])} specialist specs + 1 orchestrator to: {output_file}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Export AgentArmy to Vertex AI Agent Builder bundle")
    parser.add_argument(
        "-o",
        "--output",
        default=os.path.join(REPO_ROOT, "catalog", "vertex_agent_builder_bundle.json"),
        help="Target output JSON path",
    )
    args = parser.parse_args()
    export_vertex_agent_specs(args.output)


if __name__ == "__main__":
    main()
