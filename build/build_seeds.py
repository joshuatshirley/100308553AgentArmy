"""Write agent-seeds/ next to the doctrine. Read-only on the doctrine itself."""
import json, os, re, sys
from collections import Counter

import glob, importlib

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from roster import ROSTER
from exemplars import EXEMPLARS

# every seeds_<group>.py contributes SEEDS = {agent_id: spec}; --only seeds_x.py validates one file
ONLY = sys.argv[sys.argv.index("--only") + 1] if "--only" in sys.argv else None
VALIDATE_ONLY = "--validate-only" in sys.argv or ONLY is not None
ALL = dict(EXEMPLARS) if not ONLY else {}
for path in sorted(glob.glob(os.path.join(HERE, "seeds_*.py"))):
    if ONLY and os.path.basename(path) != ONLY: continue
    mod = importlib.import_module(os.path.basename(path)[:-3])
    for k, v in mod.SEEDS.items():
        if k in ALL: print(f"duplicate seed {k} in {path}"); sys.exit(1)
        ALL[k] = v

ROOT = r"C:\Users\joshu\..Project\Station_Commander\Army_Doctrine"
OUT = os.path.join(ROOT, "agent-seeds")
GENERATED = "2026-10-05"

catalog = json.load(open(os.path.join(HERE, "source_catalog.json"), encoding="utf-8"))
messages = json.load(open(os.path.join(HERE, "messages.json"), encoding="utf-8"))

# ---------- verified titles (read from each document's own front matter) ----------
TITLES = {
    "AR_601-210": "Regular Army and Reserve Components Enlistment Program",
    "UR_601-210": "Enlistment & Accessions Processing",
    "UR_601-37": "Army Medical Recruiting Program",
    "UR_601-2": "Management of Centers of Influence Events",
    "UR_601-108": "Army Chaplain Recruiting Program",
    "UR_601-73": "Market Analysis to Support Recruiting Operations",
    "UR_608-1": "National Voter Registration Act",
    "UR_700-5": "Integrated Logistics Support",
    "UR_190-4(1)": "Incident Reporting",
    "UR_25-2": "USAREC Cybersecurity",
    "UR_25-30": "Information Management: Publishing",
    "UR_5-01": "USAREC Knowledge Management Procedures and Standards",
    "UR_350-1": "Training and Leader Development",
    "UR_10-1_(28Sep22)": "Organization and Functions",
    "UR_27-2(V3)": "Legal Support Services for the U.S. Army Recruiting Command",
    "USAREC_Suppl_1_to_AR_600_85": "USAREC Supplement 1 to AR 600-85, Army Substance Abuse Program",
    "AR_601-2": "Army Recruiting Support Programs",
    "AR_608-1": "Army Community Service",
    "AR_10-87": "Army Commands, Army Service Component Commands, and Direct Reporting Units",
    "AR_1-201": "Army Inspection Policy",
    "AR_11-2": "Risk Management and Internal Control Program",
    "AR_135-100": "Appointment of Commissioned and Warrant Officers of the Army",
    "AR_135-155": "Promotion of Commissioned Officers and Warrant Officers",
    "AR_135-178": "Enlisted Administrative Separations",
    "AR_140-10": "Assignments, Attachments, Details, and Transfers",
    "AR_140-111": "U.S. Army Reserve Reenlistment Program",
    "AR_600-37": "Unfavorable Information",
    "AR_600-8-104": "Army Military Human Resource Records Management",
    "AR_600-8-2": "Suspension of Favorable Personnel Actions (Flag)",
    "AR_611-1": "Military Occupational Classification Structure Development and Implementation",
    "AR_614-200": "Enlisted Assignments and Utilization Management",
    "AR_623-3": "Evaluation Reporting System",
    "AR_380-67": "Personnel Security Program",
    "AR_190-45": "Law Enforcement Reporting",
    "AR_25-30": "Army Publishing Program",
    "AR_25-400-2": "Army Records Management Program",
    "AR_40-502": "Medical Readiness",
    "AR_600-9": "The Army Body Composition Program",
    "AR_601-280": "Army Retention Program",
    "AD2018-16": "Army Directive 2018-16 (Suitability Criteria for Military Personnel in Specified Positions)",
    "AD_2022-10": "Army Directive 2022-10 (Safe-to-Report for Victims of Sexual Assault)",
    "UM_3-31": "Station Operations",
    # corrected from wrong RAG chunk titles (verified against each document's cover)
    "UTC_5-02": "Intelligence",
    "UTC_5-03.1": "Prospecting, Processing, and Analysis",
    "UTC_5-03.2": "Influencing and Interviewing",
    "UTC_5-03.3": "Partnerships",
    "UTC_5-03.4": "Training and Leader Development",
    "UR_350-13": "School Recruiting Programs",
    "UR_25-30": "USAREC Business Cards",
}
# titles carried in the RAG chunks that are real titles, not just the folder id
chunk_titles = json.load(open(os.path.join(HERE, "chunk_titles.json"), encoding="utf-8"))["titles"]
for k, t in chunk_titles.items():
    if k in catalog and k not in TITLES and t and ":" in t and not t.lower().startswith(("da pam: ", "branch career")):
        TITLES[k] = t.split(":", 1)[1].strip()

