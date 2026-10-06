# Doctrine gaps found while writing the seeds

Things the agents cannot cite precisely yet, grouped by fix. All dates are as found in the library.

## Chapters that exist only as PDF (convert to text to make them citable)

| Document | Missing chapters | Agents affected |
|---|---|---|
| UR 601-210 (3 Jan 2023) | 3 Recruiting Standards Program, 5 Live Scan, 6 QC, 7 DEP/DTP, 10 renegotiation, 13 RA options, 20 meals and lodging, 21 ERM, 22 RECBN liaisons, 23 OPAT, 24 temporary reservations, 25 OCS/WOFT | 08, 12, 15, 19, 21, 24, 25, 36, 38 |
| AR 670-1 | 3 (tattoos, grooming, religious accommodation) | 11 |
| DA PAM 670-1 | 3 | 11 |
| AR 600-20 | 2 (relationships), 5 (religious accommodation, family care plans), SHARP chapters | 04, 11, 36 |
| AR 40-501 | 2 (enlistment standards, height/weight tables) | 07, 08 |
| AR 40-502 | 3 (profiling) | 07 |
| AR 600-85 | 2 to 7 | 10, 39 |
| AR 380-67 | 3 (investigative requirements) | 12 |
| AR 135-100 (1994) | 2, 5 | 15 |
| DA PAM 601-6 | 3 | 15 |
| DA PAM 600-4 | 3, 5, 6 | 16 |
| UR 601-108 | all procedures | 17 |
| AR 601-280 | 4, 6, 7, 9 to 12 | 18 |
| AR 635-200 | 7 (defective enlistments) | 27 |
| DA PAM 611-21 | 2, 3 (MOS specs, line scores, physical demands) | 06, 22 |
| UR 350-1 | 2 to 4 | 34 |
| UR 350-13 | 2 to 9 | 29 |
| AR 601-2 | 6, 7 (HRAP/SRAP) | 32 |
| AR 360-1 | 3, 7, 8 (social media) | 33 |
| AR 15-6 | 2, 3, 6 | 36 |
| UR 190-4 | Table 2-1 (image), 3 to 5 | 36 |
| AR 735-5 | 7 to 10 (FLIPL) | 37 |
| AR 25-400-2 | 4, 6 | 38 |
| AR 608-1 | 2 to 4 | 39 |
| Personnel ARs | AR 600-8-2 Ch.2, AR 623-3 Ch.2-4, AR 600-8-22 Ch.3, 5, 8, AR 614-200 Ch.4-6, 8, AR 600-37 Ch.2, 4-6 | 35 |
| DA PAM 600-3 | 2, 6, 9, 10 | 43 |

Paragraph headings were not extracted (different numbering style) for the DoDIs, AR 600-9, AR 190-45,
AR 350-51, AR 601-1, DA PAM 601-280, AD 2018-16, AD 2022-10 and several USAREC regulations. FM 6-22,
FM 7-22, FM 1, FM 3-0, ADP 1 and ADP 3-0 are not split into chapters.

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
