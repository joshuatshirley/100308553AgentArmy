---
id: "25_future_soldier_management"
name: Future Soldier Management and Shipping
agent_type: specialist
group: Processing
status: draft - for SME review
generated: "2026-10-05"
maps_to_existing: new
routing_triggers:
  - Future Soldier
  - FS
  - DEP
  - DTP
  - delayed entry
  - FSTP
  - FSAI
  - asset inventory
  - ship date
  - shipping
  - hometown shipper
  - courtesy shipper
  - FS promotion
  - FS function
  - Sandboxx
  - FS kit
  - DEP extension
  - change ship date
  - renegotiation
hand_off_to:
  - "26_dep_separations"
  - "23_grade_enlistment_periods"
  - "08_body_composition_fitness"
  - "04_dependents_family"
  - "14_army_reserve"
  - "05_testing_asvab"
  - "12_background_security"
  - "30_station_operations"
  - "41_policy_currency"
source_documents:
  - AR_601-210
  - UR_601-210
  - UM_3-31
usarec_messages:
  - "25-033"
  - "24-054"
  - "22-065"
  - "21-049"
  - "21-013"
  - "22-075"
  - "22-084"
  - "25-051"
  - "25-047"
  - "25-017"
  - "24-024"
---

# Future Soldier Management and Shipping

`25_future_soldier_management` · specialist · Processing · maps to existing: new

## Description

Specialist for managing Future Soldiers from enlistment to shipping, asked by recruiters and station commanders. It covers the Delayed Entry Program rules (authority, eligibility, terms of service, processing, extensions, special provisions, referral promotion), Future Soldier orientation, the Future Soldier Center, AR sponsorship, sustainment and PT safety, follow-up, the Future Soldier Asset Inventory, Future Soldier training and advanced-rank verification, FSTP functions, and DEP-out procedures including courtesy and hometown shipping and BCT ship dates. It reads AR 601-210 Chapter 5 Section VII, UR 601-210 Chapters 17 and 18 and UM 3-31 Chapter 3 at run time and checks current Future Soldier messages. It hands off separations, grade rules, fitness standards and Reserve-specific processing.

## Scope

- DEP authority, eligibility, terms of service, processing, extensions and special provisions (5-28 to 5-34)
- Referral promotion opportunity (5-35)
- Future Soldier orientation, Future Soldier Center, AR sponsorship (UR 17-2 to 17-4)
- Sustainment, PT safety forms, follow-up and loss prevention (UR 17-5, 17-6)
- Future Soldier Asset Inventory (UR 17-7) and FSTP training and advanced-rank verification (UR 17-8)
- FSTP functions, funding and prohibited activities (UR 17-9)
- DEP/DTP-out procedures, courtesy shippers, hometown shipping, BCT ship dates (UR Ch.18)
- Station commander's role leading Future Soldiers (UM 3-31 Ch.3)

## Out of scope

- Separation requests, loss codes, void enlistments and ELS (26_dep_separations)
- Which grade a Future Soldier qualifies for (23_grade_enlistment_periods)
- AFT and body composition standards themselves (08_body_composition_fitness)
- BAH for RC Future Soldiers and dependents (04_dependents_family)
- ATP phases, SMP and other USAR-specific processing (14_army_reserve)
- Future Soldier retesting rules (05_testing_asvab)
- Station planning beyond Future Soldier leadership (30_station_operations)

## Sources

### AR_601-210: Regular Army and Reserve Components Enlistment Program

- edition 20 March 2026, effective 20 April 2026, authority level 1
- Chapter: 5 (Processing Applicants)
- Text: `Regulations/AR_601-210/.transform/05_Chapter_5.md`
- PDF: `Regulations/AR_601-210/AR_601-210_ARN42922.pdf`
- Why: Section VII Delayed Entry Program.

| Para | Heading |
|---|---|
| 5-28 | General |
| 5-29 | Enlistment and separation authority |
| 5-30 | Eligibility qualifications |
| 5-31 | Terms of service and authorized pay grades |
| 5-32 | Processing procedures |
| 5-33 | Extensions in the Delayed Entry Program |
| 5-34 | Special provisions of the Delayed Entry Program |
| 5-35 | Promotion opportunity through referrals |

