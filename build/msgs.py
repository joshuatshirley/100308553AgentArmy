import re, json
p = r"C:\Users\joshu\..Project\Station_Commander\Army_Doctrine\USAREC_Messages_Consolidated.md"
txt = open(p, encoding='utf-8', errors='replace').read()
parts = re.split(r'^## USAREC Message (\d\d-\d{3})\s*$', txt, flags=re.M)
msgs = {}
for i in range(1, len(parts), 2):
    num, body = parts[i], parts[i+1]
    m = re.search(r'^SUBJECT:\s*(.+?)(?:\n\s*\n|\n[A-Z0-9]\.|\n\d\.)', body, flags=re.M|re.S) or re.search(r'^Subject:\s*(.+)$', body, flags=re.M)
    subj = re.sub(r'\s+', ' ', m.group(1)).strip()[:160] if m else None
    # rescission phrasings seen in the library: "UM 24-050 is rescinded", "Rescinds: 25-002",
    # "Supersedes: 23-010", "this message supersedes UM 26-001", "replaces USAREC Message 22-023"
    pats = [
        r'(?:UM|Message|Msg)\s*#?\s*(\d\d-\d{3})\s+(?:is|has been|was)\s+(?:officially\s+)?rescinded',
        r'\b(?:Rescinds|Supersedes):\s*(\d\d-\d{3})',
        r'\b(?:rescinds|supersedes|replaces)\s+(?:previous\s+(?:guidance|requirement|message)\s*)?\(?(?:USAREC\s+|USARD\s+)?(?:UM|Message|Msg)?\s*#?\s*(\d\d-\d{3})',
        r'(?:UM|Message|Msg)\s*#?\s*(\d\d-\d{3}),[^.\n]{0,160}?(?:is|has been|was)\s+rescinded',
    ]
    # The consolidated file puts machine-written summaries in front of the message text. A rescission
    # counts as "message text" only when it also appears in a numbered Requirement line or a
    # "Rescinds:/Supersedes:" field; otherwise it is "summary only" and must be checked in the PDF.
    resc = {}
    for pt in pats:
        for mm in re.finditer(pt, body, flags=re.I):
            x = mm.group(1)
            if x >= num: continue
            line = body[body.rfind("\n", 0, mm.start()) + 1: body.find("\n", mm.end())]
            structured = bool(re.search(r'Requirement:|\b\d{1,2}\.\s|Rescinds:|Supersedes:', line))
            resc[x] = "message text" if structured or resc.get(x) == "message text" else "summary only - verify in PDF"
    resc = [{"number": k, "evidence": v} for k, v in sorted(resc.items())]
    exp = re.findall(r'(?:expire[sd]?|expiration|remain in effect until|rescission)[^.\n]{0,60}', body, flags=re.I)[:2]
    cites = bool(re.search(r'AR\s*601[-–]\s?210,?\s*(?:para(?:graph)?s?\.?|chapter|ch\.?|table)?\s*\d', body, flags=re.I))
    msgs.setdefault(num, {"subject": subj, "rescinds": resc, "expiry_text": exp, "cites_ar_601_210_paragraph": cites, "chars": len(body)})
rescinded = {r["number"]: (n, r["evidence"]) for n, v in msgs.items() for r in v["rescinds"]}
for n, v in msgs.items():
    v["rescinded_by"] = rescinded[n][0] if n in rescinded else None
    if n in rescinded: v["rescission_evidence"] = rescinded[n][1]
json.dump(msgs, open('messages.json','w',encoding='utf-8'), indent=1, ensure_ascii=False)
print(len(msgs), "messages;", sum(1 for v in msgs.values() if v['rescinded_by']), "rescinded;", sum(1 for v in msgs.values() if not v['subject']), "no subject")
