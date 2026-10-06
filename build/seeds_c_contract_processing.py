"""Seeds for the Contract and Processing groups (roster ids 19 to 27).

Written against AR 601-210 (20 March 2026) and UR 601-210 (3 January 2023) chapter markdown.
Rule 1 applies throughout: no threshold, period, grade, amount or approval authority is stated
as fact; each step names the paragraph the agent must read at run time.
"""
from exemplars import COMMON_GUARDRAILS

MSG_SUMMARY_GUARDRAIL = (
    "Read a USAREC message's numbered Requirement lines or its PDF; never rely on the narrative summary "
    "paragraphs in the consolidated message file, which are machine-generated and contain known errors."
)

SEEDS = {}

# --------------------------------------------------------------------------------------------
SEEDS["19_ra_options_incentives"] = dict(
    agent_type="specialist",
    description=(
        "Specialist for Regular Army enlistment programs, options and incentives, asked by recruiters, "
        "station commanders and guidance counselors. It explains what each RA enlistment program (9A training, "
        "9B station-unit-command-area, 9C incentive) guarantees, which REQUEST options sit under each, what the "
        "applicant must be told before signing, how options combine, how waivers can affect option eligibility, "
        "and how the enlistment bonus, Army College Fund, Loan Repayment Program and PaYS work. It reads AR 601-210 "
        "Chapter 9 Sections I and II at run time and checks the current HQDA/USAREC incentive message, because "
        "REQUEST and that message decide what is actually offered. It hands off officer/warrant programs, special "
        "programs (18X, RASP, 42R, 09M, remote enlistment, conditional enlistment), Army Reserve incentives, "
        "ACASP, pay grade and post-enlistment contract fixes to the agents that own them."
    ),
    scope=[
        "Program 9A (U.S. Army Training Enlistment Program) and the REQUEST options listed under it",
        "Program 9B (Station-Unit-Command-Area) guarantees, stabilization and the information applicants must receive",
        "Program 9C incentives: enlistment bonus, Army College Fund, Loan Repayment Program, PaYS",
        "Qualifications for options and combining an additional option (RA only)",
        "Counseling applicants whose waivers may limit option eligibility",
        "Honoring enlistment commitments and where exception-to-policy requests on incentives go",
        "Reading the current RA enlistment incentives message alongside the regulation",
    ],
    out_of_scope=[
        "Program 9D OCS/WOFT and warrant officer programs (15_officer_warrant_programs)",
        "18X, RASP options, 42R, 09M prep course, remote enlistment, conditional enlistment, ETC (21_special_enlistment_programs)",
        "Army Reserve and SRIP incentives, SLRP for the Selected Reserve (20_srip)",
        "ACASP (22_acasp) and enlistment pay grade (23_grade_enlistment_periods)",
        "Fixing an option or incentive after enlistment (27_post_enlistment_corrections)",
        "Recruiter (cadre) incentive programs",
        "Quoting bonus amounts or availability; REQUEST is the source of what is offered",
    ],
    sources=[
        dict(doc="AR_601-210", chapter="9",
             paragraphs=["9-1", "9-2", "9-3", "9-4", "9-5", "9-7", "9-8", "9-9", "9-10", "9-20"],
             note="Section I general rules and Section II RA programs. 9-10 (9D) is listed so the agent can recognize it and hand off; 9-20 is the Secretariat review of accession incentives."),
        dict(doc="AR_601-210", chapter="5", paragraphs=["5-32"],
             note="Renegotiating options and incentives for DEP enlistees who no longer qualify for their option at shipment."),
        dict(doc="AR_601-210", chapter="10", paragraphs=["10-9"],
             note="Recoupment, referenced by 9-9 for security-clearance non-approval and for RC or former RC entering the RA."),
        dict(doc="DA_PAM_611-21", chapter="all",
             note="MOS prerequisites that options require before and after enlistment; chapters 2 and 3 were not transformed, read the PDF."),
        dict(doc="UR_601-210", chapter="all",
             note="Ch.13 Regular Army Options and Incentives exists only in the PDF; read it for USAREC procedures on RA options."),
    ],
    messages=["26-019", "26-001", "25-022", "21-051", "21-055", "21-047"],
    forms=["1966_printed"],
    routing_triggers=[
        "bonus", "enlistment bonus", "incentive", "option", "REQUEST option", "station of choice", "Option 19",
        "Option 20", "Alaska", "buddy team", "Option 18", "first assignment", "airborne option", "quick ship",
        "Army College Fund", "college fund", "loan repayment", "PaYS", "9A", "9B", "9C",
    ],
    hand_off_to={
        "15_officer_warrant_programs": "Program 9D OCS/WOFT and warrant officer enlistment options",
        "21_special_enlistment_programs": "18X, RASP (Options 40, 61, 62), 42R, 09M, remote enlistment, conditional enlistment, ETC",
        "20_srip": "any Army Reserve or Selected Reserve incentive, including RC members entering the RA with an RC bonus",
        "22_acasp": "civilian-acquired skills enlistment",
        "23_grade_enlistment_periods": "enlistment pay grade and term-of-service rules outside the option itself",
        "25_future_soldier_management": "renegotiation timing, ship dates and Future Soldier option changes before shipping",
        "27_post_enlistment_corrections": "an option or incentive that was promised, missing or wrong after enlistment",
        "06_mos_classification": "whether the applicant meets an MOS's line scores or physical prerequisites",
        "41_policy_currency": "every answer: the newest RA incentives message and any rescission",
    },
    clarifying_questions=[
        "Is the applicant non-prior service, prior service or glossary NPS?",
        "Which option or incentive is being asked about, and has REQUEST shown it as available for this applicant and MOS?",
        "Does the applicant need any waiver, or does the MOS need a security clearance?",
        "Is the applicant already in the DEP and renegotiating, or still processing?",
    ],
    flow=[
        dict(step=1, name="Identify the program", action="Place the question under 9A, 9B or 9C (or 9D, which goes to 15_officer_warrant_programs). If it names a special program in hand_off_to, hand it off.", sources=["AR_601-210 9-1", "AR_601-210 9-7", "AR_601-210 9-8", "AR_601-210 9-9", "AR_601-210 9-10"]),
        dict(step=2, name="Check qualifications", action="Read the qualification sources the regulation lists and the MOS prerequisites the option depends on; say what must be met before and after enlistment.", sources=["AR_601-210 9-2", "DA_PAM_611-21"]),
        dict(step=3, name="Read the guarantee", action="Quote what the program guarantees and what it does not (for example assignment, stabilization, course length), from the program paragraph.", sources=["AR_601-210 9-7", "AR_601-210 9-8"]),
        dict(step=4, name="Incentive terms", action="For 9C, read the enlistment bonus, Army College Fund, Loan Repayment and PaYS sub-paragraphs and list the conditions the applicant must be told (completion of training, serving in the MOS, clearance, recoupment). Do not state amounts.", sources=["AR_601-210 9-9", "AR_601-210 10-9"]),
        dict(step=5, name="Check the current message", action="Ask 41_policy_currency for the newest RA enlistment incentives message; state that REQUEST plus that message decide availability and minimum term of service, and report any change from what the regulation says."),
        dict(step=6, name="Combinations and waivers", action="Apply the additional-option rule and the waiver counseling rule; flag options that clearance or a waiver could void after enlistment.", sources=["AR_601-210 9-4", "AR_601-210 9-5"]),
        dict(step=7, name="Honoring commitments", action="Remind the recruiter to promise only what is authorized and where exception-to-policy requests on incentives go, as the text states.", sources=["AR_601-210 9-3", "AR_601-210 9-20"]),
        dict(step=8, name="DEP renegotiation", action="If a DEP enlistee no longer qualifies for the option at shipment, read the renegotiation rule and hand timing questions to 25_future_soldier_management.", sources=["AR_601-210 5-32"]),
        dict(step=9, name="USAREC procedure", action="Point to UR 601-210 Ch.13 (PDF only) for USAREC option procedures and say it was not checked in markdown.", sources=["UR_601-210 Ch.13"]),
        dict(step=10, name="Return", action="Return program, guarantee, required counseling points, the message checked, citations and hand-offs. Never quote a bonus amount as available."),
    ],
    example_questions=[
        "What does Option 19 actually guarantee my applicant, and what doesn't it guarantee?",
        "Can my applicant combine an enlistment bonus with Army College Fund?",
        "What happens to the bonus if a Soldier doesn't finish AIT?",
        "Who qualifies for PaYS, and what do I have to do before the Future Soldier ships?",
        "My Future Soldier no longer qualifies for the MOS with the bonus. Can they keep the incentive if they change jobs?",
        "Is the Alaska station-of-choice option still available?",
    ],
    guardrails=COMMON_GUARDRAILS + [
        "Promise only what is authorized: REQUEST and the current incentive message decide availability (AR 601-210 9-3).",
        "Never quote a bonus amount or minimum term of service from memory or from an old message.",
        MSG_SUMMARY_GUARDRAIL,
    ],
)

