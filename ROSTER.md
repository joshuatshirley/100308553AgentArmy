# Proposed agent roster

Generated 2026-10-05 from `Station_Commander/Army_Doctrine`. One orchestrator plus 43 specialists.
Every agent marked **seeded** has a full seed in `agents/<id>.md` (and `.yaml`). All are drafts pending SME review.
`Maps to existing` refers to the 9 agents already built in FlorenceTaskingCommand (`agents/<dir>`).
`Messages` is the number of USAREC messages the seed cites after checking each one.


## Front door

| Agent | What it answers | Primary sources | Maps to existing | Messages | Status |
|---|---|---|---|---|---|
| `00_orchestrator` Army Recruiting Orchestrator | Classifies every question, gathers the facts that decide routing, dispatches to specialists, verifies their citations and merges one answer. | AR_601-210 (authority hierarchy anchor); _usarec_message_catalog.json | 00_router (same role; adds tie-break and conflict rules) | all | **seeded** |

## Eligibility

| Agent | What it answers | Primary sources | Maps to existing | Messages | Status |
|---|---|---|---|---|---|
| `01_basic_eligibility` Basic Eligibility (Non-Prior Service) | Age, name, SSN, trainability and the basic-criteria checklist for NPS applicants; age exceptions to policy. | AR_601-210 Ch.2 paras 2-1 to 2-6, 2-8; AR_601-210 4-17; DoDI_1304.26 | new | 2 | **seeded** |
| `02_citizenship_language` Citizenship, Immigration and Language | Citizenship and LPR status, naturalization, document translation, ECLT/English-language deficiency, foreign-language initiatives. | AR_601-210 2-4; UR_601-210 Ch.12 para 12-3, Ch.14; AR_11-6_Army_Foreign_Language_Program | new | 5 | **seeded** |
| `03_education_credentialing` Education Credentialing | Education tiers, school profile evaluation, alternate credentials, foreign education evaluation, transcripts, credential laundering. | AR_601-210 2-7; UR_601-210 Ch.16 | new | 3 | **seeded** |
| `04_dependents_family` Dependents and Family | Dependency rules for NPS and PS, dependents waivers, sole/surviving son or daughter, EFMP screening, BAH for RC Future Soldiers. | AR_601-210 2-10, 3-8, 4-19, 4-20 | 40_family_dependency (same) | 2 | **seeded** |
| `05_testing_asvab` Testing (ASVAB, PiCAT, ARMS) | ASVAB administration, retest policy, PiCAT/APT prescreen testing, special-purpose testing, ARMS, Future Soldier retesting. | AR_601-210 Ch.5 paras 5-6 to 5-11; DoDI_1304.02 | 50_test_classification (split: testing half) | 4 | **seeded** |
| `06_mos_classification` MOS Qualification and Classification | MOS prerequisites, line-score composites, physical demands, special MOS processing and MOS exceptions to policy. | DA_PAM_611-21; AR_611-1 | 50_test_classification (split: classification half) | 5 | **seeded** |
| `07_medical_standards` Medical Standards and Prescreen | Medical disqualifying conditions, prescreen procedures, medical waiver packets, behavioral health consults, MEPS physical. | DoDI_6130.03_vol_1; AR_40-501; AR_40-502; AR_601-210 4-5, 5-12, 5-13; UR_601-210 15-4 | 20_medical_triage (same) | 5 | **seeded** |
| `08_body_composition_fitness` Body Composition and Fitness | Height/weight and tape procedures for applicants and cadre, OPAT, Future Soldier PT safety, AFT for Future Soldier promotion. | AR_600-9; FM_7-22 | 20_medical_triage (split) | 3 | **seeded** |
| `09_conduct_waivers` Conduct and Administrative Waivers | Offense classification, waiverable vs nonwaiverable conduct and administrative disqualifications, approval authority, packets, waiting periods. | AR_601-210 Ch.4; AR_601-210 2-11; UR_601-210 Ch.15 | 30_legal_adjudication (same; drug and tattoo topics split out) | 5 | **seeded** |
| `10_drug_alcohol` Drug and Alcohol Screening | Applicant drug/alcohol testing, positive results, DAT waivers and separations, marijuana-related waivers. | AR_601-210 4-18, 5-66 to 5-76; AR_600-85; USAREC_Suppl_1_to_AR_600_85 | 30_legal_adjudication (split) | 3 | **seeded** |
| `11_appearance_accommodation` Tattoos, Appearance and Religious Accommodation | Tattoo and grooming standards, tattoo waiver submissions, religious accommodation exceptions to policy. | AR_670-1; DA_PAM_670-1 | 30_legal_adjudication (split) | 2 | **seeded** |
| `12_background_security` Background Screening and Security | Applicant background screening (tech check, NACLC/secret), SF 86 completion, NSOPW query, fingerprints/LiveScan, security clearance screening, SSN verification. | UR_601-210 Ch.9; AR_601-210 2-14; AR_380-67 | 70_administrative_forms (split: SF 86 / screening) | 10 | **seeded** |

