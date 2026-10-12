# AgentArmy: Army Recruiting agent seeds

Seed definitions for an AI agent tool: one **orchestrator** that takes any Army recruiting question and
hands it to **43 specialist sub-agents**, each grounded in a specific set of Army, DoD and USAREC
doctrine. Every seed is a draft pending SME review.

## Layout

| Path | What it is |
|---|---|
| `agents/<id>.md` | One file per agent. YAML front matter (id, group, routing triggers, hand-offs, source documents, messages) plus a readable body: description, scope, out of scope, sources down to chapter and paragraph, USAREC messages with currency status, forms, clarifying questions, hand-offs, flow steps, example questions, guardrails |
| `ALL_AGENTS.md` | All 44 agents in one file between `<!-- BEGIN AGENT: id -->` / `<!-- END AGENT: id -->` markers |
| `scripts/split_agents.py` | `python scripts/split_agents.py ALL_AGENTS.md agents/` splits the combined file back into one file per agent |
| `yaml/<id>.yaml` | The same seeds as structured YAML |
| `framework/gemini_factory.py` | Compiles all 44 seeds into an active multi-agent web on Gemini (Orchestrator + 43 Specialists) |
| `framework/doctrine_retriever.py` | Runtime retriever that extracts exact cited paragraphs from `doctrine/*.md` |
| `framework/location_manager.py` | Manages location overlays for recruiting stations, MEPS SOPs, and state National Guard benefits |
| `framework/cli.py` | Interactive recruiter CLI (`python framework/cli.py`) with location-aware query routing |
| `locations/` | Modular location overlays (e.g. `locations/meps/charlotte_meps.md`, `locations/states/NC_guard.md`) |
| `scripts/ingest_message.py` | Ingests new USAREC/USARD messages, updates catalogs, and links to affected agents |
| `ROSTER.md` | The roster by group, with primary sources and how each agent maps to the earlier FlorenceTaskingCommand agents |
| `SCHEMA.yaml` | Field-by-field definition of a seed |
| `DOCTRINE_GAPS.md` | Where the source library is thin, out of date or not yet converted to text |
| `catalog/source_catalog.json` | 194 source documents: title, edition, authority level, chapter files, 14,061 paragraph headings |
| `doctrine/` | The actual chapter/paragraph markdown text for every cataloged document (1,424 files, ~36MB) — what `markdown` paths in the seeds point to, so a checkout of this repo alone is enough to run the agents |
| `catalog/usarec_message_catalog.json` | 155 USAREC/USARD messages with subject, rescission status and evidence, review flags |
| `build/` | Scripts that regenerate everything from the doctrine library |

## Roster

| Group | Agents |
|---|---|
| Front door | 00 orchestrator |
| Eligibility | 01 basic eligibility, 02 citizenship and language, 03 education credentialing, 04 dependents and family, 05 testing, 06 MOS classification, 07 medical standards, 08 body composition and fitness, 09 conduct waivers, 10 drug and alcohol, 11 appearance and accommodation, 12 background and security |
| Applicant types | 13 prior service, 14 Army Reserve, 15 officer and warrant programs, 16 AMEDD, 17 chaplain, 18 retention and reenlistment |
| Contract | 19 RA options and incentives, 20 SRIP, 21 special enlistment programs, 22 ACASP, 23 grade and enlistment periods |
| Processing | 24 processing and MEPS, 25 Future Soldier management, 26 DEP separations, 27 post-enlistment corrections |
| Operations | 28 prospecting, 29 school recruiting, 30 station operations, 31 market intelligence, 32 COI and support programs, 33 marketing and public affairs |
| Command support | 34 training, 35 personnel actions, 36 military justice and command policy, 37 logistics and property, 38 IT and records, 39 Soldier and family wellness, 40 systems how-to |
| Cross-cutting | 41 policy currency (USAREC messages), 42 leadership doctrine, 43 career guidance |

## Rules every seed follows

- Agents answer only from the cited source text loaded at run time, never from model memory.
- Seeds say what a section covers. They do not restate ages, scores, time limits, dollar amounts or
  approval authorities; the agent reads those from the source.
- Every cited paragraph exists in `catalog/source_catalog.json`; the build fails on any citation it
  cannot find. Citations an agent reads from a chapter that exists only as a PDF are labelled
  "from PDF, not catalog-verified".
- Where a USAREC message changes a paragraph, the agent shows both and says which is newer instead of
  silently choosing. Authority: AR 601-210, then other ARs/DoDIs/DA PAMs, then USAREC regs, manuals and
  current messages, then guides.
- No applicant PII.

## Source library

`markdown` paths inside the seeds are relative to this repo's own `doctrine/` folder — the chapter
text is bundled here, so a cloud agent with just this repo checked out can load it directly, no access
to the author's private library required. `pdf` paths are informational only (the original PDF filename,
for a human to cross-reference against the author's library); the PDFs themselves are not in this repo.
AR 601-210 in the library is the 20 March 2026 edition, effective 20 April 2026. The newest USAREC
message is dated 29 December 2025.

## Running the Multi-Agent Framework on Gemini

The repository includes a complete agent factory and runtime in `framework/`:

1. **Interactive Recruiter CLI**:
   ```bash
   python framework/cli.py
   ```
   Or ask a single query with location context:
   ```bash
   python framework/cli.py -q "What is the enlistment age limit?" -l "Charlotte MEPS"
   ```
2. **View Compiled Agent Web**:
   ```bash
   python framework/cli.py --roster
   ```
3. **Live Gemini Inference**:
   Set `GEMINI_API_KEY` in your environment to run live completions against Gemini models (`gemini-2.0-flash`). If no key is set, the CLI runs in dry-run mode, proving prompt construction, trigger matching, and doctrine grounding.

## Ingesting New Policy Knowledge

When a new USAREC or USARD policy message is released:
```bash
python scripts/ingest_message.py --number "26-025" --subject "Updated Medical Prescreen Timeline" --rescinds "24-053" --amends-doc "AR_601-210" --amends-para "2-9"
```
This automatically updates `catalog/usarec_message_catalog.json`, marks rescinded messages, and links the new policy to affected agent seeds in `yaml/`.

## Regenerate

From `build/`: `python catalog.py`, `python msgs.py`, `python -B build_seeds.py`
(`--validate-only` checks citations without writing). Seeds are authored in `exemplars.py` and
`seeds_*.py`; `AUTHORING.md` has the authoring rules and `lookup.py` the research helper.