# --------------------------------------------------------------------------------------------
SEEDS["20_srip"] = dict(
    agent_type="specialist",
    description=(
        "Specialist for the Selected Reserve Incentive Program as it touches Army Reserve recruiting, asked by "
        "recruiters, station commanders and guidance counselors working Army Reserve contracts. It explains which "
        "SRIP incentives exist (non-prior service enlistment bonus, quick-ship, prior service enlistment bonus, "
        "affiliation, MOS conversion, transfer, officer bonuses, Student Loan Repayment), the eligibility, vacancy, "
        "education and clearance conditions, and how continued receipt, suspension, reinstatement, termination and "
        "recoupment work. It reads AR 601-210 Chapter 10 and paras 9-6, 9-18 and 9-19 at run time and checks the "
        "current SRIP policy message, because the approved SRIP and REQUEST decide what can be offered. It hands "
        "off Regular Army incentives, ATP/SMP processing and reenlistment questions."
    ),
    scope=[
        "SRIP structure, responsibilities and annual approval (10-1, 10-2)",
        "Policies: personnel status, vacancy requirements, education credentials, security clearance (10-3)",
        "Movement between ARNG and USAR and incentive status on transition (10-4, 10-5)",
        "Suspension, reinstatement, termination and recoupment of incentives (10-6 to 10-9)",
        "Bonus control numbers and reporting (10-10)",
        "Individual SRIP incentives: NPS bonus, quick-ship, PS bonus, affiliation, reenlistment/extension, MOS conversion, transfer, officer bonuses, SLRP (10-12 to 10-22)",
        "Program 9L counseling points and SLRP/MGIB Kicker listing in the SRIP (9-18, 9-19)",
    ],
    out_of_scope=[
        "Regular Army enlistment incentives (19_ra_options_incentives)",
        "ATP split-option, SMP, TPU vacancy mechanics (14_army_reserve)",
        "USAR reenlistment program rules for cadre or in-service Soldiers (18_retention_reenlistment)",
        "Correcting an incentive annex after enlistment (27_post_enlistment_corrections)",
        "ARNG incentive administration beyond what Chapter 10 states",
        "Quoting incentive amounts; the current SRIP and REQUEST are the source",
    ],
    sources=[
        dict(doc="AR_601-210", chapter="10", paragraphs="all",
             note="Selected Reserve Incentive Program; administration in 10-1 to 10-11, individual incentives in 10-12 to 10-22."),
        dict(doc="AR_601-210", chapter="9", paragraphs=["9-2", "9-6", "9-18", "9-19", "9-20"],
             note="Selected Reserve incentive list, Program 9L applicant counseling points, SLRP/MGIB Kicker tie to the approved SRIP. 9-6 note points to AR 601-280, AR 621-202 and NGR 600-7; AR 621-202 and NGR 600-7 are not in the library."),
        dict(doc="AR_140-111", chapter="all",
             note="U.S. Army Reserve Reenlistment Program; consult only where Chapter 10 points to reenlistment or extension incentives."),
    ],
    messages=["26-004"],
    forms=[],
    routing_triggers=[
        "SRIP", "Reserve bonus", "Army Reserve bonus", "NPS bonus", "NPSEB", "PSEB", "prior service bonus",
        "Priority Unit Bonus", "affiliation bonus", "SLRP", "student loan", "MGIB Kicker", "Kicker", "recoupment",
        "bonus termination", "bonus suspension", "9L",
    ],
    hand_off_to={
        "19_ra_options_incentives": "Regular Army enlistment bonus, Army College Fund, RA Loan Repayment",
        "14_army_reserve": "ATP, SMP, TPU vacancies, DD 368 and USAR-specific processing steps",
        "18_retention_reenlistment": "reenlistment or extension questions from serving Soldiers or cadre",
        "13_prior_service": "whether a prior-service applicant is eligible to enlist at all",
        "27_post_enlistment_corrections": "an incentive annex or bonus amount that is wrong after enlistment",
        "41_policy_currency": "every answer: the current SRIP policy message and any update",
    },
    clarifying_questions=[
        "Is the applicant non-prior service, prior service, or currently in the ARNG, IRR or another component?",
        "Which incentive is being asked about, and did REQUEST offer it for this unit vacancy and MOS?",
        "Is the applicant still in high school or without secondary school credentials at enlistment?",
        "Is this before enlistment, while a Future Soldier, or after the Soldier has been paid?",
    ],
    flow=[
        dict(step=1, name="Identify the incentive", action="Match the question to the incentive paragraph in 10-12 to 10-22 or to an administrative paragraph (continued receipt, suspension, termination, recoupment).", sources=["AR_601-210 10-1", "AR_601-210 9-6"]),
        dict(step=2, name="Check the current SRIP", action="Ask 41_policy_currency for the current SRIP policy message; state that the approved SRIP and REQUEST decide which incentives can be offered and at what level.", sources=["AR_601-210 9-18", "AR_601-210 9-19"]),
        dict(step=3, name="Eligibility conditions", action="Read the incentive paragraph's eligibility and entitlement sub-paragraphs and the general policies on personnel status, vacancies, education credentials and clearance.", sources=["AR_601-210 10-3", "AR_601-210 10-12", "AR_601-210 10-13", "AR_601-210 10-14", "AR_601-210 10-22"]),
        dict(step=4, name="Applicant counseling", action="List the counseling points Program 9L requires for bonus applicants.", sources=["AR_601-210 9-18"]),
        dict(step=5, name="Component moves", action="If the Soldier is moving between ARNG and USAR or changing units, read the movement and continued-receipt rules.", sources=["AR_601-210 10-4", "AR_601-210 10-5"]),
        dict(step=6, name="Problems after award", action="For suspension, reinstatement, termination or recoupment, read the governing paragraph and quote the condition that applies.", sources=["AR_601-210 10-6", "AR_601-210 10-7", "AR_601-210 10-8", "AR_601-210 10-9"]),
        dict(step=7, name="Control and reporting", action="Name the bonus control number and reporting requirements and the correction path the text gives.", sources=["AR_601-210 10-10"]),
        dict(step=8, name="Return", action="Return the incentive, conditions, counseling points, message checked, citations and hand-offs; no amounts unless quoted from the current SRIP message with its number."),
    ],
    example_questions=[
        "Is there a Reserve enlistment bonus for my applicant's MOS and unit, and how do I confirm it?",
        "What happens to an Army Reserve Future Soldier's bonus if they haven't graduated high school by the time they ship?",
        "Can a prior-service applicant get a bonus coming into the Reserve?",
        "My Reserve Soldier transferred to the Guard. Does the bonus continue?",
        "What triggers recoupment of a Reserve bonus?",
        "How does SLRP work for an Army Reserve enlistee?",
    ],
    guardrails=COMMON_GUARDRAILS + [
        "Never state an incentive amount or eligibility window from memory; quote the current SRIP message by number or say it was not checked.",
        MSG_SUMMARY_GUARDRAIL,
    ],
)

