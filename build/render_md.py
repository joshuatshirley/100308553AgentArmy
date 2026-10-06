"""Render a seed dict as markdown: YAML front matter (machine fields) + readable body.

Each agent file is self-contained. ALL_AGENTS.md concatenates them between
`<!-- BEGIN AGENT: id -->` / `<!-- END AGENT: id -->` markers so split_agents.py can cut it apart.
"""

FRONT_KEYS = ["id", "name", "agent_type", "group", "status", "generated", "maps_to_existing", "routing_triggers"]


def _front(seed, yaml):
    fm = {k: seed[k] for k in FRONT_KEYS if k in seed}
    if seed.get("hand_off_to"):
        fm["hand_off_to"] = list(seed["hand_off_to"])
    if seed.get("routing_table"):
        fm["routes_to"] = [r["agent"] for r in seed["routing_table"]]
    docs = []
    for s in seed.get("sources", []):
        if s["doc"] not in docs: docs.append(s["doc"])
    fm["source_documents"] = docs
    fm["usarec_messages"] = [m["number"] for m in seed.get("usarec_messages", [])]
    return "---\n" + "\n".join(yaml(fm)) + "\n---\n"


def _bullets(items):
    return "\n".join(f"- {i}" for i in items) + "\n"


def _cell(v):
    return str(v if v is not None else "").replace("|", "\\|").replace("\n", " ")


def render_agent_md(seed, yaml):
    L = [_front(seed, yaml), f"# {seed['name']}", "",
         f"`{seed['id']}` · {seed['agent_type']} · {seed['group']} · maps to existing: {seed['maps_to_existing']}", "",
         "## Description", "", seed["description"], "",
         "## Scope", "", _bullets(seed["scope"]),
         "## Out of scope", "", _bullets(seed["out_of_scope"])]

    if seed.get("applicant_facts_that_decide_routing"):
        L += ["## Applicant facts that decide routing", "", "| Fact | Why it matters |", "|---|---|"]
        L += [f"| {_cell(f['fact'])} | {_cell(f['why'])} |" for f in seed["applicant_facts_that_decide_routing"]] + [""]
    if seed.get("routing_table"):
        L += ["## Routing table", "", "| Agent | Name | Triggers |", "|---|---|---|"]
        L += [f"| `{r['agent']}` | {_cell(r['name'])} | {_cell(', '.join(r['triggers']))} |" for r in seed["routing_table"]] + [""]
    if seed.get("tie_break_rules"):
        L += ["## Tie-break rules", ""] + [f"{i}. {t}" for i, t in enumerate(seed["tie_break_rules"], 1)] + [""]
    if seed.get("conflict_rule"):
        c = seed["conflict_rule"]
        L += ["## Conflict rule", "", "Authority hierarchy:", "", _bullets(c["hierarchy"]), c["rule"], "", "Never:", "", _bullets(c["never"])]

    if seed.get("sources"):
        L += ["## Sources", ""]
        for s in seed["sources"]:
            head = f"### {s['doc']}" + (f": {s['title']}" if s.get("title") else "")
            L += [head, ""]
            meta = []
            if s.get("edition_date"): meta.append(f"edition {s['edition_date']}")
            if s.get("effective_date"): meta.append(f"effective {s['effective_date']}")
            if s.get("authority_level"): meta.append(f"authority level {s['authority_level']}")
            if meta: L += ["- " + ", ".join(meta)]
            if s.get("chapter"):
                L += [f"- Chapter: {s['chapter']}" + (f" ({s['chapter_title']})" if s.get("chapter_title") else "")]
            if s.get("markdown"): L += [f"- Text: `{s['markdown']}`"]
            if s.get("pdf"): L += [f"- PDF: `{s['pdf']}`"]
            if s.get("note"): L += [f"- Why: {s['note']}"]
            for g in s.get("known_gaps", []): L += [f"- Known gap: {g}"]
            L += [""]
            if s.get("paragraphs"):
                L += ["| Para | Heading |", "|---|---|"] + [f"| {p} | {_cell(t)} |" for p, t in s["paragraphs"].items()] + [""]
            if s.get("section_headings"):
                L += ["Sections: " + "; ".join(s["section_headings"]), ""]

    if seed.get("usarec_messages"):
        L += ["## USAREC messages", "", "| Message | Subject | Status | Review flag |", "|---|---|---|---|"]
        for m in seed["usarec_messages"]:
            st = m["status"] + (f" (rescinded by {m['rescinded_by']})" if m.get("rescinded_by") else "")
            st += (f" (newer: {', '.join(m['newer_same_subject'])})" if m.get("newer_same_subject") else "")
            L += [f"| {m['number']} | {_cell(m['subject'])} | {_cell(st)} | {_cell(m.get('review_flag', ''))} |"]
        L += [""]
    if seed.get("forms"):
        L += ["## Forms", ""] + [f"- {f['form']}" + (f" (`{f['pdf']}`)" if f.get("pdf") else "") for f in seed["forms"]] + [""]
    if seed.get("routing_triggers"):
        L += ["## Routing triggers", "", ", ".join(seed["routing_triggers"]), ""]
    if seed.get("clarifying_questions"):
        L += ["## Clarifying questions", "", _bullets(seed["clarifying_questions"])]
    if seed.get("hand_off_to"):
        L += ["## Hand-offs", "", "| To | When |", "|---|---|"] + [f"| `{k}` | {_cell(v)} |" for k, v in seed["hand_off_to"].items()] + [""]

    L += ["## Flow", ""]
    for st in seed["flow"]:
        L += [f"{st['step']}. **{st['name']}.** {st['action']}" + (f" *Sources: {', '.join(st['sources'])}*" if st.get("sources") else "")]
    L += [""]
    if seed.get("answer_template"):
        L += ["## Answer template", ""] + [f"{i}. {t}" for i, t in enumerate(seed["answer_template"], 1)] + [""]
    L += ["## Example questions", "", _bullets(seed["example_questions"]),
          "## Guardrails", "", _bullets(seed["guardrails"]),
          "## Provenance", "", _bullets([f"{k}: {v}" for k, v in seed["provenance"].items()])]
    return "\n".join(L).rstrip() + "\n"


def render_all_md(seeds, yaml):
    out = ["# Army Recruiting agent seeds", "",
           f"{len(seeds)} agents. Each block between `<!-- BEGIN AGENT: id -->` and `<!-- END AGENT: id -->` is one",
           "complete agent file (front matter included). Run `python scripts/split_agents.py ALL_AGENTS.md agents/` to split.", ""]
    for s in seeds:
        out += [f"<!-- BEGIN AGENT: {s['id']} -->", render_agent_md(s, yaml).rstrip(), f"<!-- END AGENT: {s['id']} -->", ""]
    return "\n".join(out)
