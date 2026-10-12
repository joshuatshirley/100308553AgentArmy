"""AgentArmy Interactive Recruiter CLI on Gemini.

Allows recruiters, station commanders, and guidance counselors to query the
entire 44-agent web grounded in Army doctrine and local station overlays.
"""
from __future__ import annotations

import argparse
import os
import sys

# Ensure repo root is on sys.path
REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if REPO_ROOT not in sys.path:
    sys.path.insert(0, REPO_ROOT)

from framework.gemini_factory import GeminiFactory


def format_agent_roster(factory: GeminiFactory) -> str:
    lines = [
        "=" * 80,
        "AGENT ARMY ROSTER (1 Orchestrator + 43 Specialists)",
        "=" * 80,
        f"Root Orchestrator: {factory.orchestrator.name} (`{factory.orchestrator.id}`)",
        "",
    ]
    groups = {}
    for aid, agent in factory.specialists.items():
        groups.setdefault(agent.group, []).append(agent)

    for group, agents in sorted(groups.items()):
        lines.append(f"[{group}]")
        for a in agents:
            lines.append(f"  * {a.id.ljust(32)} {a.name}")
        lines.append("")

    return "\n".join(lines)


def run_query(factory: GeminiFactory, query: str, location: str | None = None) -> None:
    print("\n" + "=" * 80)
    print(f"RECRUITER QUERY: {query}")
    if location:
        print(f"LOCATION OVERLAY: {location}")
    print("=" * 80)

    result = factory.ask(query, location_context=location)
    if "error" in result:
        print(f"Error: {result['error']}")
        return

    routed = result["routed_agent"]
    print(f"\n[ROUTING] Handed to: {routed['name']} (`{routed['id']}`)")
    print(f"[GROUP]   {routed['group']}")
    print(f"[TRIGGER] Matched on: '{routed['trigger_match']}'")

    if result.get("candidate_routes") and len(result["candidate_routes"]) > 1:
        candidates = ", ".join([f"{c['id']} ({c['score']}pts)" for c in result["candidate_routes"][1:3]])
        print(f"[SECONDARY CANDIDATES] {candidates}")

    print("\n" + "-" * 80)
    print("RESPONSE (GROUNDED IN DOCTRINE):")
    print("-" * 80)
    print(result["answer"].strip())
    print("\n" + "=" * 80 + "\n")


def interactive_mode(factory: GeminiFactory) -> None:
    print("=" * 80)
    print("Welcome to AgentArmy: Grounded Army Recruiting Assistant")
    print("Type your recruiting question below (or 'exit' / 'quit' to end).")
    print("Tip: Type '/loc <location>' to set a persistent location overlay (e.g. '/loc Charlotte MEPS')")
    print("=" * 80)

    location = None
    while True:
        try:
            loc_prompt = f" [{location}]" if location else ""
            user_input = input(f"Recruiter{loc_prompt}> ").strip()
            if not user_input:
                continue

            if user_input.lower() in ("exit", "quit", "q"):
                print("Exiting AgentArmy.")
                break

            if user_input.startswith("/loc "):
                location = user_input[5:].strip()
                print(f"Active location set to: '{location}'")
                continue

            if user_input == "/loc":
                location = None
                print("Location overlay cleared.")
                continue

            if user_input == "/roster":
                print(format_agent_roster(factory))
                continue

            run_query(factory, user_input, location=location)

        except (KeyboardInterrupt, EOFError):
            print("\nExiting.")
            break


def main() -> None:
    parser = argparse.ArgumentParser(description="AgentArmy: Army Recruiting Multi-Agent Web on Gemini")
    parser.add_argument("-q", "--query", type=str, help="Single recruiting question to ask")
    parser.add_argument("-l", "--location", type=str, help="Location context (e.g. 'Charlotte MEPS', 'North Carolina')")
    parser.add_argument("--roster", action="store_true", help="Print all 44 agents in the framework")
    parser.add_argument("-i", "--interactive", action="store_true", help="Start interactive CLI loop")

    args = parser.parse_args()

    factory = GeminiFactory()

    if args.roster:
        print(format_agent_roster(factory))
        return

    if args.query:
        run_query(factory, args.query, location=args.location)
    else:
        interactive_mode(factory)


if __name__ == "__main__":
    main()
