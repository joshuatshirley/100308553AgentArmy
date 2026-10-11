# Doctrine gaps found while writing the seeds

Things the agents cannot cite precisely yet, grouped by fix. All dates are as found in the library.

## Chapters that existed only as PDF — resolved 2026-10-11

All 30 documents below have been re-split and transformed to markdown; every chapter listed as
missing is now in `catalog/source_catalog.json` with a `markdown` path under `doctrine/` in this
repo. Root cause: the PDF splitter's TOC-boundary logic silently dropped a chapter whenever (a) the
chapter had no split boundary recorded at all (29 of the 30 docs — a stale/incomplete historical run,
fixed by re-running the existing split+transform pipeline fresh) or (b) two chapters start on the
exact same PDF page (`AR 601-280` ch.10/11, `DA PAM 611-21` ch.1/2, `AR 25-400-2` ch.5/6, `AR 600-37`
ch.1/2) — in those four cases the "missing" chapter's text is physically present inside the
neighboring chapter's file (verified by grep), since a PDF page can only be assigned to one output
file; cite the neighboring chapter's file for those four.

Affected docs (all now complete): UR 601-210, AR 670-1, DA PAM 670-1, AR 600-20, AR 40-501, AR 40-502,
AR 600-85, AR 380-67, AR 135-100, DA PAM 601-6, DA PAM 600-4, UR 601-108 (needed `--deep` split; its
real chapter structure is one TOC level deeper than usual), AR 601-280, AR 635-200, DA PAM 611-21,
UR 350-1, UR 350-13, AR 601-2, AR 360-1, AR 15-6, UR 190-4, AR 735-5, AR 25-400-2, AR 608-1,
AR 600-8-2, AR 623-3, AR 600-8-22, AR 614-200, AR 600-37, DA PAM 600-3.

**Found in the process:** the library held two copies of UR 350-1 and UR 350-13 — one under
`Manuals/` (clean final PDF) and one under `Regulations/` (explicitly titled "Working Draft" in its
own PDF metadata, same printed edition date but an earlier/incomplete scan). The catalog build was
keeping the stale `Regulations/` draft; fixed to use the `Manuals/` copy as canonical.

## Paragraph/chapter citation text regenerated — 2026-10-11

The catalog build previously had two more holes: (1) it silently skipped any document whose PDF
didn't TOC-split into separate chapter files — i.e. every lone `00_Full_Document.md` — so documents
like AR 600-9, AD 2018-16, AD 2022-10, AR 190-45, AR 350-51, AR 601-1, several USAREC regulations and
all 7 DoDIs contributed **zero** chapters or paragraphs even though their text was already sitting
right there; (2) for the UM_/ADP_/FM_/STP/UTC_/UTP_ manual families, paragraph extraction was
disabled outright on the (correct, for most of them) assumption that they print the paragraph number
and the full prose on one line with no short title to extract — but that also meant a real, present
`Chapter N` structure (and plenty of extractable content in the ADP/FM/UM docs whose paragraph style
turned out to be `N-N. <sentence>`) never made it into the catalog either.

Fixed in three passes, 174 docs total, net **+7,488 paragraph citations** (5,139 → 12,627):
- Stopped skipping lone `00_Full_Document.md` files — unlocked standard `Chapter N` / `N-N. Title`
  extraction "for free" for AR 600-9, AR 135-101, AR 190-45, AR 350-51, AR 601-1, DA PAM 635-40,
  ADP 1/3-0/7-0, FM 6-22/7-22, and more.
- Added a derived-snippet pass for the UM_/ADP_/FM_ manuals that print `N-N. <full sentence>` with no
  separate title line (UM 3-0/3-29/3-30/3-31/3-32, most of ADP and FM) — the paragraph title is now the
  first ~8 words of the sentence instead of nothing.
- Added a fallback for documents with no `Chapter N` text at all — DoDIs (which use named `SECTION`s,
  not chapters), USAREC regs/supplements whose split used section titles instead of "Chapter N", and
  a flat `N. Title` directive format (AD 2018-16/2022-10) with no chapter prefix. Each split file
  becomes its own citable section, titled from its filename, with any numbered paragraphs inside it
  still extracted.

## Remaining gaps audited — 2026-10-11 (found 3 more real fixes, 1 real defect, rest confirmed dead ends)

Went through every doc still in the gap list by hand (reading the actual source text, not just the
gap message) to separate "genuinely nothing to extract" from "the extractor missed something real."

