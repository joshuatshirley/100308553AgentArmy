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

Paragraph headings still aren't extracted (different numbering style) for the DoDIs, AR 600-9,
AR 190-45, AR 350-51, AR 601-1, DA PAM 601-280, AD 2018-16, AD 2022-10 and several USAREC regulations.
FM 6-22, FM 7-22, FM 1, FM 3-0, ADP 1 and ADP 3-0 are not split into chapters. These are a different,
unrelated extractor limitation (not "exists only as PDF") and remain open.

## Not in the library

- **MEPCOM:** no USMEPCOM regulations at all (601-23 enlistment processing, 40-1 medical, 611-1 testing and others are public at mepcom.army.mil).
- **USAREC:** USAREC pamphlets, UTP 3-10.6 Chaplain Recruiting, UR 601-106 and UR 601-208 (all on recruiting.army.mil).
- **DoD manuals:** DoDM 1145.02 (ASVAB testing and MEPS processing).
- **Army regulations and directives:** AR 600-8-19, AR 621-202, AR 612-201, AR 145-1, AR 601-141, AR 601-100 and AR 40-562; Army Directive 2022-09 (tattoo locations).
- **Guard:** NGR 600-7.
- **Forms:** DA 5500/5501, DD 372, DA 3286, DA 5305 and UF 601-210.40.

## Out of date or conflicting

- UR 190-4 in the library is 2014; a July 2026 edition is posted.
- AR 600-9 is the 2013 edition. AR 350-51 is 2001, AR 135-101 is 1984 and UR 570-1 is 2006.
- AR 601-1 (2016) and STP 805K-79R-SMTG (2018) predate the 79R to 42T conversion.
- The folder holds two AR 40-501 PDFs (2019 and ARN45126), so it is unclear which is current.
- All 155 USAREC messages predate the March 2026 AR 601-210. 25 cite or change a specific paragraph and carry a review flag.
- Message 24-053's alcohol retest wait differs from AR 601-210 4-18b(1). Message 23-058 (age exceptions to policy) may conflict with the new 2-3 and 4-17. Message 26-013 changes 2-18. The seeds show both sides of each.
- UR 601-210 still names the APFT (17-5, 17-8e) where message 24-054 uses the AFT.
- Message 25-019 says UR 601-210 Ch.3 is obsolete.
- Messages 25-020 and 26-009 share a subject and date header; 26-009 rescinds 25-020.
- Messages 20-018 → 22-069 and 21-031 → 23-041: the rescission appears only in the machine summary or names an unrelated message. Verify in the PDF.

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
