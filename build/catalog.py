"""Build the source catalog: one entry per canonical doctrine document."""
import os, re, json
ROOT = r"C:\Users\joshu\..Project\Station_Commander\Army_Doctrine"
CATS = ["Regulations", "Manuals", "Pamphlets", "DoDI", "Guides", "ADP", "FM", "Certificates", "Forms"]
SKIP_MANUAL_DUPES = {"UR_10-1_(28Sep22)", "UR_5-01", "UR_601-210_1", "UR_601-37"}
# Regulations/ copies of these two are a 2022/2021 working draft superseded by the
# 2024 Manuals/ copy (different page counts/metadata, not a byte-identical dupe) -
# keep the current Manuals/ version as canonical instead.
SKIP_REGULATIONS_DUPES = {"UR_350-1", "UR_350-13"}
# These families print paragraph number + full prose on one line (no short title
# line of its own), so the strict PARA match below never fires for them. They get
# a looser, derived-snippet pass instead (see LOOSE_PARA) rather than being skipped.
UNTITLED_PARA = ("UM_", "USAREC_MANUAL", "UTC_", "UTP_", "FM_", "ADP_", "STP")
MONTHS = "January|February|March|April|May|June|July|August|September|October|November|December"
DATE = re.compile(r'\b(\d{1,2})\s+(' + MONTHS + r'),?\s+(\d{4})\b')
PARA = re.compile(r'^\s*(\d{1,2})\s?[–\-]\s?(\d{1,3})\.\s+([A-Z][^\n]{2,120})$')
# Flat directive-style numbering with no chapter prefix, e.g. AD 2018-16's "1. References.",
# "2. Purpose and Applicability" - used only as a fallback (see below), never instead of PARA.
PARA_FLAT = re.compile(r'^\s*(\d{1,2})\.\s+([A-Z][^\n]{2,120})$')
# Loose: paragraph number followed by the full prose paragraph on the same line (UM_/ADP_/FM_
# style manuals). Captures the whole line; the title gets derived by truncating to ~8 words.
LOOSE_PARA = re.compile(r'^\s*(\d{1,2})-(\d{1,3})\.\s+(.+)$')
# Dotted two-level numbering with no gap between the dots, e.g. newer DoDIs' "SECTION 2:
# RESPONSIBILITIES" / "2.1.  UNDER SECRETARY ...": section.subsection, period, title.
PARA_DOTTED = re.compile(r'^\s*(\d{1,2})\.(\d{1,3})\.\s+([A-Z][^\n]{2,120})$')
# USAREC Supplements amend specific paragraphs of their parent AR by number, e.g.
# "Paragraph 1-12, Objective and implementation" / "Add paragraph c after paragraph b."
PARA_SUPPLEMENT = re.compile(r'^\s*Paragraph\s+(\d{1,2}-\d{1,3}),\s+(.+)$')
CHAP = re.compile(r'^\s*(Chapter|Appendix)\s+([0-9A-Z]{1,3})\s*$')

def authority(doc):
    if doc == "AR_601-210": return 1
    if doc.startswith(("AR_", "DoDI", "DA_PAM", "AD")): return 2
    if doc.startswith(("UR_", "UM_", "USAREC_MANUAL", "USAREC_Suppl")): return 3
    return 4

def read(p):
    return open(p, encoding="utf-8", errors="replace").read().splitlines()

def junk(t):
    return not t or t[0].islower() or t.startswith(("Figure", "Table", "or ", "and ")) or "...." in t or re.match(r"^\d", t)

def snippet(t, limit=8):
    t = t.strip()
    if t.endswith((",", ";")): return None
    words = t.split()
    if len(words) > limit + 4:
        t = " ".join(words[:limit]) + " …"
    return t