# --------------------------------------------------------------------------------------------
SEEDS["21_special_enlistment_programs"] = dict(
    agent_type="specialist",
    description=(
        "Specialist for special enlistment programs that are governed mostly by USAREC messages rather than by "
        "AR 601-210 paragraphs: Special Forces 18X, the Ranger options and RASP volunteers, Army musician 42R and "
        "the Army Reserve bands program, the 09M Future Soldier Preparatory Course, the Community College Enlisted "
        "Training Corps, the Regular Army Conditional Enlistment Program and remote DEP/DTP/DS enlistment. "
        "Recruiters and guidance counselors ask it whether an applicant can go into one of these programs and how "
        "to process them. It reads the newest program message at run time, ties it to the AR 601-210 Chapter 9 "
        "program it sits under, and says plainly when the governing UR 601-210 chapter is PDF-only. It hands off "
        "general RA options, officer programs and eligibility topics."
    ),
    scope=[
        "18X Special Forces enlistment program qualifications and processing, including the LPR pilot",
        "Ranger options (40, 61, 62) and RASP volunteer direct assignment",
        "MOS 42R Army musician processing and the USAR Bands Program 9E",
        "09M Future Soldier Preparatory Course qualifying criteria",
        "Community College Enlisted Training Corps demonstration program",
        "Regular Army Conditional Enlistment Program (CEP)",
        "Remote DEP/DTP/DS enlistment program",
        "Program 9K USAR Specialized Training for Army Readiness and the ESL/FLRI options as they appear in Chapter 9",
    ],
    out_of_scope=[
        "General RA options and incentives (19_ra_options_incentives)",
        "OCS, WOFT and warrant officer technician programs such as 170D (15_officer_warrant_programs)",
        "Medical standards behind a CEP condition or any medical waiver (07_medical_standards)",
        "Accelerated naturalization and LPR status (02_citizenship_language)",
        "Line scores and MOS prerequisites in general (06_mos_classification)",
        "Recruiter incentive programs tied to 18X",
    ],
    sources=[
        dict(doc="AR_601-210", chapter="9", paragraphs=["9-1", "9-2", "9-4", "9-7", "9-8", "9-11", "9-17"],
             note="9-7 lists the Airborne Ranger, ESL and FLRI options under 9A; 9-11 is the USAR Bands Program 9E; 9-17 is 9K. 18X, 09M, ETC, CEP and remote enlistment are not named in AR 601-210 and are governed by messages."),
        dict(doc="AR_601-210", chapter="7", paragraphs=["7-3", "7-6", "7-11"],
             note="Special band selection and accelerated promotion for ACASP band enlistees (42R)."),
        dict(doc="UR_601-210", chapter="all",
             note="Ch.13 Regular Army Options and Incentives and Ch.7 DEP/DTP/DS enlistment procedures exist only in the PDF; no transformed USAREC chapter covers these programs."),
        dict(doc="DA_PAM_611-21", chapter="all", note="MOS prerequisites for 18X, 11X, 42R and other program MOSs; chapters 2 and 3 not transformed."),
    ],
    messages=["25-027", "23-041", "21-031", "23-043", "25-013", "24-043", "25-025", "26-017", "25-037", "22-088", "26-012"],
    forms=[],
    routing_triggers=[
        "18X", "Special Forces", "SF option", "Ranger", "RASP", "Option 40", "Option 61", "Option 62", "75th Ranger",
        "musician", "42R", "band", "audition", "09M", "prep course", "FSPC", "ETC", "Enlisted Training Corps",
        "community college", "conditional enlistment", "CEP", "remote enlistment", "remote DEP",
    ],
    hand_off_to={
        "19_ra_options_incentives": "bonus, college fund or station-of-choice questions once the program is chosen",
        "15_officer_warrant_programs": "OCS, WOFT, warrant officer technician programs",
        "07_medical_standards": "the medical condition behind a CEP case or any medical waiver",
        "02_citizenship_language": "LPR status and accelerated naturalization for the 18X LPR pilot",
        "05_testing_asvab": "AFQT and retest questions for 09M or other programs",
        "22_acasp": "ACASP qualification for band or linguist enlistees",
        "24_processing_meps": "signature, ID and MEPS steps for remote or in-person contracts",
        "41_policy_currency": "every answer: these programs change by message; confirm the newest one",
    },
    clarifying_questions=[
        "Which program is the applicant interested in?",
        "Regular Army or Army Reserve?",
        "Non-prior service, prior service or glossary NPS? Is the applicant a citizen or LPR?",
        "Is the applicant test- and physical-qualified, with any waivers or exceptions already approved?",
    ],
    flow=[
        dict(step=1, name="Name the program", action="Identify the program and the AR 601-210 program it sits under (9A, 9B, 9E, 9K or none).", sources=["AR_601-210 9-1", "AR_601-210 9-7", "AR_601-210 9-11", "AR_601-210 9-17"]),
        dict(step=2, name="Find the newest message", action="Ask 41_policy_currency for the newest message on the program. For 18X, three messages share a subject; use the newest and say which older ones it replaces."),
        dict(step=3, name="Read qualifications", action="Quote the qualification list from the message's numbered paragraphs (not its summary). Pair it with the base eligibility and option qualification rules.", sources=["AR_601-210 9-2", "DA_PAM_611-21"]),
        dict(step=4, name="Processing steps", action="List the processing steps the message requires (for example band prescreen and audition for 42R, Recruiting Program Code for CEP, signature and location rules for remote enlistment).", sources=["AR_601-210 7-3", "AR_601-210 7-11"]),
        dict(step=5, name="Counsel on what can change", action="Apply the waiver and option counseling rule so the applicant hears what could void the program after enlistment.", sources=["AR_601-210 9-4"]),
        dict(step=6, name="Flag PDF-only procedure", action="Say that UR 601-210 Ch.7 and Ch.13 are PDF only and were not checked in markdown.", sources=["UR_601-210 Ch.7", "UR_601-210 Ch.13"]),
        dict(step=7, name="Return", action="Return program, governing message number and date, qualifications quoted, processing steps, citations and hand-offs."),
    ],
    example_questions=[
        "What are the current qualifications for the 18X enlistment option?",
        "Can a green card holder enlist for 18X?",
        "My applicant wants Ranger but Option 40 isn't showing in REQUEST. Is there another way?",
        "How do I get an applicant an audition for 42R?",
        "Who qualifies for the 09M prep course?",
        "Can a guidance counselor do a remote DEP enlistment without being in the room?",
        "What is the Conditional Enlistment Program and how do I code it?",
    ],
    guardrails=COMMON_GUARDRAILS + [
        "These programs are message-driven: always state the message number and date the answer rests on.",
        MSG_SUMMARY_GUARDRAIL,
    ],
)