## Applicant types

| Agent | What it answers | Primary sources | Maps to existing | Messages | Status |
|---|---|---|---|---|---|
| `13_prior_service` Prior Service and Glossary NPS | PS/GNPS eligibility (AR 601-210 Ch.3, not Ch.2), RE codes, RCP, verification of service, inter-service transfer, HRC business rules. | AR_601-210 Ch.3; AR_601-210 4-13, 4-23, 4-24; UR_601-210 Ch.8; AR_635-200; AR_135-178 | 60_prior_service (same) | 11 | **seeded** |
| `14_army_reserve` Army Reserve Processing | USAR-specific processing: ATP/split option, TPU vacancies, SMP, DMOSQ, conditional release DD 368, entry-level separations, renegotiations. | UR_601-210 Ch.12; AR_601-210 Ch.5 Sec V; AR_140-10; AR_140-111 | new | 10 | **seeded** |
| `15_officer_warrant_programs` Officer and Warrant Officer Programs | OCS, WOFT and warrant officer procurement, enlistment options 9D/9H/9I/9J, ROTC/USMA disenrollees, OCS/WOFT processing. | AR_601-210 9-10, 9-14 to 9-16; DA_PAM_601-6; AR_350-51; AR_135-100; UR_601-210 Ch.8 paras 8-4 to 8-8 | new | 4 | **seeded** |
| `16_amedd` AMEDD (Medical Recruiting) | AMEDD appointments: eligibility, AOC and CV review, packets and boards, HPSP/FAP/STRAP, AMEDD waivers (malpractice, license, conduct). | UR_601-37; DA_PAM_600-4; AR_135-101 | new | 24 | **seeded** |
| `17_chaplain` Chaplain Recruiting | Chaplain and chaplain candidate accession requirements and processing. | UR_601-108; DoDI_1304.28; DoDI_5120.08 | new | 3 | **seeded** |
| `18_retention_reenlistment` Retention and Reenlistment | Army retention program rules for cadre and in-service questions; Army Reserve reenlistment. | AR_601-280; DA_PAM_601-280; AR_140-111 | new | 0 | **seeded** |

## Contract