**Fixed:**
- **A third paragraph-numbering convention**, dotted `N.N. Title` (vs. the dashed `N-N.` and flat
  `N.` styles already handled) — used by the newer DoDIs' `SECTION N:` structure. This was the
  single highest-value fix: **DoDI 6130.03** (the core medical-disqualification instruction) went
  from 4 to 51 (vol 1) and 2 to 48 (vol 2) paragraphs — its Section 6 "Disqualifying Conditions" is
  now individually citable by condition (`MEDICAL STANDARDS`, `HEAD`, `EYES`, ...). Also unlocked
  DoDI 1304.28 (0→23) and DoDI 5120.08 (0→8).
- **USAREC Supplements amend specific paragraphs of their parent AR by number** (`Paragraph 1-12,
  Objective and implementation` / `Add paragraph c after paragraph b.`), a format the other three
  patterns didn't match. Added a dedicated pattern; USAREC Suppl 1 to AR 600-8-22 went 0→6.
- **A real bug in the fallback chapter-labeling code added this session**: any split file whose
  filename-derived title was literally "Blank Page" was skipped outright, on the assumption a page
  titled that way has nothing on it. Several don't — the PDF's own bookmark metadata just mislabels
  a page that actually holds the regulation's signature block, effective-date line, or (in one case)
  an entire fillable form. Fixed to check actual content length instead of trusting the label; this
  alone recovered real content UR 27-2(V3), UR 601-73, UR 690-6 were silently missing, plus
  `MRB_1_NEW_UPDATEv2` (a real form: "1.Type of Decline", "2. Component", ...).