def clean_chapter_title(t):
    if not t: return t
    t = re.sub(r",?\s*page \d+.*$", "", t)
    t = re.sub(r"\s+Chapter \d+\s*$", "", t)
    t = re.sub(r"(\w)- (\w)", r"\1\2", t)
    return t.strip()

chunk_chapters = json.load(open(os.path.join(HERE, "chunk_titles.json"), encoding="utf-8"))["chapters"]

def junk(t):
    return not t or t[0].islower() or t.startswith(("Figure", "Table", "or ", "and ")) or "...." in t or re.match(r"^\d", t)

for doc, e in catalog.items():
    e["title"] = TITLES.get(doc)
    e["title_verified"] = doc in TITLES
    last = None
    for ch, c in e["chapters"].items():
        c["title"] = clean_chapter_title(c["title"])
        if junk(c["title"]):
            alt = (chunk_chapters.get(doc) or {}).get(ch, "")
            alt = alt[3:].strip() if alt.startswith("## ") else None
            c["title"] = (alt.title() if alt and alt.isupper() else alt)
        if c["file"] is None and e["transform_dir"]:
            c["note"] = "chapter listed in front matter but not transformed to markdown; read the PDF"
        for p, rec in c["paragraphs"].items():
            if "section" not in rec and last: rec["section"] = last  # carry-over across chapter files
            last = rec.get("section")
    if doc == "UR_601-210":
        missing = [ch for ch, c in e["chapters"].items() if c["file"] is None]
        if missing: e["gaps"].append(f"chapters {', '.join(missing)} exist only in the PDF (not transformed)")
    if doc == "USAREC_MANUAL_3-0":
        e["gaps"].append("possible duplicate of UM_3-0 (same date and chapter titles, different PDF); UM_3-0 used as canonical")

# ---------- message catalog with currency flags ----------
def norm(s): return re.sub(r"[^a-z0-9 ]", "", (s or "").lower()).split(" summary")[0][:60]
by_subject = {}
for n in sorted(messages):
    by_subject.setdefault(norm(messages[n]["subject"]), []).append(n)
for n, m in messages.items():
    later = [x for x in by_subject[norm(m["subject"])] if x > n]
    m["newer_same_subject"] = later or None
    if m.get("rescinded_by"):
        m["status"] = "rescinded" if m.get("rescission_evidence") == "message text" else "rescinded per summary only - verify in PDF"
    elif later: m["status"] = "check: newer message with same subject"
    else: m["status"] = "no rescission found in library"
    m.pop("chars", None)
    pdf = os.path.join(ROOT, "USAREC Messages", f"USAREC_MESSAGE_{n}.pdf")
    m["pdf"] = f"USAREC Messages/USAREC_MESSAGE_{n}.pdf" if os.path.exists(pdf) else None
    if m.get("cites_ar_601_210_paragraph") or re.search(r"AR 601-210", m["subject"] or ""):
        m["review_flag"] = "changes or cites an AR 601-210 paragraph and predates the 20 March 2026 edition (effective 20 April 2026); confirm it still applies"