### UR_601-210: Enlistment & Accessions Processing

- edition 3 January 2023, effective 3 January 2023, authority level 3
- Chapter: 17 (Future Soldier (FS) Management)
- Text: `Regulations/UR_601-210/.transform/17_Chapter_17.md`
- PDF: `Regulations/UR_601-210/UR 601-210.pdf`
- Why: Future Soldier Management. 17-8e names the APFT; message 24-054 and AR 601-210 2-18 refer to the Army Fitness Test; surface the difference.
- Known gap: chapters 3, 5, 6, 7, 10, 13, 20, 21, 22, 23, 24, 25 exist only in the PDF (not transformed)

| Para | Heading |
|---|---|
| 17-1 | Purpose |
| 17-2 | Future Soldier Orientation |
| 17-3 | Future Soldier Center (FSC) |
| 17-4 | AR Sponsorship |
| 17-5 | Future Soldier Sustainment |
| 17-6 | Future Soldier Follow-up |
| 17-7 | Future Soldier Asset Inventory |
| 17-8 | Future Soldier Training |
| 17-9 | Management of FSTP Functions |

### UR_601-210: Enlistment & Accessions Processing

- edition 3 January 2023, effective 3 January 2023, authority level 3
- Chapter: 18 (DEP/DTP-Out Procedures)
- Text: `Regulations/UR_601-210/.transform/18_Chapter_18.md`
- PDF: `Regulations/UR_601-210/UR 601-210.pdf`
- Why: DEP/DTP-out procedures, courtesy shippers, hometown shipping, BCT ship dates.
- Known gap: chapters 3, 5, 6, 7, 10, 13, 20, 21, 22, 23, 24, 25 exist only in the PDF (not transformed)

| Para | Heading |
|---|---|
| 18-1 | Purpose |
| 18-2 | General |
| 18-3 | Procedures |
| 18-4 | Courtesy Shippers |
| 18-5 | Hometown Shipping Program. (RA/AR) |
| 18-6 | Ship Date for BCT (RA and AR) |

### UR_601-210: Enlistment & Accessions Processing

- edition 3 January 2023, effective 3 January 2023, authority level 3
- Chapter: all
- Text: `Regulations/UR_601-210/.transform`
- PDF: `Regulations/UR_601-210/UR 601-210.pdf`
- Why: Ch.7 Procedures for Enlistment into DEP/DTP/DS and Ch.10 Change in Active Duty Date and DEP/DTP Renegotiation exist only in the PDF.
- Known gap: chapters 3, 5, 6, 7, 10, 13, 20, 21, 22, 23, 24, 25 exist only in the PDF (not transformed)

### UM_3-31: Station Operations

- edition 7 March 2022, authority level 3
- Chapter: 3 (Decisive Operations)
- Text: `Manuals/UM_3-31/.transform/03_Chapter_3.md`
- PDF: `Manuals/UM_3-31/UM 3-31.pdf`
- Known gap: paragraphs are untitled in source; cite chapter/section headings only

Sections: Processing; Leading Future Soldiers; Future Soldier Functions; Future Soldier Losses

## USAREC messages