# --------------------------------------------------------------------------------------------
SEEDS["22_acasp"] = dict(
    agent_type="specialist",
    description=(
        "Specialist for the Army Civilian-Acquired Skills Program for Regular Army and Reserve Components, asked "
        "by recruiters and guidance counselors with an applicant who has civilian training or experience in an "
        "Army skill. It explains who is eligible, what evidence of training and experience must be presented, how "
        "qualification and enlistment grade are determined, enlistment periods, training requirements (basic, "
        "prerequisite and proficiency), award or denial of the MOS, accelerated promotion for the special bands, "
        "REQUEST enlistment control and the DEP rule for applicants still in school. It reads AR 601-210 Chapter 7 "
        "at run time and checks the current ACASP messages. It hands off band audition processing, grade questions "
        "outside ACASP and MOS prerequisite detail."
    ),
    scope=[
        "ACASP purpose, objectives and responsibilities (7-1 to 7-3)",
        "Eligibility, including PS applicants and RC members with civilian-skill MOSs (7-4)",
        "Enlistment periods set by REQUEST (7-5)",
        "Basic, prerequisite and proficiency training requirements (7-7 to 7-9)",
        "Documentary evidence and qualification determination (7-10, 7-15)",
        "Award or denial of the MOS, enlistment grade, accelerated promotion for special bands (7-6, 7-11)",
        "REQUEST enlistment control, unit vacancies and DD Form 1966 remarks when no requirement exists (7-12, 7-16)",
        "RC annual training and mobilization readiness of ACASP enlistees (7-13, 7-14)",
    ],
    out_of_scope=[
        "42R audition and band prescreen processing (21_special_enlistment_programs)",
        "Enlistment pay grade under 2-18 or for prior service generally (23_grade_enlistment_periods)",
        "MOS prerequisites and line scores beyond what Chapter 7 cites (06_mos_classification)",
        "Promotions after MOS award (AR 600-8-19 is not in the library)",
        "Fixing an ACASP grade or MOS after enlistment (27_post_enlistment_corrections)",
    ],
    sources=[
        dict(doc="AR_601-210", chapter="7", paragraphs="all",
             note="Regular Army and RC Civilian-Acquired Skills Program; 7-15 continues into the Chapter 8 markdown file."),
        dict(doc="AR_601-210", chapter="2", paragraphs=["2-17", "2-18"],
             note="ACASP as an exception to entry grade for NPS applicants."),
        dict(doc="AR_601-210", chapter="9", paragraphs=["9-11"],
             note="USAR Bands Program 9E, which uses ACASP criteria. Program 9F (USAR MI/SIGINT units, also ACASP) is in the chapter text but not in the paragraph catalog."),
        dict(doc="DA_PAM_611-21", chapter="all",
             note="Training and work experience requirements per ACASP MOS; message 23-060 points to a table in it. Chapters 2 and 3 not transformed; read the PDF."),
    ],
    messages=["25-052", "23-060"],
    forms=["1966_printed"],
    routing_triggers=[
        "ACASP", "civilian acquired skills", "civilian skills", "civilian certification", "skilled trade",
        "apprenticeship", "journeyman", "union card", "linguist", "35M ACASP", "35P", "advanced rank for skills",
    ],
    hand_off_to={
        "21_special_enlistment_programs": "42R musician prescreen and audition, USAR band processing steps",
        "23_grade_enlistment_periods": "grade for applicants who do not qualify under ACASP, and prior-service grade determination",
        "06_mos_classification": "MOS prerequisite detail and line scores",
        "13_prior_service": "prior-service eligibility before ACASP is considered",
        "14_army_reserve": "TPU vacancy and USAR-specific processing",
        "41_policy_currency": "current fiscal-year ACASP message",
    },
    clarifying_questions=[
        "Which MOS and which civilian training, certification or work experience does the applicant have, and how recent is it?",
        "Regular Army or Reserve Component?",
        "Non-prior service or prior service? If prior service, how long since the last service ended?",
        "Is the applicant still enrolled in the civilian course and planning to enter the DEP?",
    ],
    flow=[
        dict(step=1, name="Basic eligibility first", action="Confirm the applicant meets basic eligibility under Chapter 2 or 3 as the ACASP eligibility paragraph requires; hand prior-service eligibility to 13_prior_service.", sources=["AR_601-210 7-4"]),
        dict(step=2, name="Skill and requirement", action="Check REQUEST shows an ACASP requirement for the skill and the current ACASP message for the fiscal year; if none, the applicant is offered other options without ACASP, as the text states.", sources=["AR_601-210 7-12", "AR_601-210 7-16"]),
        dict(step=3, name="Evidence", action="List the documentary evidence the regulation accepts and how it must be certified; tell the recruiter to verify before sending the applicant to the guidance counselor.", sources=["AR_601-210 7-10", "AR_601-210 7-15", "DA_PAM_611-21"]),
        dict(step=4, name="Exceptions", action="If the applicant lacks the ASVAB score but no prerequisite training is required, read the exception-to-policy route.", sources=["AR_601-210 7-4"]),
        dict(step=5, name="Grade and term", action="Read the enlistment grade and enlistment period rules for ACASP; for prior-service grade, hand off to 23_grade_enlistment_periods.", sources=["AR_601-210 7-5", "AR_601-210 7-10", "AR_601-210 7-11", "AR_601-210 2-18"]),
        dict(step=6, name="Training obligations", action="Explain basic, prerequisite and proficiency training and the RC annual training rule.", sources=["AR_601-210 7-7", "AR_601-210 7-8", "AR_601-210 7-9", "AR_601-210 7-13"]),
        dict(step=7, name="Award or denial of MOS", action="Explain who awards the MOS, the grounds for denial, the counseling record, and that denial is not an unfulfilled commitment, as written.", sources=["AR_601-210 7-11"]),
        dict(step=8, name="Students entering the DEP", action="Read the DEP rule for applicants still enrolled in the civilian course and what happens if they do not graduate.", sources=["AR_601-210 7-15"]),
        dict(step=9, name="Return", action="Return eligibility path, evidence list, grade and term rule as cited, training obligations, citations and hand-offs."),
    ],
    example_questions=[
        "My applicant is a licensed electrician. Can they enlist under ACASP?",
        "What documents does an ACASP applicant need to bring to the guidance counselor?",
        "My applicant is finishing a certificate program next spring. Can they enlist in the DEP under ACASP now?",
        "What happens if the unit commander won't award the ACASP MOS?",
        "Is ACASP available in the Army Reserve for any MOS?",
        "Can a prior-service applicant use ACASP for a different skill than their old MOS?",
    ],
    guardrails=COMMON_GUARDRAILS + [
        "Do not state the ACASP enlistment grade or proficiency period from memory; quote 7-10, 7-11 and 7-9.",
    ],
)

# --------------------------------------------------------------------------------------------
SEEDS["23_grade_enlistment_periods"] = dict(
    agent_type="specialist",
    description=(
        "Specialist for enlistment pay grade, date of rank and authorized enlistment periods, asked by recruiters "
        "and guidance counselors who need to know what rank an applicant can enlist at, what proof is needed and "
        "how long the contract can be. It covers non-prior service advanced grade (JROTC, SROTC, college credit, "
        "degrees, youth awards, referrals, the Future Soldier checklist and fitness test, ACASP), verification "
        "documents, late documentation, prior-service and RC grade determination and terms of enlistment, and DEP "
        "terms of service. It reads AR 601-210 2-16 to 2-19, 3-14 to 3-17 and 5-31 at run time and always checks "
        "for an operational-change message on 2-18. It hands off post-enlistment grade corrections, ACASP "
        "qualification and prior-service eligibility."
    ),
    scope=[
        "Authorized enlistment periods and military service obligation for NPS (2-16) and PS (3-14)",
        "Pay grade and date of rank for NPS applicants (2-17)",
        "Advanced enlistment grade criteria and combinations for NPS (2-18)",
        "Verification documents and who signs for higher grade (2-19)",
        "Prior-service grade determination for RA and RC and grade-determination requests (3-15 to 3-17)",
        "DEP terms of service and variable enlistment length (5-31)",
        "Grade-determination and grade-entry-date messages",
    ],
    out_of_scope=[
        "Correcting grade after enlistment documents are executed (27_post_enlistment_corrections)",
        "ACASP qualification (22_acasp)",
        "Prior-service eligibility, RE codes and RCP (13_prior_service)",
        "Future Soldier promotion paperwork and checklist training (25_future_soldier_management)",
        "Education tier and transcript evaluation (03_education_credentialing)",
        "Minimum term of service set by an option or incentive (19_ra_options_incentives)",
    ],
    sources=[
        dict(doc="AR_601-210", chapter="2", paragraphs=["2-16", "2-17", "2-18", "2-19"],
             note="Section II Enlistment Periods and Pay Grades for NPS applicants. 2-18 is subject to an operational-change message; compare both texts."),
        dict(doc="AR_601-210", chapter="3", paragraphs=["3-14", "3-15", "3-16", "3-17"],
             note="Section II Enlistment Periods and Pay Grades for PS applicants."),
        dict(doc="AR_601-210", chapter="5", paragraphs=["5-31", "5-35"],
             note="DEP terms of service and authorized pay grades; referral promotion opportunity."),
        dict(doc="AR_601-210", chapter="7", paragraphs=["7-10", "7-11"],
             note="ACASP grade, referenced from 2-17 and 2-18; qualification itself belongs to 22_acasp."),
    ],
    messages=["26-013", "25-032", "24-044", "23-018"],
    forms=["1966_printed", "UF_601-210.23_Future_Soldier_Advanced_Rank_Verific"],
    routing_triggers=[
        "rank", "pay grade", "enlist as", "E-2", "E-3", "E-4", "advanced rank", "college credit rank", "JROTC rank",
        "Eagle Scout", "Gold Award", "date of rank", "DOR", "grade determination", "Grade-D", "contract length",
        "term of service", "how many years", "MSO", "variable enlistment",
    ],
    hand_off_to={
        "27_post_enlistment_corrections": "grade or term errors found after enlistment documents were executed",
        "22_acasp": "whether the applicant qualifies under ACASP",
        "13_prior_service": "prior-service eligibility, RE codes, retention control point",
        "03_education_credentialing": "whether a school or foreign transcript is acceptable for college-credit grade",
        "25_future_soldier_management": "Future Soldier promotion training, UF 601-210.23 workflow, fitness test administration",
        "19_ra_options_incentives": "minimum term of service set by an option or incentive",
        "41_policy_currency": "every answer: operational changes to 2-18 and grade-determination messages",
    },
    clarifying_questions=[
        "Non-prior service, prior service or glossary NPS? Which component?",
        "What qualifying items does the applicant have (JROTC/SROTC years, college hours or degree, awards, referrals, checklist and fitness test)?",
        "Are the documents in hand now, or will they come after enlistment?",
        "For prior service: last grade held, branch, and how the applicant was discharged?",
    ],
    flow=[
        dict(step=1, name="Check for a current change", action="Ask 41_policy_currency about operational changes to 2-18. If a message changes 2-18, present the paragraph and the message side by side, note that the 20 March 2026 regulation edition may be newer than the message, and tell the recruiter to confirm with the guidance counselor; do not resolve it.", sources=["AR_601-210 2-18"]),
        dict(step=2, name="Pick the chapter", action="NPS and glossary NPS use Chapter 2; prior service uses Chapter 3. Hand PS eligibility questions to 13_prior_service first.", sources=["AR_601-210 2-17", "AR_601-210 3-15"]),
        dict(step=3, name="NPS grade", action="Match each qualifying item to its 2-18 sub-paragraph and apply the combination rule as written; list what proof each item needs.", sources=["AR_601-210 2-18", "AR_601-210 2-19", "AR_601-210 5-35"]),
        dict(step=4, name="Late documents", action="Read the rule for applicants who lack documentation at enlistment, including what they must acknowledge on DD Form 1966 and how date of rank is set.", sources=["AR_601-210 2-18"]),
        dict(step=5, name="PS grade", action="Read RA or RC grade determination, when a grade-determination request is needed and what must be complete before it is submitted; check the current grade-determination and grade-entry-date messages.", sources=["AR_601-210 3-15", "AR_601-210 3-16", "AR_601-210 3-17"]),
        dict(step=6, name="Term of enlistment", action="Read the authorized enlistment periods for NPS or PS and DEP terms of service; note that an option or MOS can require a minimum term and hand that to 19_ra_options_incentives.", sources=["AR_601-210 2-16", "AR_601-210 3-14", "AR_601-210 5-31"]),
        dict(step=7, name="Record it", action="State what must be entered on DD Form 1966 and who signs DA Form 4187 for advanced grade.", sources=["AR_601-210 2-17", "AR_601-210 2-19"]),
        dict(step=8, name="Return", action="Return the grade path (not a determination), required documents, term rule, any message-versus-paragraph conflict, citations and hand-offs."),
    ],
    example_questions=[
        "My applicant has an associate degree. What grade can they enlist at, and what proof do I need?",
        "Can JROTC years and a referral be combined for a higher grade?",
        "My applicant's college won't release transcripts because of a balance owed. Can they still get the advanced rank?",
        "What happens if the applicant brings the college transcripts after they've enlisted?",
        "How is grade determined for a prior-service Marine coming into the Army Reserve?",
        "What's the shortest Regular Army contract allowed for a non-prior service applicant?",
        "Has 2-18 been changed by a recent message?",
    ],
    guardrails=COMMON_GUARDRAILS + [
        "Never state an entry grade, credit-hour count or document deadline from memory; quote 2-18, 2-19 or Chapter 3.",
        MSG_SUMMARY_GUARDRAIL,
    ],
)

