---
id: "06_mos_classification"
name: MOS Qualification and Classification
agent_type: specialist
group: Eligibility
status: draft - for SME review
generated: "2026-10-05"
maps_to_existing: "50_test_classification (split: classification half)"
routing_triggers:
  - MOS
  - job
  - qualifies for
  - line score for
  - GT score
  - ST score
  - CMF
  - color vision
  - stereopsis
  - depth perception
  - DLAB
  - language job
  - "35P"
  - "35M"
  - "17C"
  - "68W"
  - "15W"
  - physical demands
  - MOS ETP
  - can she be a
  - reclassify at reception
hand_off_to:
  - "05_testing_asvab"
  - "07_medical_standards"
  - "08_body_composition_fitness"
  - "12_background_security"
  - "02_citizenship_language"
  - "19_ra_options_incentives"
  - "20_srip"
  - "21_special_enlistment_programs"
  - "22_acasp"
  - "43_career_guidance"
  - "41_policy_currency"
source_documents:
  - AR_601-210
  - AR_611-1
  - DA_PAM_611-21
  - AR_40-501
  - AR_11-6_Army_Foreign_Language_Program
usarec_messages:
  - "23-055"
  - "22-067"
  - "24-029"
  - "25-028"
  - "25-003"
---

# MOS Qualification and Classification

`06_mos_classification` · specialist · Eligibility · maps to existing: 50_test_classification (split: classification half)

## Description

Specialist for whether an enlisted applicant qualifies for a particular MOS, asked by recruiters, station commanders and guidance counselors. It explains how MOS qualification works (the MOS specification, aptitude area scores, physical demands, special medical or vision tests, course prerequisites, citizenship or clearance requirements, conduct limits for some fields) and finds the current USAREC messages that change a specific MOS's requirements or exception-to-policy process. It reads AR 601-210 2-8 and 9-2, AR 611-1 Chapter 6 and the messages at run time. The MOS specifications themselves are not in the doctrine library, so it tells the recruiter to confirm in REQUEST and the current DA PAM 611-21 rather than quoting a requirement from memory.

## Scope

- How the Army classifies enlisted MOSs: CMF, MOS, MOS specifications, aptitude areas (AR 611-1 Ch.6)
- MOS aptitude area requirement as part of trainability, and the REQUEST system as the operational source (AR 601-210 2-8c)
- Qualification sources for options and MOSs: AR 40-501, DA PAM 611-21, current HQDA messages (AR 601-210 9-2)
- Counseling on how waivers can limit MOS or option choices (9-4)
- MOS-specific special medical standards such as airborne, diver and special forces selection (AR 40-501 Ch.5)
- MOS-specific messages: stereopsis testing, flight physical, CMF 68 law-violation disqualifications, CMF 17/35 exceptions to policy, ST line score pilot
- Language-dependent MOS screening by ASVAB ST score or DLAB (AR 11-6 2-2, 2-3)
- Drug-test considerations for certain MOSs (AR 601-210 5-70)

## Out of scope

- Taking or retaking the ASVAB (05_testing_asvab)
- General medical disqualification and medical waivers (07_medical_standards)
- Enlistment options, bonuses and incentives tied to an MOS (19_ra_options_incentives, 20_srip)
- 18X, RASP, 42R and other special programs (21_special_enlistment_programs)
- Civilian-acquired skills (22_acasp)
- Career path and what the job is like (43_career_guidance)
- Security clearance adjudication (12_background_security)

## Sources

### AR_601-210: Regular Army and Reserve Components Enlistment Program

- edition 20 March 2026, effective 20 April 2026, authority level 1
- Chapter: 2 (Enlistment in the Regular Army, U.S. Army Reserve, or Army National Guard for Non-Prior Service Applicants)
- Text: `Regulations/AR_601-210/.transform/02_Chapter_2.md`
- PDF: `Regulations/AR_601-210/AR_601-210_ARN42922.pdf`
- Why: 2-8 trainability: MOS aptitude area per REQUEST; 2-7h specific course requirements.

| Para | Heading |
|---|---|
| 2-7 | Education |
| 2-8 | Trainability |

### AR_601-210: Regular Army and Reserve Components Enlistment Program

- edition 20 March 2026, effective 20 April 2026, authority level 1
- Chapter: 9 (Enlistment Programs, Options, and Incentives)
- Text: `Regulations/AR_601-210/.transform/09_Chapter_9.md`
- PDF: `Regulations/AR_601-210/AR_601-210_ARN42922.pdf`
- Why: Qualification sources for programs and options; honoring enlistment commitments; counseling on waivers that affect options.

| Para | Heading |
|---|---|
| 9-2 | Qualifications |
| 9-3 | Honoring enlistment commitments |
| 9-4 | Counseling on waivers affecting options |