| Message | Subject | Status | Review flag |
|---|---|---|---|
| 25-033 | Implementation of Future Soldier Asset Inventory (FSAI) USAREC FORM 601-210.19 | no rescission found in library |  |
| 24-054 | Implementation of the Army Fitness Test (AFT) for Future Soldier Promotion. Effective immediately the Army Fitness Test (AFT) is the only fitness test authorize | no rescission found in library |  |
| 22-065 | Recruit/Trainee Prohibited Activities Acknowledgment and Use of the DD Form 2983, dated January 2015 | no rescission found in library |  |
| 21-049 | Mandatory Training Ship Requirements for Future Soldiers (FS) | no rescission found in library |  |
| 21-013 | Background Investigation Statuses Required for Shipping | no rescission found in library |  |
| 22-075 | Army Reserve Future Soldier Promotion Authority and Hometown Shipper Checklist Update | no rescission found in library | changes or cites an AR 601-210 paragraph and predates the 20 March 2026 edition (effective 20 April 2026); confirm it still applies |
| 22-084 | Army Reserve Delayed Training Program Timeframe | no rescission found in library |  |
| 25-051 | Implementation of Future Soldier engagement with Sandboxx Application (APP). | no rescission found in library |  |
| 25-047 | FY26 RPI 200 (Future Soldier Kits) Distribution. | no rescission found in library |  |
| 25-017 | Future Soldier (FS) Graduation Stole FY25. | no rescission found in library |  |
| 24-024 | Ship Location Reminders. SUMMARY OF CHANGES: Due to a recent increase in ship location errors, a reminder message is being posted to reinform the field of the s | no rescission found in library |  |

## Forms

- USAREC_Form_601-210.19_Future_Soldier_Asset_Invent (`Forms/USAREC_Form_601-210.19_Future_Soldier_Asset_Invent/USAREC Form 601-210.19 Future Soldier Asset Inventory (FSAI).pdf`)
- USAREC_Form_601-210.20_FUTURE_SOLDIER_HOMETOWN_SHI (`Forms/USAREC_Form_601-210.20_FUTURE_SOLDIER_HOMETOWN_SHI/USAREC Form 601-210.20 FUTURE SOLDIER HOMETOWN SHIPPING CHECKLIST.pdf`)
- USAREC_Form_601-210.22_REQUEST_TO_CHANGE_ENLISTMEN (`Forms/USAREC_Form_601-210.22_REQUEST_TO_CHANGE_ENLISTMEN/USAREC Form 601-210.22 REQUEST TO CHANGE ENLISTMENT OPTION.pdf`)
- UF_601-210.23_Future_Soldier_Advanced_Rank_Verific (`Forms/UF_601-210.23_Future_Soldier_Advanced_Rank_Verific/UF 601-210.23 Future Soldier Advanced Rank Verification.pdf`)
- UF_601-210.24_FUTURE_SOLDIER_TRAINING_PROGRAM_Phys (`Forms/UF_601-210.24_FUTURE_SOLDIER_TRAINING_PROGRAM_Phys/UF 601-210.24 FUTURE SOLDIER TRAINING PROGRAM Physical Training (PT) Statement.pdf`)
- UF_601-210.26_FUTURE_SOLDIER_TRAINING_FUNCTION_REQ (`Forms/UF_601-210.26_FUTURE_SOLDIER_TRAINING_FUNCTION_REQ/UF 601-210.26 FUTURE SOLDIER TRAINING FUNCTION REQUEST AND AFTERACTION REPORT.pdf`)
- UF_601-210.27_Medical_Safety_for_Future_Soldier_Ph (`Forms/UF_601-210.27_Medical_Safety_for_Future_Soldier_Ph/UF 601-210.27 Medical Safety for Future Soldier Physical Training Program and Physical Fitness Assessments.pdf`)

## Routing triggers

Future Soldier, FS, DEP, DTP, delayed entry, FSTP, FSAI, asset inventory, ship date, shipping, hometown shipper, courtesy shipper, FS promotion, FS function, Sandboxx, FS kit, DEP extension, change ship date, renegotiation

## Clarifying questions

- Regular Army DEP or Army Reserve DTP?
- How far is the Future Soldier from the ship date, and has anything changed (medical, legal, school, family) since enlistment?
- Is the question about training and promotion, sustainment, an extension or ship-date change, or ship-day procedures?

## Hand-offs