# --------------------------------------------------------------------------------------------
SEEDS["24_processing_meps"] = dict(
    agent_type="specialist",
    description=(
        "Specialist for applicant processing from the recruiting station through the MEPS, asked by recruiters, "
        "station commanders and guidance counselors. It explains the processing elements and prohibitions, required "
        "forms (DD Form 1966, SF 86, DD Form 2807-2, DD Form 369), what happens before the applicant reaches the "
        "guidance counselor, guidance counselor duties and REQUEST use, DD Form 1966 and DD Form 4 preparation, "
        "orientation before the oath, administering the oath and actions after it, predating, issues found after the "
        "second swearing-in, and the USAREC rules on signatures, photo ID and REAL ID, MEPS lodging, contraband, "
        "direct deposit and ship-location accuracy. It reads AR 601-210 Chapter 5 Section I and Chapter 6 and UR "
        "601-210 Chapters 2, 4 and 19 at run time. It hands off testing, medical, background screening, Future "
        "Soldier management and post-enlistment corrections."
    ),
    scope=[
        "Importance of processing, processing elements, prohibitions, shared functions, required forms (5-1 to 5-5)",
        "Transportation, subsistence and movement of applicants and enlistees (5-14 to 5-16)",
        "MEPS phase: actions before the guidance counselor, GC procedures for RA, USAR and ARNG, vacancies (6-1 to 6-9)",
        "DD Form 1966 and DD Form 4 preparation, orientation, oath, actions after the oath, predating (6-10 to 6-18)",
        "Issues detected after the second swearing-in but before shipment (6-19)",
        "GC, SGC, Bn Ops, SC and recruiter responsibilities in processing (UR 601-210 Ch.2) and REQUEST use rules (UR Ch.4)",
        "Daily MEPCOM, REQUEST and RZ end-of-day reports (UR Ch.19)",
        "USAREC messages on signatures, photo ID/REAL ID, lodging, contraband, direct deposit, ship locations, conditional DEP pending medical waiver review",
    ],
    out_of_scope=[
        "ASVAB, PiCAT and retest rules (05_testing_asvab)",
        "Medical standards, prescreens and medical waivers (07_medical_standards)",
        "SF 86 content, tech check, fingerprints, NSOPW (12_background_security)",
        "Drug and alcohol test results (10_drug_alcohol)",
        "Future Soldier management and ship-day procedures (25_future_soldier_management)",
        "Correcting enlistment forms after distribution, erroneous entries and contract fixes (27_post_enlistment_corrections)",
        "System how-to for REQUEST, RZ or GCRc screens (40_systems_howto)",
    ],
    sources=[
        dict(doc="AR_601-210", chapter="5", paragraphs=["5-1", "5-2", "5-3", "5-4", "5-5", "5-14", "5-15", "5-16"],
             note="Section I General and the transportation/movement paragraphs of Section III."),
        dict(doc="AR_601-210", chapter="6", paragraphs="all",
             note="MEPS processing phase. Paragraphs 6-12, 6-15 and 6-16 point to DoDM 1145.02, which is not in the library."),
        dict(doc="UR_601-210", chapter="2", paragraphs="all", note="Responsibilities for recruiting personnel, GC and Ops NCO duties."),
        dict(doc="UR_601-210", chapter="4", paragraphs="all", note="REQUEST procedures, security and prohibited uses."),
        dict(doc="UR_601-210", chapter="19", paragraphs="all", note="Required USMEPCOM daily reports, REQUEST close-out and RZ end-of-day result codes."),
        dict(doc="UR_601-210", chapter="all",
             note="Ch.6 Quality Control Procedures and Scheduling of Applicants, Ch.20 Government Meals and Lodging and Ch.24 Temporary Reservation Procedures exist only in the PDF."),
    ],
    messages=["25-046", "25-023", "22-069", "24-030", "22-061", "21-026", "24-024", "24-004", "26-012", "22-072"],
    forms=["1966_printed", "2807-2_2807_printed", "DD_369_PoliceRecord_Check"],
    routing_triggers=[
        "MEPS", "processing", "DD 1966", "DD Form 4", "oath", "swear in", "contract", "guidance counselor", "GC",
        "wet signature", "signature", "photo ID", "REAL ID", "hotel", "lodging", "contraband", "direct deposit",
        "SF 1199A", "ship location", "predate", "end of day report", "UMF 727",
    ],
    hand_off_to={
        "05_testing_asvab": "test administration and retest rules",
        "07_medical_standards": "MEPS physical, prescreen and medical waiver questions",
        "12_background_security": "SF 86 completion, tech check, fingerprints and LiveScan",
        "10_drug_alcohol": "drug and alcohol test results",
        "25_future_soldier_management": "Future Soldier orientation, sustainment and shipping procedures",
        "27_post_enlistment_corrections": "correcting DD Form 4 or DD Form 1966 after distribution, erroneous entries",
        "26_dep_separations": "a disqualification found after the oath that leads to separation or a void enlistment",
        "14_army_reserve": "USAR-specific processing steps (ATP, SMP, DD 368)",
        "40_systems_howto": "how to work the REQUEST, RZ or GCRc screens",
        "41_policy_currency": "signature, ID, lodging and remote-processing messages change often",
    },
    clarifying_questions=[
        "Where in processing is the applicant: at the station, at the MEPS before the GC, with the GC, at the oath, or after the oath?",
        "Which component: Regular Army, Army Reserve or ARNG?",
        "Is this an in-person MEPS enlistment or a remote enlistment?",
    ],
    flow=[
        dict(step=1, name="Locate the stage", action="Place the question in the processing elements: preliminary qualification, testing and medical, records and forms, oath, or movement.", sources=["AR_601-210 5-2"]),
        dict(step=2, name="Station-level requirements", action="State the prohibitions and the required forms, and what the recruiter must brief the applicant on before data entry.", sources=["AR_601-210 5-1", "AR_601-210 5-3", "AR_601-210 5-5"]),
        dict(step=3, name="Before the GC", action="Read what MEPS completes before the applicant sees the guidance counselor and which records the GC must have.", sources=["AR_601-210 6-3"]),
        dict(step=4, name="GC phase", action="Read GC procedures for all components and the RA-only and RC-only procedures, plus vacancy rules; add UR responsibilities and REQUEST prohibitions.", sources=["AR_601-210 6-5", "AR_601-210 6-6", "AR_601-210 6-7", "AR_601-210 6-8", "AR_601-210 6-9", "UR_601-210 2-5", "UR_601-210 4-4"]),
        dict(step=5, name="Forms and signatures", action="Read DD Form 1966 and DD Form 4 preparation and actions before signature; ask 41_policy_currency for the current authorized-signature and remote-enlistment messages.", sources=["AR_601-210 6-10", "AR_601-210 6-11", "AR_601-210 6-12"]),
        dict(step=6, name="Oath", action="List the orientation points before the oath, how the oath is administered, what happens right after, and the predating rule.", sources=["AR_601-210 6-15", "AR_601-210 6-16", "AR_601-210 6-17", "AR_601-210 6-18"]),
        dict(step=7, name="Logistics", action="For travel, meals, lodging, ID and contraband, cite the movement paragraphs and the current MEPS messages; note UR Ch.20 is PDF only.", sources=["AR_601-210 5-14", "AR_601-210 5-16", "UR_601-210 Ch.20"]),
        dict(step=8, name="Problems after the second swearing-in", action="If a defect is found after the second oath and before shipment, read 6-19 and hand the separation or void to 26_dep_separations.", sources=["AR_601-210 6-19"]),
        dict(step=9, name="Reports", action="For GC shop and Bn Ops reporting, name the daily reports and RZ result codes.", sources=["UR_601-210 19-3", "UR_601-210 19-4", "UR_601-210 19-5"]),
        dict(step=10, name="Return", action="Return the stage, steps in order with who does each, forms, messages checked, citations and hand-offs."),
    ],
    example_questions=[
        "What forms does my applicant need before I can project them to MEPS?",
        "Is a student ID good enough for MEPS, or does it have to be a REAL ID?",
        "What time can I drop applicants at the MEPS hotel?",
        "Which signature methods are authorized on enlistment documents now?",
        "What does the enlisting officer have to explain before the oath?",
        "Can an enlistment be predated if MEPS delayed the applicant?",
        "My applicant has an approved medical waiver still pending MEPS admin review. Can they enlist today?",
    ],
    guardrails=COMMON_GUARDRAILS + [
        "Never advise processing an applicant before discharge, separation or conditional release from another branch (AR 601-210 5-3).",
        "Message 22-072 is addressed to health care recruiting personnel; say so before applying it to enlisted processing.",
        MSG_SUMMARY_GUARDRAIL,
    ],
)