def clean_filename_title(fname):
    t = re.sub(r'\.md$', '', fname)
    t = re.sub(r'^\d+_', '', t)           # strip the NN_ split-order prefix
    t = re.sub(r'^\d{1,3}\.?_+', '', t)   # strip an embedded "1._"/"8.__" paragraph remnant
    t = t.replace('_', ' ')
    t = re.sub(r'\s+', ' ', t).strip(' .')
    return t or "Untitled section"

cat = {}
for c in CATS:
    base = os.path.join(ROOT, c)
    for name in sorted(os.listdir(base)):
        full = os.path.join(base, name)
        if name.startswith(".") or not os.path.isdir(full): continue
        if c == "Manuals" and name in SKIP_MANUAL_DUPES: continue
        if c == "Regulations" and name in SKIP_REGULATIONS_DUPES: continue
        tdir = os.path.join(full, ".transform")
        pdfs = [f for f in os.listdir(full) if f.lower().endswith(".pdf")]
        tfiles = sorted(f for f in os.listdir(tdir) if f.endswith(".md")) if os.path.isdir(tdir) else []
        entry = {"doc_id": name, "category": c, "authority_level": authority(name),
                 "path": f"{c}/{name}", "pdf": pdfs[0] if pdfs else None,
                 "transform_dir": f"{c}/{name}/.transform" if tfiles else None,
                 "edition_date": None, "effective_date": None, "chapters": {}, "gaps": []}
        # edition date from the first front-matter-ish file
        head = []
        for f in tfiles[:2]:
            if f.startswith("00_Full"): continue
            head += read(os.path.join(tdir, f))[:80]
        for l in head:
            if entry["edition_date"] is None:
                m = DATE.search(l)
                if m and "supersede" not in l.lower() and "revision" not in l.lower(): entry["edition_date"] = f"{m.group(1)} {m.group(2)} {m.group(3)}"
            if entry["effective_date"] is None and l.strip().lower().startswith("effective"):
                m = DATE.search(l)
                if m: entry["effective_date"] = f"{m.group(1)} {m.group(2)} {m.group(3)}"
        if not tfiles: entry["gaps"].append("no .transform markdown; PDF only")

        # ---- Pass 1: standard "Chapter N" + "N-N. Title" extraction (unchanged shape) ----
        titled = not name.startswith(UNTITLED_PARA)
        chap_files, chap_titles, paras = {}, {}, {}
        for f in tfiles:
            lines = read(os.path.join(tdir, f))
            m = re.match(r'(\d+)_Chapter_(\d+)', f)
            if m: chap_files.setdefault(m.group(2), f)
            section = None
            for i, l in enumerate(lines):
                sm = re.match(r'^Section ([IVX]+)$', l.strip())
                if sm and i + 1 < len(lines): section = f"Section {sm.group(1)}: {lines[i+1].strip()}"
                cm = CHAP.match(l)
                if cm and cm.group(1) == "Chapter" and i + 1 < len(lines) and lines[i+1].strip():
                    t = lines[i+1].strip()
                    if i + 2 < len(lines) and lines[i+2].strip() and not re.match(r'^(Section|\d)', lines[i+2].strip()) and len(t) > 70:
                        t += " " + lines[i+2].strip()
                    chap_titles.setdefault(cm.group(2), t)
                pm = PARA.match(l)
                if pm:
                    ch, n, t = pm.group(1), pm.group(2), pm.group(3).strip()
                    if t.endswith((",", ";")): continue
                    if len(t.split()) > 12: t = " ".join(t.split()[:8]) + " …"
                    rec = {"title": t}
                    if section: rec["section"] = section
                    paras.setdefault(ch, {}).setdefault(f"{ch}-{n}", rec)

        # ---- Pass 2: loose derived-snippet paragraphs for UM_/ADP_/FM_-style manuals that
        # already have real chapters (from filenames) but print paragraph+prose on one line ----
        if not titled and (chap_files or chap_titles) and not paras:
            for f in tfiles:
                m = re.match(r'(\d+)_Chapter_(\d+)', f)
                if not m: continue
                ch = m.group(2)
                for l in read(os.path.join(tdir, f)):
                    lm = LOOSE_PARA.match(l)
                    if not lm: continue
                    n, body = lm.group(2), lm.group(3)
                    if junk(body): continue
                    t = snippet(body)
                    if not t: continue
                    paras.setdefault(ch, {}).setdefault(f"{ch}-{n}", {"title": t})

        # ---- Pass 3: fallback for docs with zero chapters from Pass 1 (DoDI section files,
        # flat-numbered directives like AD 2018-16, odd/garbled split filenames) - one chapter
        # per split file, keyed "S1", "S2"... by file order, titled from the filename ----
        fallback_order = []
        if tfiles and not chap_files and not chap_titles:
            idx = 0
            for f in tfiles:
                title = clean_filename_title(f)
                lines = read(os.path.join(tdir, f))
                body_chars = sum(len(l) for l in lines if l.strip()
                                  and not l.startswith("# Source:") and not l.startswith("--- [Page"))
                # Some real-content pages still carry a stray "Blank Page" TOC-bookmark title
                # (a source-PDF metadata quirk, not an indication the page is actually blank) -
                # only skip when the page truly has nothing on it.
                if title.lower() == "blank page" and body_chars < 80: continue
                idx += 1
                key = f"S{idx}"
                fallback_order.append(key)
                chap_titles[key] = title
                chap_files[key] = f
                for l in lines:
                    sm = PARA_SUPPLEMENT.match(l)
                    dm = None if sm else PARA_DOTTED.match(l)
                    if sm:
                        n, t = sm.group(1), sm.group(2).strip()
                    elif dm:
                        n, t = f"{dm.group(1)}.{dm.group(2)}", dm.group(3).strip()
                    else:
                        pm = PARA.match(l) or PARA_FLAT.match(l)
                        if not pm: continue
                        groups = pm.groups()
                        n, t = (groups[1], groups[2]) if len(groups) == 3 else (groups[0], groups[1])
                        t = t.strip()
                    if junk(t) or t.endswith((",", ";")): continue
                    if len(t.split()) > 12: t = " ".join(t.split()[:8]) + " …"
                    paras.setdefault(key, {}).setdefault(f"{key}-{n}", {"title": t})

        if fallback_order:
            for ch in fallback_order:
                entry["chapters"][ch] = {"title": chap_titles.get(ch),
                                         "file": f"{entry['transform_dir']}/{chap_files[ch]}" if ch in chap_files else None,
                                         "paragraphs": dict(paras.get(ch, {}))}
        else:
            for ch in sorted(set(chap_files) | set(chap_titles) | set(paras), key=lambda x: int(x) if x.isdigit() else 999):
                entry["chapters"][ch] = {"title": chap_titles.get(ch),
                                         "file": f"{entry['transform_dir']}/{chap_files[ch]}" if ch in chap_files else None,
                                         "paragraphs": dict(sorted(paras.get(ch, {}).items(), key=lambda kv: int(kv[0].split('-')[1])))}
        if tfiles and not entry["chapters"]: entry["gaps"].append("no paragraph or chapter structure recognized in source")
        elif tfiles and not any(c["paragraphs"] for c in entry["chapters"].values()):
            entry["gaps"].append("no paragraph numbering in source (narrative prose or reference tables); cite by chapter/section")
        cat[name] = entry
json.dump(cat, open("source_catalog.json", "w", encoding="utf-8"), indent=1, ensure_ascii=False)
print(len(cat), "documents")
for k, v in cat.items():
    if v["category"] in ("Regulations", "Manuals", "Pamphlets", "DoDI"):
        print(f'{k:45} L{v["authority_level"]} {str(v["edition_date"]):18} eff={str(v["effective_date"]):18} ch={len(v["chapters"])} paras={sum(len(c["paragraphs"]) for c in v["chapters"].values())} {v["gaps"]}')