| Agent | What it answers | Primary sources | Maps to existing | Messages | Status |
|---|---|---|---|---|---|
| `19_ra_options_incentives` RA Enlistment Options and Incentives | Regular Army enlistment programs/options (9A-9C etc.), enlistment bonuses, honoring commitments, current incentive messages. | AR_601-210 Ch.9 paras 9-1 to 9-10, 9-20 | new | 6 | **seeded** |
| `20_srip` Selected Reserve Incentive Program | SRIP eligibility, suspension, termination and recoupment; Reserve enlistment/affiliation bonuses and SLRP. | AR_601-210 Ch.10; AR_601-210 9-18, 9-19 | new | 1 | **seeded** |
| `21_special_enlistment_programs` Special Enlistment Programs | 18X, RASP, musician 42R, 09M Future Soldier Prep Course, Enlisted Training Corps, conditional enlistment, remote DEP. | AR_601-210 Ch.9; UR_601-210 (program chapters not transformed; see gaps) | new | 11 | **seeded** |
| `22_acasp` Civilian-Acquired Skills Program | ACASP eligibility, qualification determination, grades and accelerated promotion for RA and USAR. | AR_601-210 Ch.7 | new | 2 | **seeded** |
| `23_grade_enlistment_periods` Pay Grade and Enlistment Periods | Authorized enlistment periods, enlistment pay grade and date of rank for NPS and PS, higher-grade verification, grade-determination ETPs. | AR_601-210 2-16 to 2-19; AR_601-210 3-14 to 3-17 | new | 4 | **seeded** |

## Processing

| Agent | What it answers | Primary sources | Maps to existing | Messages | Status |
|---|---|---|---|---|---|
| `24_processing_meps` Applicant Processing and MEPS | Processing elements and prohibitions, required forms (DD 1966 etc.), MEPS phase, oath, signatures and contract upload, IDs, lodging, ship-location accuracy. | AR_601-210 Ch.5 Sec I, Ch.6; UR_601-210 Ch.2, Ch.19 | 70_administrative_forms (extends) | 10 | **seeded** |
| `25_future_soldier_management` Future Soldier Management and Shipping | DEP/DTP rules, FS orientation, sustainment, FSTP, FSAI, FS promotions and referrals, hometown/courtesy shipping, ship-date rules. | AR_601-210 Ch.5 Sec VII; UR_601-210 Ch.17, Ch.18; UM_3-31 Ch.3 | new | 11 | **seeded** |
| `26_dep_separations` DEP Separations and Losses | Separation requests, failure to report, positive drug test separation, loss forgiveness, void enlistments, USAR entry-level separations. | UR_601-210 Ch.11; AR_601-210 5-73 to 5-76 | new | 2 | **seeded** |
| `27_post_enlistment_corrections` Post-Enlistment Commitments and Corrections | Unfulfilled or erroneous enlistment commitments, contract and grade corrections, extensions, incentive annex corrections. | AR_601-210 Ch.8 | new | 0 | **seeded** |

## Operations

| Agent | What it answers | Primary sources | Maps to existing | Messages | Status |
|---|---|---|---|---|---|
| `28_prospecting_leads` Prospecting and Lead Generation | Prospecting methods, lead refinement, Army interview, high-potential leads, texting operations, EMM Connect. | UM_3-32; UM_3-31 Ch.3, Ch.4; UM_3-30 Ch.2 | 10_prospecting (same) | 3 | **seeded** |
| `29_school_recruiting` School Recruiting Program | School recruiting program, ESS role, high school student protection guidance, educator events, HS testing program. | UM_3-31 Ch.4 (School Recruiting Program); AR_601-210 5-10 | 10_prospecting (split) | 1 | **seeded** |
| `30_station_operations` Station Operations and Command | Station commander duties: operations process, TLP, running estimates, RFA/SWOT, MAP, station recruiting plan, battle rhythm, AARs, IPRs. | UM_3-31; UM_3-0; UM_3-30; STP805K-79R-SMTG | new | 0 | **seeded** |
| `31_market_intelligence` Market Intelligence and Targeting | IPOE, market analysis, recruiting zones, targeting boards, event and geographic targeting, fusion cells, PAE. | UR_601-73; UM_3-29 Ch.3, Ch.4; UM_3-30 Ch.3; FM_2-0; ADP_2-0 | new | 0 | **seeded** |
| `32_coi_support_programs` COI Events and Recruiting Support Programs | COI event management, educator tours, HRAP/SRAP/ADOS-RC support soldiers, Soldier Referral Program. | UR_601-2; AR_601-2 | new | 2 | **seeded** |
| `33_marketing_public_affairs` Marketing, Public Affairs and Social Media | Army marketing program, local advertising, public affairs, visual information, social media standards. | DA_PAM_601-208; AR_360-1; UR_25-30 | 90_social_media_content (extends) | 0 | **seeded** |