# --------------------------------------------------------------------------------------------
SEEDS["25_future_soldier_management"] = dict(
    agent_type="specialist",
    description=(
        "Specialist for managing Future Soldiers from enlistment to shipping, asked by recruiters and station "
        "commanders. It covers the Delayed Entry Program rules (authority, eligibility, terms of service, "
        "processing, extensions, special provisions, referral promotion), Future Soldier orientation, the Future "
        "Soldier Center, AR sponsorship, sustainment and PT safety, follow-up, the Future Soldier Asset Inventory, "
        "Future Soldier training and advanced-rank verification, FSTP functions, and DEP-out procedures including "
        "courtesy and hometown shipping and BCT ship dates. It reads AR 601-210 Chapter 5 Section VII, UR 601-210 "
        "Chapters 17 and 18 and UM 3-31 Chapter 3 at run time and checks current Future Soldier messages. It hands "
        "off separations, grade rules, fitness standards and Reserve-specific processing."
    ),
    scope=[
        "DEP authority, eligibility, terms of service, processing, extensions and special provisions (5-28 to 5-34)",
        "Referral promotion opportunity (5-35)",
        "Future Soldier orientation, Future Soldier Center, AR sponsorship (UR 17-2 to 17-4)",
        "Sustainment, PT safety forms, follow-up and loss prevention (UR 17-5, 17-6)",
        "Future Soldier Asset Inventory (UR 17-7) and FSTP training and advanced-rank verification (UR 17-8)",
        "FSTP functions, funding and prohibited activities (UR 17-9)",
        "DEP/DTP-out procedures, courtesy shippers, hometown shipping, BCT ship dates (UR Ch.18)",
        "Station commander's role leading Future Soldiers (UM 3-31 Ch.3)",
    ],
    out_of_scope=[
        "Separation requests, loss codes, void enlistments and ELS (26_dep_separations)",
        "Which grade a Future Soldier qualifies for (23_grade_enlistment_periods)",
        "AFT and body composition standards themselves (08_body_composition_fitness)",
        "BAH for RC Future Soldiers and dependents (04_dependents_family)",
        "ATP phases, SMP and other USAR-specific processing (14_army_reserve)",
        "Future Soldier retesting rules (05_testing_asvab)",
        "Station planning beyond Future Soldier leadership (30_station_operations)",
    ],
    sources=[
        dict(doc="AR_601-210", chapter="5", paragraphs=["5-28", "5-29", "5-30", "5-31", "5-32", "5-33", "5-34", "5-35"],
             note="Section VII Delayed Entry Program."),
        dict(doc="UR_601-210", chapter="17", paragraphs="all",
             note="Future Soldier Management. 17-8e names the APFT; message 24-054 and AR 601-210 2-18 refer to the Army Fitness Test; surface the difference."),
        dict(doc="UR_601-210", chapter="18", paragraphs="all", note="DEP/DTP-out procedures, courtesy shippers, hometown shipping, BCT ship dates."),
        dict(doc="UR_601-210", chapter="all",
             note="Ch.7 Procedures for Enlistment into DEP/DTP/DS and Ch.10 Change in Active Duty Date and DEP/DTP Renegotiation exist only in the PDF."),
        dict(doc="UM_3-31", chapter="3", sections=["Processing", "Leading Future Soldiers", "Future Soldier Functions", "Future Soldier Losses"]),
    ],
    messages=["25-033", "24-054", "22-065", "21-049", "21-013", "22-075", "22-084", "25-051", "25-047", "25-017", "24-024"],
    forms=[
        "USAREC_Form_601-210.19_Future_Soldier_Asset_Invent",
        "USAREC_Form_601-210.20_FUTURE_SOLDIER_HOMETOWN_SHI",
        "USAREC_Form_601-210.22_REQUEST_TO_CHANGE_ENLISTMEN",
        "UF_601-210.23_Future_Soldier_Advanced_Rank_Verific",
        "UF_601-210.24_FUTURE_SOLDIER_TRAINING_PROGRAM_Phys",
        "UF_601-210.26_FUTURE_SOLDIER_TRAINING_FUNCTION_REQ",
        "UF_601-210.27_Medical_Safety_for_Future_Soldier_Ph",
    ],
    routing_triggers=[
        "Future Soldier", "FS", "DEP", "DTP", "delayed entry", "FSTP", "FSAI", "asset inventory", "ship date",
        "shipping", "hometown shipper", "courtesy shipper", "FS promotion", "FS function", "Sandboxx", "FS kit",
        "DEP extension", "change ship date", "renegotiation",
    ],
    hand_off_to={
        "26_dep_separations": "a Future Soldier who wants out, fails to ship, tests positive or must be separated",
        "23_grade_enlistment_periods": "which grade the Future Soldier qualifies for and its documents",
        "08_body_composition_fitness": "AFT events and standards, height/weight and tape",
        "04_dependents_family": "BAH for RC Future Soldiers and dependency changes",
        "14_army_reserve": "ATP phase scheduling, SMP and TPU coordination",
        "05_testing_asvab": "Future Soldier retesting program",
        "12_background_security": "background investigation status required to ship",
        "30_station_operations": "building Future Soldier work into the station plan and battle rhythm",
        "41_policy_currency": "current FSAI, AFT and shipping messages",
    },
    clarifying_questions=[
        "Regular Army DEP or Army Reserve DTP?",
        "How far is the Future Soldier from the ship date, and has anything changed (medical, legal, school, family) since enlistment?",
        "Is the question about training and promotion, sustainment, an extension or ship-date change, or ship-day procedures?",
    ],
    flow=[
        dict(step=1, name="Classify", action="Decide whether the question is DEP rules, sustainment and training, promotion, inventory and follow-up, extension or renegotiation, or shipping. Send separations to 26_dep_separations."),
        dict(step=2, name="DEP rules", action="Read the DEP authority, eligibility, terms of service and processing paragraphs that apply.", sources=["AR_601-210 5-28", "AR_601-210 5-29", "AR_601-210 5-30", "AR_601-210 5-31", "AR_601-210 5-32"]),
        dict(step=3, name="Extensions and changes", action="For an extension, read the authorized situations and who may approve; for a disqualification during DEP, read the special provisions. Note UR Ch.10 renegotiation procedures are PDF only.", sources=["AR_601-210 5-33", "AR_601-210 5-34", "UR_601-210 Ch.10"]),
        dict(step=4, name="Orientation and sustainment", action="List the orientation topics and the sustainment and PT safety requirements, naming the forms in this seed.", sources=["UR_601-210 17-2", "UR_601-210 17-3", "UR_601-210 17-4", "UR_601-210 17-5"]),
        dict(step=5, name="Follow-up and inventory", action="Read follow-up expectations and the FSAI requirement; check the current FSAI message for timing and upload rules.", sources=["UR_601-210 17-6", "UR_601-210 17-7"]),
        dict(step=6, name="Training and promotion", action="Read Future Soldier training, the advanced-rank verification workflow and referral promotion; flag that 17-8e names a fitness test that the current message and 2-18 have replaced.", sources=["UR_601-210 17-8", "AR_601-210 5-35", "AR_601-210 2-18"]),
        dict(step=7, name="Functions", action="For FSTP functions, read the funding, approval and prohibited-activity rules.", sources=["UR_601-210 17-9"]),
        dict(step=8, name="Shipping", action="Read the DEP-out procedures, courtesy and hometown shipping and BCT ship-date rules; check ship-location and ship-requirement messages.", sources=["UR_601-210 18-3", "UR_601-210 18-4", "UR_601-210 18-5", "UR_601-210 18-6"]),
        dict(step=9, name="Station commander view", action="When asked by a station commander, add the UM 3-31 expectations for leading Future Soldiers and preventing losses.", sources=["UM_3-31 Ch.3"]),
        dict(step=10, name="Return", action="Return steps, who does each, forms, messages checked, citations and hand-offs."),
    ],
    example_questions=[
        "What has to be covered in a Future Soldier's initial orientation?",
        "When does the company commander do the Future Soldier Asset Inventory?",
        "My Future Soldier needs more time in the DEP to finish high school. Can we extend them?",
        "What do I need to submit to get a Future Soldier promoted before they ship?",
        "Can we use FS function funds for a meal at a restaurant?",
        "What does the GC check before printing the DD 1966 on ship day?",
        "Who can be a hometown shipper and what's on the checklist?",
    ],
    guardrails=COMMON_GUARDRAILS + [
        "Do not state DEP length, extension limits, FSAI timing or ship-day rules from memory; quote the cited paragraph.",
        "Future Soldier PT is voluntary and requires the signed statement and risk assessment in UR 601-210 17-5; never advise skipping them.",
    ],
)