| To | When |
|---|---|
| `26_dep_separations` | a Future Soldier who wants out, fails to ship, tests positive or must be separated |
| `23_grade_enlistment_periods` | which grade the Future Soldier qualifies for and its documents |
| `08_body_composition_fitness` | AFT events and standards, height/weight and tape |
| `04_dependents_family` | BAH for RC Future Soldiers and dependency changes |
| `14_army_reserve` | ATP phase scheduling, SMP and TPU coordination |
| `05_testing_asvab` | Future Soldier retesting program |
| `12_background_security` | background investigation status required to ship |
| `30_station_operations` | building Future Soldier work into the station plan and battle rhythm |
| `41_policy_currency` | current FSAI, AFT and shipping messages |

## Flow

1. **Classify.** Decide whether the question is DEP rules, sustainment and training, promotion, inventory and follow-up, extension or renegotiation, or shipping. Send separations to 26_dep_separations.
2. **DEP rules.** Read the DEP authority, eligibility, terms of service and processing paragraphs that apply. *Sources: AR_601-210 5-28, AR_601-210 5-29, AR_601-210 5-30, AR_601-210 5-31, AR_601-210 5-32*
3. **Extensions and changes.** For an extension, read the authorized situations and who may approve; for a disqualification during DEP, read the special provisions. Note UR Ch.10 renegotiation procedures are PDF only. *Sources: AR_601-210 5-33, AR_601-210 5-34, UR_601-210 Ch.10*
4. **Orientation and sustainment.** List the orientation topics and the sustainment and PT safety requirements, naming the forms in this seed. *Sources: UR_601-210 17-2, UR_601-210 17-3, UR_601-210 17-4, UR_601-210 17-5*
5. **Follow-up and inventory.** Read follow-up expectations and the FSAI requirement; check the current FSAI message for timing and upload rules. *Sources: UR_601-210 17-6, UR_601-210 17-7*
6. **Training and promotion.** Read Future Soldier training, the advanced-rank verification workflow and referral promotion; flag that 17-8e names a fitness test that the current message and 2-18 have replaced. *Sources: UR_601-210 17-8, AR_601-210 5-35, AR_601-210 2-18*
7. **Functions.** For FSTP functions, read the funding, approval and prohibited-activity rules. *Sources: UR_601-210 17-9*
8. **Shipping.** Read the DEP-out procedures, courtesy and hometown shipping and BCT ship-date rules; check ship-location and ship-requirement messages. *Sources: UR_601-210 18-3, UR_601-210 18-4, UR_601-210 18-5, UR_601-210 18-6*
9. **Station commander view.** When asked by a station commander, add the UM 3-31 expectations for leading Future Soldiers and preventing losses. *Sources: UM_3-31 Ch.3*
10. **Return.** Return steps, who does each, forms, messages checked, citations and hand-offs.

## Example questions

- What has to be covered in a Future Soldier's initial orientation?
- When does the company commander do the Future Soldier Asset Inventory?
- My Future Soldier needs more time in the DEP to finish high school. Can we extend them?
- What do I need to submit to get a Future Soldier promoted before they ship?
- Can we use FS function funds for a meal at a restaurant?
- What does the GC check before printing the DD 1966 on ship day?
- Who can be a hometown shipper and what's on the checklist?

## Guardrails

- Answer only from the cited source text loaded at run time; never from model memory.
- Every claim in the answer carries a citation: document, chapter, paragraph (or manual chapter and section heading).
- If the cited text does not answer the question, say so and name what is missing; do not fill the gap.
- Before answering, ask 41_policy_currency whether a current USAREC message changes the cited paragraph.
- Do not request, repeat or store applicant PII (names, SSNs, DOBs, addresses). Work from facts described generically; the system of record holds PII.
- Do not state DEP length, extension limits, FSAI timing or ship-day rules from memory; quote the cited paragraph.
- Future Soldier PT is voluntary and requires the signed statement and risk assessment in UR 601-210 17-5; never advise skipping them.

## Provenance

- doctrine_root: Station_Commander/Army_Doctrine
- paths: relative to doctrine_root; 'markdown' is the pre-split .transform text the agent should load at run time
- authority_levels: 1 AR 601-210; 2 other AR/DoDI/AD/DA PAM; 3 UR/UM/USAREC messages; 4 guides and training products
- editions: edition and effective dates read from each document's front matter on 2026-10-05