## Command support

| Agent | What it answers | Primary sources | Maps to existing | Messages | Status |
|---|---|---|---|---|---|
| `34_training_development` Training and Leader Development | Training management at station/company, recruiter certification and training records, institutional/self-development, NCO development. | UR_350-1; UR_350-13; AR_350-1; FM_7-0; ADP_7-0; STP805K-79R-SMTG | 80_training_development (same) | 0 | **seeded** |
| `35_personnel_actions` Personnel Actions for Cadre | Awards, evaluations, flags, unfavorable information, records, enlisted assignments and assignment to USAREC, 42T/79R PAR submissions. | AR_600-8-22; USAREC_Suppl_1_to_AR_600_8_22; AR_623-3; DA_PAM_623-3; AR_600-8-2; AR_600-37; AR_600-8-104; AR_614-200; AR_601-1_10112016_Asg_of_Enl_Pers_to_USAREC | new | 2 | **seeded** |
| `36_military_justice_command` Military Justice, Investigations and Command Policy | Article 15, AR 15-6 investigations, command policy and EO, recruiter impropriety, law enforcement reporting, incident reporting, safe-to-report. | AR_27-10; AR_15-6; AR_600-20; AR_190-45; UR_190-4(1); UR_27-2(V3); AD_2022-10; AD2018-16 | new | 3 | **seeded** |
| `37_logistics_property` Logistics, Property and Equipment | Property accountability, financial liability investigations, supply discipline, logistics support, manpower and equipment control. | AR_735-5; UR_700-5; UR_570-1 | new | 2 | **seeded** |
| `38_it_records_knowledge` IT, Records and Knowledge Management | Cybersecurity, IT use, records management and retention, publications and forms, knowledge management standards. | UR_25-1(V3); UR_25-2; AR_25-1_15Jul19_IM_Army_IT; AR_25-2; AR_25-400-2; AR_25-13; AR_25-30; UR_5-01 | new | 1 | **seeded** |
| `39_soldier_family_wellness` Soldier and Family Wellness | SFRG, sponsorship, Army Community Service, ASAP for cadre, holistic health and fitness, risk assessment counseling, voter registration. | AR_608-1; UR_608-1; AR_600-85; FM_7-22; UM_3-30 Ch.5 | new | 0 | **seeded** |
| `40_systems_howto` Recruiting Systems How-To | Recruiter Zone, GCRc, REQUEST, LiveScan/WEBS setup, end-of-day reports, MHS Genesis access. | Recruiter+Zone+User+Guide+ver+6+05+010; GCRc+User+Guide+(GC-OPS); GCRc+Company+User+Guide(1); G6_Knowledge_Document_LiveScan_WEBS_2018_Set-up_Gu; UR_601-210 Ch.4, Ch.19 | new | 5 | **seeded** |

## Cross-cutting

| Agent | What it answers | Primary sources | Maps to existing | Messages | Status |
|---|---|---|---|---|---|
| `41_policy_currency` Policy Currency (USAREC Messages) | Finds the newest USAREC message on a topic, reports rescissions and supersessions, and flags operational changes to named paragraphs. | _usarec_message_catalog.json; USAREC_Messages_Consolidated.md | new | all | **seeded** |
| `42_leadership_doctrine` Army Leadership and Operations Doctrine | Mission command, operations process, leadership and counseling doctrine as applied to recruiting leaders. | ADP_6-22; FM_6-22; ADP_6-0; ADP_5-0; ADP_3-0; FM_3-0; ADP_1; FM_1 | new | 0 | **seeded** |
| `43_career_guidance` Career Paths and Branch Guidance | What a career in a CMF or branch looks like, officer talent management, career maps, civilian credentialing tie-ins, for applicant counseling. | DA_PAM_600-3; G1 CMF and branch career guides; DA_PAM_611-21 | new | 0 | **seeded** |