# ---------- validation of every citation used in seeds ----------
errors = []
def para_exists(doc, para):
    ch = para.split("-")[0]
    return para in catalog.get(doc, {}).get("chapters", {}).get(ch, {}).get("paragraphs", {})

def resolve_source(s):
    doc = s["doc"]
    if doc not in catalog: errors.append(f"unknown doc {doc}"); return s
    e = catalog[doc]
    out = {"doc": doc, "title": e["title"], "edition_date": e["edition_date"], "effective_date": e["effective_date"],
           "authority_level": e["authority_level"], "pdf": f"{e['path']}/{e['pdf']}" if e["pdf"] else None}
    ch = s.get("chapter")
    if ch and ch != "all":
        c = e["chapters"].get(ch)
        if not c: errors.append(f"{doc} chapter {ch} not in catalog"); return out
        out["chapter"] = ch
        out["chapter_title"] = c["title"]
        out["markdown"] = c["file"]
        if s.get("paragraphs") == "all":
            out["paragraphs"] = {p: r["title"] for p, r in c["paragraphs"].items()}
        elif s.get("paragraphs"):
            out["paragraphs"] = {}
            for p in s["paragraphs"]:
                if not para_exists(doc, p): errors.append(f"{doc} {p} not found")
                else: out["paragraphs"][p] = c["paragraphs"][p]["title"]
        if s.get("sections"): out["section_headings"] = s["sections"]
    else:
        out["chapter"] = "all"
        out["markdown"] = e["transform_dir"]
    if s.get("note"): out["note"] = s["note"]
    if e["gaps"]: out["known_gaps"] = e["gaps"]
    return out

def check_step_sources(flow, rid=""):
    # refs: "DOC 4-22" (paragraph), "DOC Ch.4" (chapter) or "DOC" (whole document)
    for st in flow:
        for ref in st.get("sources", []):
            parts = ref.split(" ", 1)
            doc, rest = parts[0], (parts[1] if len(parts) > 1 else "")
            if doc not in catalog: errors.append(f"{rid} step {st['step']}: unknown doc in '{ref}'"); continue
            if not rest: continue
            if rest.startswith("Ch."):
                if rest[3:] not in catalog[doc]["chapters"]: errors.append(f"{rid} step {st['step']}: {ref} chapter not found")
            elif not para_exists(doc, rest): errors.append(f"{rid} step {st['step']}: {ref} not found")

# ---------- tiny YAML writer (no PyYAML on this machine) ----------
SAFE = re.compile(r"^[A-Za-z0-9_][A-Za-z0-9 _./()'&,+-]*$")
def ys(v):
    if v is None: return "null"
    if isinstance(v, bool): return "true" if v else "false"
    if isinstance(v, int): return str(v)
    v = str(v)
    if SAFE.match(v) and not v.lower() in ("yes", "no", "true", "false", "null", "on", "off") and not re.match(r"^\d", v):
        return v
    return json.dumps(v, ensure_ascii=False)

def yaml(obj, ind=0):
    pad = "  " * ind
    lines = []
    if isinstance(obj, dict):
        for k, v in obj.items():
            key = ys(k)
            if isinstance(v, (dict, list)) and v:
                lines.append(f"{pad}{key}:")
                lines += yaml(v, ind + 1)
            elif isinstance(v, (dict, list)):
                lines.append(f"{pad}{key}: {'{}' if isinstance(v, dict) else '[]'}")
            else:
                lines.append(f"{pad}{key}: {ys(v)}")
    else:
        for v in obj:
            if isinstance(v, dict) and v:
                sub = yaml(v, ind + 1)
                lines.append(f"{pad}- {sub[0].lstrip()}")
                lines += sub[1:]
            elif isinstance(v, list):
                lines.append(f"{pad}-")
                lines += yaml(v, ind + 1)
            else:
                lines.append(f"{pad}- {ys(v)}")
    return lines