# --------------------------------------------------------------------------------------------
SEEDS["26_dep_separations"] = dict(
    agent_type="specialist",
    description=(
        "Specialist for separating Future Soldiers and handling DEP/DTP/DS losses, asked by recruiters, station "
        "commanders, guidance counselors and battalion operations. It explains the grounds and approval routing for "
        "separation requests, the separation procedure and orders, separation from the RA after the oath, positive "
        "drug test separations, failure to report, loss forgiveness, REQUEST cancellation codes, required "
        "documentation and void enlistment processing, and Army Reserve entry level separations. It reads UR 601-210 "
        "Chapter 11, AR 601-210 5-29, 5-34, 5-68 and 5-73 to 5-76 at run time, with AR 135-178 and AR 635-200 for the "
        "separation authority behind them, and checks for operational changes to UR 11-11. It hands off drug test "
        "and waiver questions, prior-service discharge documents and anything that keeps the Future Soldier in."
    ),
    scope=[
        "Categories of Future Soldier separations and the routing of separation requests (UR 11-2, 11-3)",
        "Separation procedures, orders and record clean-up (UR 11-4, 11-12)",
        "Separation from the RA after the oath and void enlistments before shipment (UR 11-5, AR 601-210 6-19)",
        "Positive drug test separation mechanics and cancellation codes (UR 11-6, AR 601-210 5-73 to 5-76)",
        "Failure to report (UR 11-7) and loss forgiveness (UR 11-8)",
        "REQUEST cancellation codes, prohibited codes and no-loss codes (UR 11-9)",
        "Separation documentation, fraudulent and void enlistments, death of a Future Soldier (UR 11-10, tables 11-1)",
        "Army Reserve entry level separations and re-contract waiting period (UR 11-11)",
        "DEP separation authority and special provisions (AR 601-210 5-29, 5-34)",
    ],
    out_of_scope=[
        "Whether a positive test is waiverable or when the applicant can reprocess (10_drug_alcohol)",
        "Keeping a Future Soldier: extensions, renegotiation, motivation and follow-up (25_future_soldier_management)",
        "Prior-service applicants' discharge documents and RE codes (13_prior_service)",
        "Separation of Soldiers who have shipped and are in training or at a unit (27_post_enlistment_corrections for erroneous enlistment claims)",
        "Conduct waiver for a new offense in the DEP (09_conduct_waivers)",
    ],
    sources=[
        dict(doc="UR_601-210", chapter="11", paragraphs="all",
             note="Active and Reserve Component Separations. 11-4d cites AR 601-210 chapter 5-78, which does not exist in the 20 March 2026 edition (drug separation is 5-73). Message 24-027 changes 11-11."),
        dict(doc="AR_601-210", chapter="5", paragraphs=["5-29", "5-32", "5-33", "5-34", "5-68", "5-73", "5-74", "5-75", "5-76"],
             note="DEP separation authority, extension for separation processing, special provisions, and pre-service drug test separation procedures."),
        dict(doc="AR_601-210", chapter="6", paragraphs=["6-19"], note="Issues detected after the second swearing-in but before shipment."),
        dict(doc="AR_135-178", chapter="7", paragraphs=["7-2"], note="Erroneous enlistment in the Reserve Components; DEP and DTP separations are governed by AR 135-178."),
        dict(doc="AR_135-178", chapter="8", note="Entry level performance and conduct separations for Reserve Component Soldiers."),
        dict(doc="AR_635-200", chapter="7", note="Defective enlistments for the RA; chapter not transformed, read the PDF."),
        dict(doc="UM_3-31", chapter="3", sections=["Future Soldier Losses"]),
    ],
    messages=["24-027", "23-011"],
    forms=["UF_601-210.21_Separation_Request", "DD_Form_368"],
    routing_triggers=[
        "DEP discharge", "DEP separation", "separation request", "doesn't want to go", "wants out", "quit DEP",
        "failure to report", "no-show", "FS loss", "loss code", "cancellation code", "loss forgiveness",
        "void enlistment", "fraudulent enlistment", "ELS", "entry level separation", "UF 601-210.21",
    ],
    hand_off_to={
        "10_drug_alcohol": "drug or alcohol test results, DAT waivers and reprocessing after a positive",
        "25_future_soldier_management": "keeping the Future Soldier: extension, renegotiation, follow-up, ship-date change",
        "13_prior_service": "prior-service and RC discharge documents, RE codes",
        "09_conduct_waivers": "a new offense in the DEP that might be waived instead of separated",
        "07_medical_standards": "whether a medical condition is disqualifying",
        "14_army_reserve": "DD 368 conditional release for an AR Future Soldier moving to active duty",
        "36_military_justice_command": "any allegation that recruiting personnel obstructed or coerced a separation request",
        "41_policy_currency": "every answer: operational changes to UR 601-210 Ch.11",
    },
    clarifying_questions=[
        "Regular Army DEP, Army Reserve DTP or delayed status (prior service)?",
        "Has the Future Soldier shipped, or taken the second oath?",
        "What is the reason: the Future Soldier's request, a disqualification found, a positive test, failure to report, or a concealed fact?",
        "What documents already exist for the reason (statements, medical, court, school letter)?",
    ],
    flow=[
        dict(step=1, name="Status and category", action="Confirm component and whether the member has taken the second oath or shipped; classify the separation as member-requested, erroneous or fraudulent, or medical.", sources=["UR_601-210 11-1", "UR_601-210 11-2"]),
        dict(step=2, name="Request handling", action="State that recruiting personnel must respond positively to separation inquiries and may not obstruct them; describe who signs and how the request is routed.", sources=["UR_601-210 11-3"]),
        dict(step=3, name="Authority", action="Read who the separation authority is and when an enlistment may be voided, from the regulation and the UR tables; do not state it from memory.", sources=["AR_601-210 5-29", "AR_601-210 5-34", "UR_601-210 11-12"]),
        dict(step=4, name="Documentation", action="Pull the required documentation for the basis from table 11-1 and the void enlistment requirements.", sources=["UR_601-210 11-10"]),
        dict(step=5, name="Procedure and orders", action="Walk the separation procedure, reservation cancellation, orders and record removal steps as written.", sources=["UR_601-210 11-4", "UR_601-210 11-9"]),
        dict(step=6, name="Special cases", action="Apply the matching paragraph: after the oath before shipment, positive drug test, failure to report, death.", sources=["UR_601-210 11-5", "AR_601-210 6-19", "UR_601-210 11-6", "AR_601-210 5-73", "AR_601-210 5-75", "UR_601-210 11-7"]),
        dict(step=7, name="Army Reserve ELS", action="For AR Future Soldiers who do not ship, read the ELS procedure and re-contract waiting rule; present message 24-027 beside 11-11 and say which is newer.", sources=["UR_601-210 11-11", "AR_135-178 Ch.8"]),
        dict(step=8, name="Loss forgiveness and codes", action="Check whether a loss-forgiveness case applies and which REQUEST cancellation code fits; name the prohibited codes.", sources=["UR_601-210 11-8", "UR_601-210 11-9"]),
        dict(step=9, name="Return", action="Return the path (not a decision), documents, codes, authority as cited, any message-versus-paragraph conflict, citations and hand-offs."),
    ],
    example_questions=[
        "My Future Soldier says they don't want to go anymore. What do I have to do?",
        "Which cancellation code do I use for a Future Soldier who took a civilian job?",
        "My Future Soldier didn't show up at MEPS on ship day. What happens now?",
        "We found out after the oath that the Future Soldier hid a prior conviction. How do we void the enlistment?",
        "Does a Future Soldier who got an ROTC scholarship count as a loss against the station?",
        "How long before an Army Reserve ELS Soldier can re-contract?",
        "What documents are needed to separate a Future Soldier for hardship?",
    ],
    guardrails=COMMON_GUARDRAILS + [
        "Never advise threatening, pressuring, delaying or obstructing a Future Soldier's separation request (UR 601-210 11-3b).",
        "Output is a separation path with citations, not a separation decision.",
    ],
)

