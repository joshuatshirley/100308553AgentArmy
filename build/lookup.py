"""Lookup helper for seed authors.

  python lookup.py doc AR_601-210            -> chapters, files, paragraph headings
  python lookup.py doc AR_601-210 4          -> one chapter only
  python lookup.py find tattoo               -> documents whose id/title match
  python lookup.py msg tattoo waiver         -> USAREC messages whose subject matches ALL words
  python lookup.py msgbody 24-017            -> first 3000 chars of a message's text
  python lookup.py forms 601-210             -> form folders matching
  python lookup.py grep AR_601-210 4 "waiting period"  -> lines in that chapter's markdown containing the phrase
"""
import json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = r"C:\Users\joshu\..Project\Station_Commander\Army_Doctrine"
cat = json.load(open(os.path.join(HERE, "source_catalog.json"), encoding="utf-8"))
msgs = json.load(open(os.path.join(HERE, "messages.json"), encoding="utf-8"))

def doc(d, ch=None):
    e = cat[d]
    print(d, "| L%s" % e["authority_level"], "| edition", e["edition_date"], "| gaps", e["gaps"])
    for c, v in e["chapters"].items():
        if ch and c != ch: continue
        print(f"  Ch.{c}: {v['title']}  [{v['file']}]")
        for p, r in v["paragraphs"].items():
            print(f"     {p}  {r['title']}" + (f"   <{r['section']}>" if r.get("section") else ""))

cmd, args = sys.argv[1], sys.argv[2:]
if cmd == "doc": doc(args[0], args[1] if len(args) > 1 else None)
elif cmd == "find":
    q = " ".join(args).lower()
    for k, e in cat.items():
        if q in k.lower(): print(k, "|", e["category"], "| chapters", len(e["chapters"]), "| gaps", e["gaps"])
elif cmd == "msg":
    for n in sorted(msgs, reverse=True):
        s = (msgs[n]["subject"] or "").lower()
        if all(w.lower() in s for w in args):
            m = msgs[n]; print(n, "|", m["subject"][:140], "|", m.get("status", ""), "| rescinded_by", m.get("rescinded_by"))
elif cmd == "msgbody":
    t = open(os.path.join(ROOT, "USAREC_Messages_Consolidated.md"), encoding="utf-8", errors="replace").read()
    parts = re.split(r"^## USAREC Message (\d\d-\d{3})\s*$", t, flags=re.M)
    d = {parts[i]: parts[i + 1] for i in range(1, len(parts), 2)}
    print(re.sub(r"[ \t]+", " ", d[args[0]][:3000]))
elif cmd == "forms":
    for f in sorted(os.listdir(os.path.join(ROOT, "Forms"))):
        if all(w.lower() in f.lower() for w in args): print(f)
elif cmd == "grep":
    d, ch, phrase = args[0], args[1], " ".join(args[2:]).lower()
    f = cat[d]["chapters"][ch]["file"]
    for i, l in enumerate(open(os.path.join(ROOT, f), encoding="utf-8", errors="replace")):
        if phrase in l.lower(): print(i + 1, l.rstrip()[:200])