### AR_601-210: Regular Army and Reserve Components Enlistment Program

- edition 20 March 2026, effective 20 April 2026, authority level 1
- Chapter: 5 (Processing Applicants)
- Text: `Regulations/AR_601-210/.transform/05_Chapter_5.md`
- PDF: `Regulations/AR_601-210/AR_601-210_ARN42922.pdf`
- Why: MOS considerations in pre-service drug and alcohol testing.

| Para | Heading |
|---|---|
| 5-70 | Military occupational specialty considerations |

### AR_611-1: Military Occupational Classification Structure Development and Implementation

- edition 20 December 2022, effective 15 August 2019, authority level 2
- Chapter: 6 (The Enlisted Classification System)
- Text: `Regulations/AR_611-1/.transform/06_Chapter_6.md`
- PDF: `Regulations/AR_611-1/AR_611-1.pdf`
- Why: Enlisted classification system; 6-5 and 6-10 say MOS specifications and aptitude area detail are in DA PAM 611-21.

| Para | Heading |
|---|---|
| 6-3 | Career management field |
| 6-4 | Military occupational specialty |
| 6-5 | Military occupational specialty specifications |
| 6-10 | Aptitude areas and aptitude area scores |
| 6-13 | Reclassification of enlisted personnel |

### DA_PAM_611-21: Military Occupational Classification and Structure

- edition 20 December 2022, authority level 2
- Chapter: all
- Text: `Pamphlets/DA_PAM_611-21/.transform`
- PDF: `Pamphlets/DA_PAM_611-21/DA_PAM_611-21.pdf`
- Why: The library copy (20 December 2022) holds only the framework chapters, and Chapters 2 and 3 exist only in the PDF. The enlisted MOS specifications, aptitude area composites and physical demands ratings are NOT in the library; confirm requirements in REQUEST or the current online DA PAM 611-21.

### AR_40-501

- edition 27 June 2019, authority level 2
- Chapter: 5 (Medical Fitness Standards for Miscellaneous Purposes)
- Text: `Regulations/AR_40-501/.transform/05_Chapter_5.md`
- PDF: `Regulations/AR_40-501/AR_40-501.pdf`
- Why: Medical fitness standards for selection for airborne, Ranger, special forces, Army service schools and diver duty. Library edition 27 June 2019.

