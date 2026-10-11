"""Build the source catalog: one entry per canonical doctrine document."""
import os, re, json
ROOT = r"C:\Users\joshu\..Project\Station_Commander\Army_Doctrine"
CATS = ["Regulations", "Manuals", "Pamphlets", "DoDI", "Guides", "ADP", "FM", "Certificates", "Forms"]
SKIP_MANUAL_DUPES = {"UR_10-1_(28Sep22)", "UR_5-01", "UR_601-210_1", "UR_601-37"}
# Regulations/ copies of these two are a 2022/2021 working draft superseded by the
# 2024 Manuals/ copy (different page counts/metadata, not a byte-identical dupe) -
# keep the current Manuals/ version as canonical instead.
SKIP_REGULATIONS_DUPES = {"UR_350-1", "UR_350-13"}
UNTITLED_PARA = ("UM_", "USAREC_MANUAL", "UTC_", "UTP_", "FM_", "ADP_", "STP")
MONTHS = "January|February|March|April|May|June|July|August|September|October|November|December"
DATE = re.compile(r'\b(\d{1,2})\s+(' + MONTHS + r'),?\s+(\d{4})\b')
PARA = re.compile(r'^\s*(\d{1,2})\s?[–\-]\s?(\d{1,3})\.\s+([A-Z][^\n]{2,120})$')
CHAP = re.compile(r'^\s*(Chapter|Appendix)\s+([0-9A-Z]{1,3})\s*$')

def authority(doc):
    if doc == "AR_601-210": return 1
    if doc.startswith(("AR_", "DoDI", "DA_PAM", "AD")): return 2
    if doc.startswith(("UR_", "UM_", "USAREC_MANUAL", "USAREC_Suppl")): return 3
    return 4

def read(p):
    return open(p, encoding="utf-8", errors="replace").read().splitlines()

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
        # chapters + titled paragraphs, assigned by paragraph-number prefix
        titled = not name.startswith(UNTITLED_PARA)
        chap_files, chap_titles, paras = {}, {}, {}
        for f in tfiles:
            if f.startswith("00_Full"): continue
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
                    # wrapped titles: join one more line if it continues lowercase/short
                    if i + 2 < len(lines) and lines[i+2].strip() and not re.match(r'^(Section|\d)', lines[i+2].strip()) and len(t) > 70:
                        t += " " + lines[i+2].strip()
                    chap_titles.setdefault(cm.group(2), t)
                pm = PARA.match(l) if titled else None
                if pm:
                    ch, n, t = pm.group(1), pm.group(2), pm.group(3).strip()
                    if t.endswith((",", ";")): continue
                    if len(t.split()) > 12: t = " ".join(t.split()[:8]) + " …"
                    rec = {"title": t}
                    if section: rec["section"] = section
                    paras.setdefault(ch, {}).setdefault(f"{ch}-{n}", rec)
        for ch in sorted(set(chap_files) | set(chap_titles) | set(paras), key=lambda x: int(x) if x.isdigit() else 999):
            entry["chapters"][ch] = {"title": chap_titles.get(ch),
                                     "file": f"{entry['transform_dir']}/{chap_files[ch]}" if ch in chap_files else None,
                                     "paragraphs": dict(sorted(paras.get(ch, {}).items(), key=lambda kv: int(kv[0].split('-')[1])))}
        if tfiles and not titled: entry["gaps"].append("paragraphs are untitled in source; cite chapter/section headings only")
        if tfiles and titled and not paras: entry["gaps"].append("paragraph headings not extracted (numbering style differs); cite by chapter")
        cat[name] = entry
json.dump(cat, open("source_catalog.json", "w", encoding="utf-8"), indent=1, ensure_ascii=False)
print(len(cat), "documents")
for k, v in cat.items():
    if v["category"] in ("Regulations", "Manuals", "Pamphlets", "DoDI"):
        print(f'{k:45} L{v["authority_level"]} {str(v["edition_date"]):18} eff={str(v["effective_date"]):18} ch={len(v["chapters"])} paras={sum(len(c["paragraphs"]) for c in v["chapters"].values())} {v["gaps"]}')