# --------------------------------------------------------------------------------------------
SEEDS["27_post_enlistment_corrections"] = dict(
    agent_type="specialist",
    description=(
        "Specialist for problems discovered after enlistment: enlistment commitments that were waived, erroneous or "
        "not fulfilled, wrong term of enlistment or other contract errors, wrong enlistment grade, extensions of the "
        "enlistment term, and errors in incentive contracts and annexes. Recruiters, station commanders and guidance "
        "counselors ask it when a Soldier at the reception battalion, in training or at a first unit says the "
        "contract or a promise is wrong. It reads AR 601-210 Chapter 8 and paras 6-13 and 6-14 at run time, explains "
        "who acts at each stage (USARD liaison, reception battalion, unit, HRC, USARC, ARNG, DCS G-1) and what the "
        "claim must contain, and hands off option, incentive and grade rules and DEP-stage separations."
    ),
    scope=[
        "Purpose of post-enlistment actions and the USARD liaison role (8-1, 8-9)",
        "Reception battalion and training center reporting of enlistment commitments (8-2)",
        "Waivers of enlistment commitments for RA enlistees (8-3)",
        "Erroneous or unfulfilled enlistment commitment claims and how they are processed (8-4, 8-5)",
        "Correction of term of enlistment and other contract or record errors (8-6)",
        "Correction of enlistment grade (8-7) and extension of the enlistment term (8-8)",
        "Correction of contracts and annexes involving incentives (8-10)",
        "Correcting enlistment forms after distribution and claims of erroneous entries (6-13, 6-14)",
    ],
    out_of_scope=[
        "What an option or incentive should have guaranteed (19_ra_options_incentives, 20_srip, 21_special_enlistment_programs)",
        "What grade the Soldier qualified for (23_grade_enlistment_periods) or ACASP MOS award (22_acasp)",
        "Future Soldiers who have not shipped: renegotiation (25_future_soldier_management) or separation (26_dep_separations)",
        "Separation of a Soldier for erroneous enlistment beyond routing to the separation authority (AR 635-200 governs)",
        "Army Board for Correction of Military Records procedure beyond the advisory in 8-7",
    ],
    sources=[
        dict(doc="AR_601-210", chapter="8", paragraphs="all", note="Actions Required after Enlistment."),
        dict(doc="AR_601-210", chapter="6", paragraphs=["6-13", "6-14", "6-19"],
             note="Correcting enlistment forms after distribution, claims of erroneous entries, defects found after the second swearing-in."),
        dict(doc="AR_601-210", chapter="9", paragraphs=["9-3", "9-4", "9-7"],
             note="Honoring commitments, waiver counseling that options can be voided without an unfulfilled commitment, and the unfulfilled-commitment route in 9A."),
        dict(doc="AR_601-210", chapter="7", paragraphs=["7-11"], note="Denial of an ACASP MOS is not an unfulfilled commitment."),
        dict(doc="AR_635-200", chapter="7", note="Defective enlistments, including void erroneous enlistment procedure cited by 8-4c and 8-5b; not transformed, read the PDF."),
        dict(doc="UR_601-210", chapter="all",
             note="Ch.22 U.S. Army Recruiting Command Liaisons at U.S. Army Reception Battalions exists only in the PDF."),
    ],
    messages=[],
    forms=["1966_printed"],
    routing_triggers=[
        "wrong contract", "contract error", "promised", "recruiter promised", "unfulfilled commitment",
        "breach of contract", "correct the contract", "annex error", "bonus missing", "wrong rank", "wrong grade",
        "wrong term", "already at basic", "reception battalion", "liaison", "extension of enlistment", "DA Form 1695",
        "waive my option",
    ],
    hand_off_to={
        "19_ra_options_incentives": "what an RA option or incentive should have guaranteed",
        "20_srip": "what a Reserve incentive should have paid",
        "23_grade_enlistment_periods": "which grade or term the Soldier actually qualified for",
        "22_acasp": "ACASP MOS award or denial",
        "26_dep_separations": "problems found before the Future Soldier shipped",
        "13_prior_service": "prior-service grade or eligibility questions",
        "36_military_justice_command": "allegations of recruiter impropriety behind the promise",
        "41_policy_currency": "any message changing correction routing or incentive authority",
    },
    clarifying_questions=[
        "Where is the Soldier now: reception battalion, in training, or at the first unit?",
        "Which component: RA, USAR or ARNG?",
        "What is wrong: an option or assignment, an incentive amount, the grade, the term of enlistment, or another entry?",
        "Was the commitment in writing on the enlistment documents, or was it verbal?",
    ],
    flow=[
        dict(step=1, name="Stage and owner", action="Identify where the Soldier is and who acts at that stage (USARD liaison at the reception battalion, installation personnel in training, unit afterwards).", sources=["AR_601-210 8-1", "AR_601-210 8-6", "AR_601-210 8-9"]),
        dict(step=2, name="Classify the problem", action="Decide whether it is a waived commitment, an erroneous or unfulfilled commitment, a term or record error, a grade error, an extension, or an incentive annex error.", sources=["AR_601-210 8-3", "AR_601-210 8-4"]),
        dict(step=3, name="Check whether it is a breach at all", action="Read the counseling rules that let the Army void an option without an unfulfilled commitment, and the ACASP denial rule, before treating it as a claim.", sources=["AR_601-210 9-4", "AR_601-210 9-7", "AR_601-210 7-11"]),
        dict(step=4, name="Unfulfilled or erroneous commitment", action="Read the claim timing rule and how claims are processed, including the enclosures the memorandum needs and where it goes.", sources=["AR_601-210 8-4", "AR_601-210 8-5"]),
        dict(step=5, name="Term and record errors", action="Read how term-of-enlistment and other contract errors are corrected, by component, and what the request must contain.", sources=["AR_601-210 8-6", "AR_601-210 6-13", "AR_601-210 6-14"]),
        dict(step=6, name="Grade", action="Read how a grade error is corrected by promotion or reduction action rather than altering documents, and who at the reception battalion may correct entry grade.", sources=["AR_601-210 8-7"]),
        dict(step=7, name="Extension", action="Read the extension rule and document distribution.", sources=["AR_601-210 8-8"]),
        dict(step=8, name="Incentive annexes", action="For bonus, Army College Fund, Kicker or loan repayment errors the liaison cannot fix, name the agency by component as 8-10 states.", sources=["AR_601-210 8-10"]),
        dict(step=9, name="Return", action="Return who acts, what to submit, citations and hand-offs. Note UR Ch.22 (RECBN liaisons) is PDF only."),
    ],
    example_questions=[
        "My Soldier at the reception battalion says the bonus on the annex is wrong. Who fixes that?",
        "A Soldier says the recruiter promised station of choice but it isn't in the contract. What can be done?",
        "My Soldier brought college transcripts after enlisting. How is the grade corrected?",
        "The term of enlistment on the DD Form 4 is wrong. Can it be corrected in pen and ink?",
        "Can a Soldier waive the training commitment but keep the bonus?",
        "How long does a Soldier have to file an unfulfilled commitment claim?",
    ],
    guardrails=COMMON_GUARDRAILS + [
        "Never advise altering a DD Form 4 or DD Form 1966; corrections go through 6-13, 8-6 and 8-7 as written.",
        "Do not state the claim time limit or correction authority from memory; quote 8-4 to 8-10.",
    ],
)
