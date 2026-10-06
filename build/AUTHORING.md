# How to author agent seeds (read fully before writing)

Build dir: this folder. Doctrine root (READ ONLY, never write there):
`C:\Users\joshu\..Project\Station_Commander\Army_Doctrine`

You write ONE file: `seeds_<yourgroup>.py` in this folder containing `SEEDS = { "<agent_id>": {...}, ... }`.
The spec format is EXACTLY the specialist format in `exemplars.py` (see `EXEMPLARS["09_conduct_waivers"]`
and `EXEMPLARS["30_station_operations"]`). Copy `COMMON_GUARDRAILS` via
`from exemplars import COMMON_GUARDRAILS`. Roster entries (id, name, summary, starting sources, triggers,
maps_to) are in `roster.py`; your ids must match the roster exactly.

Required keys per seed: agent_type ("specialist"), description, scope, out_of_scope, sources, messages,
forms, routing_triggers, hand_off_to, clarifying_questions, flow, example_questions, guardrails.

## Research tools (python -B lookup.py ...)
- `doc AR_601-210 4` chapters, markdown files, paragraph numbers + headings (+ section)
- `find 670` document ids matching
- `msg tattoo` USAREC messages whose subject contains all words; `msgbody 24-017` to read one
- `forms 601-210` form folder names (forms list uses exact folder names)
- `grep AR_601-210 4 "waiting period"` lines in that chapter's text
Read the actual chapter markdown (path from `doc`) for anything you describe. Do not rely on memory.

## Hard rules (the user's standing rules; violations get the seed rejected)
1. Never state a threshold, age, score, dollar amount, time period, or approval authority as fact in
   description/scope/flow/questions. Say WHAT the section covers ("the waiting periods in 4-31"), and tell
   the agent to read it at run time. Empty is better than wrong.
2. Every paragraph you cite must exist in the catalog. Source entry forms:
   - `dict(doc="AR_601-210", chapter="4", paragraphs=["4-31","4-33"], note="...")` or `paragraphs="all"`
   - manuals with untitled paragraphs: `dict(doc="UM_3-31", chapter="3", sections=["Prospecting", ...])`
     using section headings copied from that manual's table of contents (`.transform/00_Front_Matter.md`)
   - whole document: `dict(doc="AR_670-1", chapter="all", note="...")` (use when chapters/paras are not extracted)
   Flow step `sources` refs: `"AR_601-210 4-31"`, `"UM_3-31 Ch.3"`, or bare `"DoDI_1304.26"`.
3. Messages: only include messages whose subject/body you checked are on-topic (`msgbody`). Include rescinded
   ones only if useful, the build marks their status. Use the 5-digit form "24-017".
4. hand_off_to keys must be roster ids. Hand off anything another roster agent owns (see roster summaries).
5. Example questions are questions only, realistic recruiter/station commander voice, 5 to 7 of them.
6. No PII, no station-specific tactics, no named local businesses.
7. Description: one plain paragraph, who asks, what it answers, what it reads, what it hands off.
8. Flow: 5 to 11 ordered steps, each with name + action, most with sources.
9. Where the doctrine is thin or not extracted (catalog `gaps`), say so in a source `note` instead of inventing.
10. UR 601-210 chapters 3,5,6,7,10,13,20-25 are PDF only: you may cite them as
    `dict(doc="UR_601-210", chapter="all", note="Ch.25 OCS/WOFT Processing Procedures exists only in the PDF")`.

## Validate (must pass before you finish)
`python -B build_seeds.py --only seeds_<yourgroup>.py`  -> prints OK or lists citation errors. Fix all errors.
Do not edit any other file in this folder. Do not write anywhere else.