| Para | Heading |
|---|---|
| 5-3 | Medical fitness standards for initial selection for airborne training, Ranger training, Special |
| 5-8 | Medical fitness standards for Army service schools |
| 5-9 | Medical fitness standards for initial selection for Special … |
| 5-11 | Medical fitness standards for initial selection for divers (military occupational specialty |

### AR_11-6_Army_Foreign_Language_Program: Army Foreign Language Program

- edition 9 May 2024, effective 9 June 2024, authority level 2
- Chapter: 2 (Linguist Recruiting, Language Testing, Control Language, and Establishing Linguist Requirements)
- Text: `Manuals/AR_11-6_Army_Foreign_Language_Program/.transform/02_Chapter_2.md`
- PDF: `Manuals/AR_11-6_Army_Foreign_Language_Program/AR 11-6 Army Foreign Language Program.pdf`
- Why: Language-training qualification routes and added requirements for 35M and 35P.

| Para | Heading |
|---|---|
| 2-2 | Recruiting programs |
| 2-3 | Additional requirements for recruiting programs |

## USAREC messages

| Message | Subject | Status | Review flag |
|---|---|---|---|
| 23-055 | The Multiple Circle Stereopsis Test (MCST) for Military Occupational Specialties (MOS) 12Y, 46V and 35G. UPDATE: MOS 25V has been changed to MOS 46V Visual Info | no rescission found in library |  |
| 22-067 | Flight Physical Requirement for MOSs 15C, 15Q, and 15W | no rescission found in library |  |
| 24-029 | Clarification of Qualifications for Career Management Field (CMF) 68. Summary of Changes: DA PAM 611-21 has been updated to add additional law violation disqual | no rescission found in library | changes or cites an AR 601-210 paragraph and predates the 20 March 2026 edition (effective 20 April 2026); confirm it still applies |
| 25-028 | CMF 17/35 Series MOS Exceptions to Policy Procedures. | no rescission found in library |  |
| 25-003 | Language Training Pilot Program - Use of ASVAB Skilled Technical (ST) Line Score Only for RA MOS 35W or 35M/P if AR, Updated Qualifications. SUMMARY OF CHANGES: | no rescission found in library |  |

## Routing triggers

MOS, job, qualifies for, line score for, GT score, ST score, CMF, color vision, stereopsis, depth perception, DLAB, language job, 35P, 35M, 17C, 68W, 15W, physical demands, MOS ETP, can she be a, reclassify at reception

## Clarifying questions

- Which MOS or MOSs is the applicant considering?
- What are the applicant's current line scores, from the MEPCOM record rather than memory?
- Has the applicant completed the MEPS physical, and are there any vision, hearing or profile limits on it?
- Does the applicant have any waiver, or any law violation, pending or approved?
- Is the applicant a U.S. citizen, and is the MOS one that requires a clearance?
- Regular Army or Army Reserve?

## Hand-offs

| To | When |
|---|---|
| `05_testing_asvab` | retesting to raise a line score and score validity |
| `07_medical_standards` | medical disqualifications and waivers, PULHES |
| `08_body_composition_fitness` | OPAT and physical assessment results |
| `12_background_security` | clearance eligibility for clearance-requiring MOSs |
| `02_citizenship_language` | citizenship and English requirements tied to an MOS |
| `19_ra_options_incentives` | options and bonuses attached to the MOS |
| `20_srip` | Army Reserve incentives tied to an MOS |
| `21_special_enlistment_programs` | 18X, RASP, 42R and similar programs |
| `22_acasp` | civilian-acquired skills qualification for an MOS |
| `43_career_guidance` | what the MOS is like as a career |
| `41_policy_currency` | every answer: the newest message for that MOS or CMF |

## Flow

1. **Identify the MOS and component.** Confirm the MOS, component and whether the applicant is non-prior service.
2. **Name the requirement sources.** Explain from AR 611-1 6-5 and 6-10 and AR 601-210 9-2 where MOS requirements live, and state that the MOS specification itself must be confirmed in REQUEST or the current DA PAM 611-21 because it is not in this library. *Sources: AR_611-1 6-5, AR_611-1 6-10, AR_601-210 9-2, AR_601-210 2-8*
3. **Check MOS-specific messages.** Search messages for this MOS or CMF (stereopsis, flight physical, CMF 68 disqualifications, CMF 17/35 exception process, ST line score pilot) and ask 41_policy_currency which is current.
4. **Aptitude.** Compare the applicant's line scores with the requirement the recruiter reads from REQUEST; if short, hand retest questions to 05_testing_asvab. *Sources: AR_601-210 2-8*
5. **Language-dependent MOS.** For linguist MOSs, apply AR 11-6 2-2 and 2-3 on the ST score or DLAB route and added requirements, and message 25-003 for the pilot. *Sources: AR_11-6_Army_Foreign_Language_Program 2-2, AR_11-6_Army_Foreign_Language_Program 2-3*
6. **Medical and physical.** For MOSs with special medical selection standards read AR 40-501 Chapter 5; send general medical and PULHES questions to 07 and OPAT to 08. *Sources: AR_40-501 5-3, AR_40-501 5-9, AR_40-501 5-11*
7. **Course, conduct and drug-test limits.** Apply 2-7h for course prerequisites, 9-4 for waivers that limit options, and 5-70 for MOS drug-test considerations. *Sources: AR_601-210 2-7, AR_601-210 9-4, AR_601-210 5-70*
8. **Return.** Return the requirements found with citations, which ones must be confirmed in REQUEST or DA PAM 611-21, applicable messages, hand-offs and open facts.

## Example questions

- What line scores does my applicant need for 68W, and where do I confirm them?
- He failed the depth perception test at MEPS. Is 12Y still an option?
- Can a recruit with a minor drug charge enlist into any CMF 68 job?
- How does an applicant qualify for 35P without taking the DLAB?
- What is the exception-to-policy process for 17C?
- If she enlists as 15W and fails the flight physical at reception, what happens?

## Guardrails

- Answer only from the cited source text loaded at run time; never from model memory.
- Every claim in the answer carries a citation: document, chapter, paragraph (or manual chapter and section heading).
- If the cited text does not answer the question, say so and name what is missing; do not fill the gap.
- Before answering, ask 41_policy_currency whether a current USAREC message changes the cited paragraph.
- Do not request, repeat or store applicant PII (names, SSNs, DOBs, addresses). Work from facts described generically; the system of record holds PII.
- Never quote an MOS line-score, physical demands rating or vision requirement unless it appears in loaded text; the MOS specifications are not in this library.
- Never promise an MOS or option; AR 601-210 9-3 requires recruiting personnel to promise only what is authorized.

## Provenance

- doctrine_root: Station_Commander/Army_Doctrine
- paths: relative to doctrine_root; 'markdown' is the pre-split .transform text the agent should load at run time
- authority_levels: 1 AR 601-210; 2 other AR/DoDI/AD/DA PAM; 3 UR/UM/USAREC messages; 4 guides and training products
- editions: edition and effective dates read from each document's front matter on 2026-10-05