# roster source strings: check doc ids and any explicit paragraph refs
for r in ROSTER:
    for src in r["sources"]:
        doc = src.split(" ")[0]
        if doc.startswith("_") or doc in ("G1", "USAREC_Messages_Consolidated.md"): continue
        if doc not in catalog: errors.append(f"roster {r['id']}: unknown doc {doc}"); continue
        for a, b in re.findall(r"(\d{1,2}-\d{1,3})(?: to (\d{1,2}-\d{1,3}))?", src[len(doc):]):
            for p in (a, b):
                if p and not para_exists(doc, p): errors.append(f"roster {r['id']}: {doc} {p} not found")

# ---------- assemble ----------
roster_by_id = {r["id"]: r for r in ROSTER}
EXEMPLARS = ALL
for rid in EXEMPLARS:
    if rid not in roster_by_id: errors.append(f"seed {rid} is not in the roster")
for rid, ex in EXEMPLARS.items():
    for k in ex.get("hand_off_to", {}):
        if k not in roster_by_id: errors.append(f"{rid}: hand_off_to unknown agent {k}")
seeds = {}

def keyword_messages(r):
    words = [w.lower() for w in r["triggers"] if len(w) >= 3]
    hits = []
    for n, m in messages.items():
        s = (m["subject"] or "").lower()
        if any(re.search(r"\b" + re.escape(w) + r"\b", s) for w in words): hits.append(n)
    return sorted(hits, reverse=True)

written = []
for rid, ex in EXEMPLARS.items():
    r = roster_by_id[rid]
    seed = {
        "id": rid, "name": r["name"], "agent_type": ex["agent_type"], "group": r["group"],
        "status": "draft - for SME review", "generated": GENERATED,
        "maps_to_existing": r["maps_to"],
        "description": ex["description"],
        "scope": ex["scope"], "out_of_scope": ex["out_of_scope"],
    }
    if rid == "00_orchestrator":
        seed["applicant_facts_that_decide_routing"] = ex["applicant_facts_that_decide_routing"]
        seed["routing_table"] = [{"agent": x["id"], "name": x["name"], "triggers": x["triggers"]} for x in ROSTER if x["id"] != rid]
        seed["tie_break_rules"] = ex["tie_break_rules"]
        seed["conflict_rule"] = ex["conflict_rule"]
        seed["sources"] = [
            {"doc": "_source_catalog.json", "note": "every document, edition, authority level, chapter file and paragraph heading the specialists may cite"},
            {"doc": "_usarec_message_catalog.json", "note": "155 USAREC messages with subject and currency status"},
        ]
        seed["flow"] = ex["flow"]
        seed["answer_template"] = ex["answer_template"]
    else:
        seed["sources"] = [resolve_source(s) for s in ex["sources"]]
        seed["usarec_messages"] = [
            {"number": n, "subject": messages[n]["subject"], "status": messages[n]["status"],
             **({"rescinded_by": messages[n]["rescinded_by"]} if messages[n].get("rescinded_by") else {}),
             **({"newer_same_subject": messages[n]["newer_same_subject"]} if messages[n].get("newer_same_subject") else {}),
             **({"review_flag": messages[n]["review_flag"]} if messages[n].get("review_flag") else {}),
             "pdf": messages[n]["pdf"]}
            for n in ex["messages"] if (n in messages or errors.append(f"message {n} not in catalog"))
        ]
        seed["forms"] = []
        for f in ex["forms"]:
            p = os.path.join(ROOT, "Forms", f)
            if not os.path.isdir(p): errors.append(f"form folder {f} not found"); continue
            pdfs = [x for x in os.listdir(p) if x.lower().endswith(".pdf")]
            seed["forms"].append({"form": f, "pdf": f"Forms/{f}/{pdfs[0]}" if pdfs else None})
        seed["routing_triggers"] = ex["routing_triggers"]
        seed["clarifying_questions"] = ex["clarifying_questions"]
        seed["hand_off_to"] = ex["hand_off_to"]
        check_step_sources(ex["flow"], rid)
        seed["flow"] = ex["flow"]
    seed["example_questions"] = ex["example_questions"]
    seed["guardrails"] = ex["guardrails"]
    seed["provenance"] = {
        "doctrine_root": "Station_Commander/Army_Doctrine",
        "paths": "relative to doctrine_root; 'markdown' is the pre-split .transform text the agent should load at run time",
        "authority_levels": "1 AR 601-210; 2 other AR/DoDI/AD/DA PAM; 3 UR/UM/USAREC messages; 4 guides and training products",
        "editions": "edition and effective dates read from each document's front matter on " + GENERATED,
    }
    seeds[rid] = seed