- **`STP805K-79R-SMTG`** (the 79R recruiter MOS Soldier's Manual and Training Guide) was a genuine
  split failure, not a catalog bug: its 342-page PDF has real TOC bookmarks only on the last ~13
  pages, so the existing TOC-based splitter put pages 1–329 under "Front Matter" and the rest under
  nine entries all literally titled "Blank Page." Re-ran the split in manual whole-document mode
  (bypassing the useless TOC) to capture the complete 476KB/342-page text as one file instead of
  the ~350 bytes that had been sitting there.

**Diagnosed, not fixed — a real defect, different class of problem:** `ADP_2-0`'s PDF has a broken
embedded font — PyMuPDF extracts raw glyph codes instead of the right characters throughout the
*entire* document (confirmed isolated to this one doc; checked the rest of the library for the same
corruption and found none). The corruption is a constant +29 character-code shift (`$` → `A`,
`&KDSWHU` → `Chapter`), but shift-decoding also loses word-space boundaries unreliably, so a decoded
version would be close-but-wrong text — worse to publish than leaving it empty. Needs real font/CMap
-aware re-extraction (or OCR), not a text post-process; out of scope for this pass.

**Confirmed genuinely nothing to extract (26 docs):** read the actual source text for every one
rather than trusting the gap label. `240126_ITEMLC...` is a graphics-only flyer (`<USE_PDF>`, zero
text layer). `NCO_Charge` and `UF_608-6.1` are Adobe XFA/LiveCycle forms whose static text layer is
just the "upgrade your PDF viewer" placeholder — the real fields are dynamic XFA content PyMuPDF
can't reach. `UTC_5-03.1` does have `Chapter N` structure (already in the catalog) but its body text
extraction is too fragmented (large pull-quote text wrongly extracted as a run of one-line markdown
headings) to trust for paragraph-level citation. The rest — FM 1's narrative chapters, the GCRc/LiveScan
user guides, and the ~20 single-page DD/USAREC forms and checklists — genuinely have no numbered
paragraph structure in the source (bulleted checklists, blank fillable tables, screenshots). `New
folder` is an empty directory with no PDF at all. `USAREC_MANUAL_3-0`'s note is a known-duplicate
flag, not a gap. See `catalog/source_catalog.json` for the current list.

## Not in the library

**Fetched from public .mil sources — 2026-10-11:** USMEPCOM 601-23 (Entrance Processing and Data
Reporting Management, eff. 26 Feb 2024, from mepcom.army.mil), USMEPCOM 40-1 (Medical
Qualification Program, eff. 15 Dec 2020), USMEPCOM 611-1 (Enlistment Qualification Tests,
eff. 18 Mar 2024), UR 601-106 (Active Duty for Operational Support-Reserve Component Program,
eff. 10 Jul 2024, from recruiting.army.mil), UR 601-208 (Local Recruiting Marketing Program,
28 Oct 2015), and DoDM 1145.02 (MEPS, eff. 23 Jul 2018, Change 1 7 May 2025, from esd.whs.mil).
All six are now split, transformed and cataloged with zero extraction gaps (372 new paragraph
citations). None required a login — the sandbox's own `curl`/fetch tooling gets a blanket 403 from
`.mil` domains (confirmed: generic sites load fine, army.mil doesn't even with browser headers),
so these were pulled through an actual browser session instead.

Still not in the library (not attempted this pass):
- **USAREC:** USAREC pamphlets, UTP 3-10.6 Chaplain Recruiting (all reportedly on recruiting.army.mil).
- **Army regulations and directives:** AR 600-8-19, AR 621-202, AR 612-201, AR 145-1, AR 601-141, AR 601-100 and AR 40-562; Army Directive 2022-09 (tattoo locations).
- **Guard:** NGR 600-7.
- **Forms:** DA 5500/5501, DD 372, DA 3286, DA 5305 and UF 601-210.40.

## Out of date or conflicting

- **Resolved 2026-10-11:** AR 600-9 updated to the current ARN43120 edition (16 Jul 2019 text,
  27 Feb 2025 administrative revision) from armypubs.army.mil — was the 2013 edition. UR 601-2
  updated to the copy carrying the 11 September 2024 administrative revision (same effective date,
  25 June 2015, printed on the cover per Army convention — the revision is noted in the History
  paragraph, not the header date) — was missing that revision. The "two AR 40-501 PDFs, unclear
  which is current" note was wrong: `AR_40-501.pdf` and `AR_40-501_ARN45126.pdf` are byte-identical
  (same MD5) — not a real ambiguity, just the same file saved under two names.
- **Blocked by IRM, not fetched:** the public recruiting.army.mil links for the current UR 190-4
  (15 Jul 2026) and the current UR 350-13 (27 May 2026) both open to a "Switch to a work or school
  account" wall — Microsoft Information Rights Management requiring an authenticated .mil account.
  The bytes download but are encrypted; not usable. If you can open either from your own CAC-linked
  account, save it and hand me the PDF. UR 350-1's public link (claimed "admin revision 1 Jun 26")
  turned out to just serve the same stale "Working Draft" copy already known to be inferior to the
  library's `Manuals/UR_350-1` — not fetched, nothing to gain.
- AR 350-51 is 2001, AR 135-101 is 1984 and UR 570-1 is 2006 — not checked for a public current edition this pass.
- AR 601-1 (2016) and STP 805K-79R-SMTG (2018) predate the 79R to 42T conversion.
- All 155 USAREC messages predate the March 2026 AR 601-210. 25 cite or change a specific paragraph and carry a review flag.
- Message 24-053's alcohol retest wait differs from AR 601-210 4-18b(1). Message 23-058 (age exceptions to policy) may conflict with the new 2-3 and 4-17. Message 26-013 changes 2-18. The seeds show both sides of each.
- UR 601-210 still names the APFT (17-5, 17-8e) where message 24-054 uses the AFT.
- Message 25-019 says UR 601-210 Ch.3 is obsolete.
- Messages 25-020 and 26-009 share a subject and date header; 26-009 rescinds 25-020.
- Messages 20-018 → 22-069 and 21-031 → 23-041: the rescission appears only in the machine summary or names an unrelated message. Verify in the PDF.
- **System status, per station-level confirmation (2026-10-11):** GCRc, Leader Zone (LZ) and the LiveScan/WEBS setup guide are retired with no replacement guide published; Recruiter Zone is still in use but is being phased out in favor of AIE, which has no user guide yet. `40_systems_howto` was updated to say so rather than citing the GCRc/LiveScan guides as current or guessing at AIE's screens. The GCRc/LiveScan PDFs and catalog entries are left in the library as a historical record but are no longer cited by any agent.

## Cross-reference errors in the source text

- AR 601-210 2-9a cites "DoDI 6103.03" (should be 6130.03).
- AR 601-210 2-3a points to 6-14 for the oath; the oath is 6-16.
- AR 601-210 7-11h points to 3-18 for Reserve prior-service grade; the rule is in 3-17.
- UR 601-210 11-4d cites "AR 601-210 chapter 5-78"; the drug separation paragraph is 5-73.
- UR 601-210 15-4 cites AR 40-501 7-8e from an older edition.
- AR 601-210 9-12 (Program 9F) is in the text but was missed by the paragraph extractor.

## Source quality

- `USAREC_Messages_Consolidated.md` puts machine-written summaries in front of message text, and some contain errors. Agents quote only the Subject and Requirement lines or the PDF.
- The systems guides are dated (GCRc 2013, LiveScan/WEBS 2018, RZ guide undated).