if errors:
    print("CITATION ERRORS:"); [print(" ", e) for e in errors]; sys.exit(1)
if VALIDATE_ONLY:
    print(f"OK: {len(seeds)} seeds validated:", ", ".join(seeds)); sys.exit(0)

from render_md import render_agent_md, render_all_md
os.makedirs(os.path.join(OUT, "agents"), exist_ok=True)
os.makedirs(os.path.join(OUT, "agents_md"), exist_ok=True)
for rid in [r["id"] for r in ROSTER if r["id"] in seeds]:
    seed = seeds[rid]
    path = os.path.join(OUT, "agents", f"{rid}.yaml")
    open(path, "w", encoding="utf-8", newline="\n").write(f"# Agent seed: {seed['name']}\n" + "\n".join(yaml(seed)) + "\n")
    open(os.path.join(OUT, "agents_md", f"{rid}.md"), "w", encoding="utf-8", newline="\n").write(render_agent_md(seed, yaml))
    written.append(path)
open(os.path.join(OUT, "ALL_AGENTS.md"), "w", encoding="utf-8", newline="\n").write(render_all_md([seeds[r["id"]] for r in ROSTER if r["id"] in seeds], yaml))

# ---------- catalogs ----------
json.dump(catalog, open(os.path.join(OUT, "_source_catalog.json"), "w", encoding="utf-8", newline="\n"), indent=1, ensure_ascii=False)
json.dump(dict(sorted(messages.items(), reverse=True)), open(os.path.join(OUT, "_usarec_message_catalog.json"), "w", encoding="utf-8", newline="\n"), indent=1, ensure_ascii=False)

# ---------- roster index ----------
L = ["# Proposed agent roster", "",
     f"Generated {GENERATED} from `Station_Commander/Army_Doctrine`. One orchestrator plus {len(ROSTER) - 1} specialists.",
     "Every agent marked **seeded** has a full seed in `agents/<id>.md` (and `.yaml`). All are drafts pending SME review.",
     "`Maps to existing` refers to the 9 agents already built in FlorenceTaskingCommand (`agents/<dir>`).",
     "`Messages` is the number of USAREC messages the seed cites after checking each one.", ""]
group = None
for r in ROSTER:
    if r["group"] != group:
        group = r["group"]
        L += ["", f"## {group}", "", "| Agent | What it answers | Primary sources | Maps to existing | Messages | Status |", "|---|---|---|---|---|---|"]
    status = "**seeded**" if r["id"] in seeds else "proposed"
    msgs = (len(seeds[r["id"]].get("usarec_messages", [])) if r["id"] in seeds else len(keyword_messages(r))) if r["id"] not in ("00_orchestrator", "41_policy_currency") else "all"
    L.append(f"| `{r['id']}` {r['name']} | {r['summary']} | {'; '.join(r['sources'])} | {r['maps_to']} | {msgs} | {status} |")
open(os.path.join(OUT, "_roster_index.md"), "w", encoding="utf-8", newline="\n").write("\n".join(L) + "\n")

# ---------- stats for README ----------
cats = Counter(e["category"] for e in catalog.values())
stat = Counter(m["status"] for m in messages.values())
print("written:", *written, sep="\n  ")
print("catalog:", dict(cats), "| paragraphs:", sum(len(c["paragraphs"]) for e in catalog.values() for c in e["chapters"].values()))
print("messages:", dict(stat))
