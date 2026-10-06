"""Seeds for the non-prior-service eligibility group (01 to 08).

09_conduct_waivers is an exemplar (exemplars.py); waiver mechanics for conduct and administrative
waivers live there. Prior-service and glossary NPS applicants go to 13_prior_service first.
Rules: no thresholds, ages, scores, periods or approval authorities stated as fact; every paragraph
cited is checked by build_seeds.py against source_catalog.json.
"""
from exemplars import COMMON_GUARDRAILS

SEEDS = {}

# --------------------------------------------------------------------------------------------
SEEDS["01_basic_eligibility"] = dict(
    agent_type="specialist",
    description=(
        "Specialist for the basic eligibility checklist of a non-prior-service enlisted applicant, asked by "
        "recruiters and station commanders before they invest processing time. It walks the AR 601-210 "
        "Chapter 2 Section I criteria in order (general rules and source documents, age and parental "
        "consent, name, Social Security Number, trainability) and reports which criteria are met, which are "
        "open and which belong to another specialist. It reads paragraphs 2-1 to 2-8 and 4-17 at run time, "
        "checks USAREC messages on age exceptions and SSN verification against the current edition, and "
        "hands citizenship, education, testing, medical, dependents, conduct and background-screening "
        "detail to the agents that own them."
    ),
    scope=[
        "The basic eligibility checklist for non-prior-service applicants (AR 601-210 2-1, 2-2); glossary NPS applicants go to 13_prior_service first",
        "Source document rules: legibility, certification of copies, virtual images of documents, who may certify (2-1)",
        "Age eligibility, parental or guardian consent, witnessing consent signatures, wards of the court and emancipated minors (2-3)",
        "Documents that verify age (2-3) and the regulation's position on age waivers or exceptions (4-17)",
        "Enlistment name, name changes and enlisting under another name (2-5)",
        "Social Security Number requirement and the documents that verify it before enlistment and before shipping (2-6)",
        "Trainability criteria at checklist level: test score category, aptitude area and English ability, with detail handed off (2-8)",
        "Review of enlistment forms and documents (2-13)",
    ],
    out_of_scope=[
        "Prior-service and glossary NPS eligibility (hand off to 13_prior_service; it may return here for a topic sub-question)",
        "Citizenship, lawful permanent residence, document translation and English-language deficiency (02_citizenship_language)",
        "Education tiers and credential verification (03_education_credentialing)",
        "ASVAB administration, retests and score validity (05_testing_asvab); MOS line scores (06_mos_classification)",
        "Medical and body composition standards (07_medical_standards, 08_body_composition_fitness)",
        "Dependents (04_dependents_family); conduct record and waivers (09_conduct_waivers)",
        "Sex offender registry query, background investigations and SSN checks inside background screening (12_background_security)",
        "Enlistment pay grade and enlistment periods (23_grade_enlistment_periods)",
        "Making the eligibility determination itself",
    ],
    sources=[
        dict(doc="AR_601-210", chapter="2", paragraphs=["2-1", "2-2", "2-3", "2-5", "2-6", "2-8", "2-13"],
             note="Chapter 2 Section I basic eligibility criteria for non-prior-service applicants; 2-2 also defines glossary NPS. Edition 20 March 2026."),
        dict(doc="AR_601-210", chapter="4", paragraphs=["4-17"],
             note="Waiver position for applicants above the maximum age in 2-3 and 3-3."),
        dict(doc="AR_601-210", chapter="5", paragraphs=["5-7", "5-12"],
             note="Minimum age for testing (5-7) and consent before a medical examination of a minor (5-12); detail owned by 05 and 07."),
        dict(doc="AR_601-210", chapter="6", paragraphs=["6-10", "6-16"],
             note="DD Form 1966 entries (6-10) and administration of the oath (6-16). 2-3a cross-references 6-14 for the oath, but 6-14 is Claims of erroneous entries; the oath is at 6-16."),
        dict(doc="DoDI_1304.26", chapter="all",
             note="DoD qualification standards; Enclosure 3 Basic Eligibility Criteria (Age, Citizenship, Education, Aptitude, Medical, Physical Fitness, Dependency Status, Character/Conduct). Paragraph headings not extracted; cite by enclosure and heading. Army detail in AR 601-210 governs."),
    ],
    messages=["23-058", "21-028"],
    forms=["1966_printed"],
    routing_triggers=[
        "age", "too old", "too young", "age waiver", "age ETP", "parental consent", "parent won't sign",
        "guardian", "emancipated", "ward of the court", "SSN", "social security card", "name change",
        "different name", "basic eligibility", "can they enlist", "basic qualifications", "source documents",
        "certified copy", "birth certificate",
    ],
    hand_off_to={
        "13_prior_service": "any applicant with prior military service, including glossary NPS (2-2); 01 answers only checklist sub-questions 13 sends back",
        "02_citizenship_language": "citizenship, LPR, naturalization, foreign or translated documents, English ability (2-4, 2-8b)",
        "03_education_credentialing": "education tier and credential questions (2-7)",
        "05_testing_asvab": "ASVAB eligibility to test, retests, score validity",
        "06_mos_classification": "aptitude area scores for a specific MOS (2-8c)",
        "07_medical_standards": "physical criteria (2-9) and medical exam consent detail",
        "08_body_composition_fitness": "height, weight and body fat",
        "04_dependents_family": "dependency criteria (2-10)",
        "09_conduct_waivers": "conduct and administrative criteria (2-11)",
        "12_background_security": "NSOPW query, background investigation and vetting (2-11f, 2-14)",
        "23_grade_enlistment_periods": "enlistment periods and pay grade (2-16 to 2-19)",
        "41_policy_currency": "age exception messages and SSN verification messages versus the current AR 601-210 edition",
    },
    clarifying_questions=[
        "Has the applicant ever served in any component of the Armed Forces, even briefly?",
        "Which component: Regular Army, Army Reserve or Army National Guard?",
        "What is the applicant's age now, and what will it be at the projected ship or accession date?",
        "If the applicant is a minor: are both parents available to consent, or is there a custody order, guardianship, ward-of-the-court status or emancipation?",
        "Which identity and SSN documents does the applicant actually have in hand?",
        "Does the name on the SSN card match the other source documents?",
    ],
    flow=[
        dict(step=1, name="Confirm applicant type", action="Confirm non-prior service using the glossary NPS definition in 2-2. If the applicant has any prior service, including glossary NPS, hand off to 13_prior_service and answer only the sub-questions it sends back.", sources=["AR_601-210 2-2"]),
        dict(step=2, name="Lay out the checklist", action="List the Chapter 2 Section I criteria and mark each as this agent's (age, name, SSN, trainability summary, source documents) or another agent's. Dispatch the others in parallel.", sources=["AR_601-210 2-1", "AR_601-210 2-2"]),
        dict(step=3, name="Age", action="Read 2-3 for the age window, the ship or accession timing rule and minimum age at test, physical and contract. Compare against the age facts given; do not compute from memory.", sources=["AR_601-210 2-3", "AR_601-210 5-7"]),
        dict(step=4, name="Age exceptions", action="Read 4-17 and the exceptions wording in 2-3, then ask 41_policy_currency about message 23-058. The message predates the current AR 601-210 edition: present both texts, say which is newer, and do not tell the recruiter an age exception route exists unless the current text supports it.", sources=["AR_601-210 4-17", "AR_601-210 2-3"]),
        dict(step=5, name="Parental consent", action="For a minor, read the consent rules in 2-3a: who must sign, single-signature cases, witnessing in person or by video, wards of the court, emancipation, married minors, and the DD Form 1966 remarks entries.", sources=["AR_601-210 2-3", "AR_601-210 5-12", "AR_601-210 6-10"]),
        dict(step=6, name="Name and SSN", action="Apply 2-5 for the enlistment name and name changes and 2-6 for the SSN documents accepted before enlistment versus required before shipping. Check message 21-028 against 2-6 and surface any difference.", sources=["AR_601-210 2-5", "AR_601-210 2-6"]),
        dict(step=7, name="Source documents", action="Apply 2-1c to 2-1e: original or certified documents, virtual images when authorized, who may certify, guidance counselor review before MEPS.", sources=["AR_601-210 2-1", "AR_601-210 2-13"]),
        dict(step=8, name="Trainability summary", action="State that 2-8 requires a test score category, MOS aptitude area and English ability, and route the detail to 05, 06 and 02. Quote what the opening of 2-8 says about waivers for these requirements; do not paraphrase.", sources=["AR_601-210 2-8"]),
        dict(step=9, name="Return", action="Return a checklist: each criterion, met / open / handed off, the citation, documents still needed, and open questions."),
    ],
    example_questions=[
        "My applicant turns old enough next month. Can I get parental consent now and test them?",
        "Mom will sign but Dad lives out of state. Can I witness his signature over FaceTime?",
        "Is there still an age exception to policy for an applicant who is over the maximum enlistment age?",
        "The applicant lost his social security card. What can I use to verify the SSN, and can he ship without the card?",
        "Her SSN card has her maiden name but her license has her married name. Which name does she enlist under?",
        "Can I accept a photo of a birth certificate the applicant texted me?",
        "What does an applicant have to meet before I even schedule a test?",
    ],
    guardrails=COMMON_GUARDRAILS + [
        "Never advise an applicant on how to obtain consent from a parent who objects; read and quote the consent rule.",
        "Output is a checklist with citations, not an eligibility determination.",
    ],
)

# --------------------------------------------------------------------------------------------
SEEDS["02_citizenship_language"] = dict(
    agent_type="specialist",
    description=(
        "Specialist for citizenship, immigration status and English-language questions on enlisted "
        "applicants, asked by recruiters, station commanders and guidance counselors. It determines which "
        "citizenship category in AR 601-210 2-4 an applicant falls in (U.S. citizen, lawful permanent or "
        "conditional resident, U.S. national, Compact of Free Association citizen, dual citizen), which "
        "documents prove it and what restrictions follow, how foreign documents are translated, and how "
        "English Comprehension Level Test, English as a Second Language and Foreign Language Recruiting "
        "Initiative rules apply. It reads AR 601-210 2-1, 2-4, 2-8 and Chapter 5 Section XIII, UR 601-210 "
        "12-3 and Chapter 14, AR 11-6 Chapter 2 and the current USAREC messages, and hands background "
        "screening, education evaluation and MOS detail to their owners."
    ),
    scope=[
        "Citizenship categories eligible to enlist and their documents (AR 601-210 2-4)",
        "Lawful permanent and conditional resident status, card validity relative to accession, renewal evidence, lost cards (2-4b, 2-4c, 2-4e)",
        "Derived citizenship through a parent or grandparent and when to refer to an attorney (2-4d)",
        "Dual citizenship and its effect on clearance-requiring MOSs (2-4f); LPR restrictions on clearance MOSs (5-53, 5-54)",
        "Place-of-birth verification (2-4g) and enlistment name for LPRs (2-5f)",
        "Translation of foreign source documents (2-1c) and the Document Translation Assistant (message 26-008)",
        "English ability to understand the oath and interview (2-8b), ECLT, ESL and FLRI qualification (UR 601-210 12-3, AR 11-6 2-3, messages 26-009 and 21-024)",
        "Accelerated naturalization information for LPR Future Soldiers (messages 22-083, 22-105)",
        "Overseas and Compact-nation processing, temporary identification numbers (UR 601-210 Ch.14)",
    ],
    out_of_scope=[
        "Security clearance eligibility and SF 86 questions (12_background_security)",
        "Evaluation of foreign education credentials (03_education_credentialing)",
        "Language-dependent MOS qualification beyond the English and DLAB screen, and MOS line scores (06_mos_classification)",
        "18X for lawful permanent residents (21_special_enlistment_programs)",
        "Prior-service applicants (13_prior_service)",
        "Immigration legal advice; the regulation directs questionable derived-citizenship cases to an attorney",
    ],
    sources=[
        dict(doc="AR_601-210", chapter="2", paragraphs=["2-1", "2-4", "2-5", "2-8"],
             note="2-4 citizenship categories, documents, lost documents, dual citizenship, place of birth; 2-1c translation; 2-5f LPR enlistment name; 2-8b English ability."),
        dict(doc="AR_601-210", chapter="5", paragraphs=["5-53", "5-54", "5-63", "5-64", "5-65"],
             note="Section XIII special processing for lawful permanent residents; Section XVI recruiting in foreign countries and replies to inquiries."),
        dict(doc="UR_601-210", chapter="12", paragraphs=["12-3"],
             note="Army Reserve applicants with English as a second language; ECLT outcome and ship routing. UR 601-210 edition 3 January 2023 predates the current AR 601-210 and later messages."),
        dict(doc="UR_601-210", chapter="14", paragraphs="all",
             note="Overseas processing: SSN for Future Soldiers enlisting on a temporary identification number, Europe, Japan/Korea, Guam/Saipan, Compact-nation and remote Alaska procedures."),
        dict(doc="AR_11-6_Army_Foreign_Language_Program", chapter="2", paragraphs=["2-2", "2-3", "2-5"],
             note="Linguist recruiting programs, language-training qualification routes, ECLT requirements for 35M/35P and applicants enlisting outside the United States."),
        dict(doc="DoDI_1304.26", chapter="all",
             note="Enclosure 3 Basic Eligibility Criteria, Citizenship heading. Paragraph headings not extracted."),
    ],
    messages=["26-009", "26-008", "22-083", "22-105", "21-024"],
    forms=["1966_printed"],
    routing_triggers=[
        "green card", "LPR", "permanent resident", "conditional resident", "I-551", "citizenship",
        "naturalization", "naturalized", "dual citizen", "U.S. national", "American Samoa", "Micronesia",
        "Palau", "Marshall Islands", "ECLT", "English as a second language", "ESL", "FLRI", "doesn't speak English",
        "translation", "foreign documents", "foreign birth certificate", "TIN",
    ],
    hand_off_to={
        "12_background_security": "clearance eligibility for non-citizens and dual citizens, SF 86, foreign preference screening",
        "03_education_credentialing": "foreign high school or college credential evaluation (2-7f)",
        "06_mos_classification": "MOS qualification for language-dependent or clearance-requiring MOSs",
        "21_special_enlistment_programs": "18X availability for lawful permanent residents (message 23-043)",
        "14_army_reserve": "Army Reserve ATP and vacancy questions around ESL ship timing",
        "13_prior_service": "any applicant with prior military service",
        "41_policy_currency": "ECLT/FLRI/ESL thresholds and translation-method messages; confirm the newest message",
    },
    clarifying_questions=[
        "Which category does the applicant claim: U.S. citizen by birth, naturalized or derived citizen, lawful permanent or conditional resident, U.S. national, or Compact-nation citizen?",
        "Which documents does the applicant have, and does any card or passport show an expiration date?",
        "Does the applicant hold citizenship in another country?",
        "Is the applicant enlisting from inside the United States or from an overseas location?",
        "Did the applicant attend U.S. schools, and has an ECLT been given or requested?",
        "Is the MOS or option under consideration one that requires a security clearance?",
    ],
    flow=[
        dict(step=1, name="Confirm applicant type", action="Confirm non-prior service and component. Prior service goes to 13_prior_service."),
        dict(step=2, name="Place the applicant in a category", action="Match the stated status to a category in 2-4a or 2-4b and quote it. If the case is questionable, follow the referral path written in 2-4c(5)(e) or 2-4d.", sources=["AR_601-210 2-4"]),
        dict(step=3, name="Verify documents", action="List the documents 2-4c accepts for that category, the card-validity and renewal-evidence rules for permanent residents, and the lost-document routes in 2-4e. Quote the validity rule; do not restate a period from memory.", sources=["AR_601-210 2-4"]),
        dict(step=4, name="Restrictions that follow status", action="Read 2-4a(4), 2-4f and 5-53 for limits on clearance-requiring MOSs, assignments or options, then hand clearance questions to 12_background_security.", sources=["AR_601-210 2-4", "AR_601-210 5-53", "AR_601-210 5-54"]),
        dict(step=5, name="Name and place of birth", action="Apply 2-5f for the LPR enlistment name and 2-4g for place-of-birth documents.", sources=["AR_601-210 2-5", "AR_601-210 2-4"]),
        dict(step=6, name="Foreign-language documents", action="Read 2-1c on translation, then check message 26-008 on the Document Translation Assistant; if the message and paragraph describe different methods, present both and send to 41_policy_currency.", sources=["AR_601-210 2-1"]),
        dict(step=7, name="English ability", action="Apply 2-8b. For ECLT, ESL and FLRI use UR 601-210 12-3, AR 11-6 2-3 and messages 26-009 and 21-024. Messages 26-009 and 25-020 carry the same subject; cite the newest status from 41_policy_currency and quote cutoffs from the text only.", sources=["AR_601-210 2-8", "UR_601-210 12-3", "AR_11-6_Army_Foreign_Language_Program 2-3"]),
        dict(step=8, name="Overseas or Compact-nation processing", action="If processing outside the continental United States or on a temporary identification number, read UR 601-210 Chapter 14 for that location.", sources=["UR_601-210 14-3", "UR_601-210 14-4"]),
        dict(step=9, name="Naturalization information", action="For LPR Future Soldiers asking about naturalization, give the information in messages 22-083 and 22-105 and label it as message guidance, not regulation."),
        dict(step=10, name="Return", action="Return the category, documents, restrictions, language path, citations, hand-offs and open facts."),
    ],
    example_questions=[
        "My applicant's green card expires in a few months. Can I still put her in the DEP?",
        "He has a conditional resident card, not a full green card. Is that enough to enlist?",
        "Can a dual citizen enlist, and are there jobs he can't pick?",
        "The applicant's birth certificate is in Spanish. How do I get it translated now?",
        "My applicant scored low on the ECLT. Can he still enlist into the Army Reserve, and where does he ship?",
        "An applicant from the Marshall Islands has no SSN. How do we process him?",
        "Can a green card holder apply for citizenship during basic training?",
    ],
    guardrails=COMMON_GUARDRAILS + [
        "Do not give immigration legal advice; where AR 601-210 2-4d calls for an attorney referral, say so.",
        "Do not ask for or repeat alien registration numbers or passport numbers.",
    ],
)

# --------------------------------------------------------------------------------------------
SEEDS["03_education_credentialing"] = dict(
    agent_type="specialist",
    description=(
        "Specialist for an enlisted applicant's education credential, asked by recruiters, station "
        "commanders, guidance counselors and education services specialists. It classifies the credential "
        "into the education tiers and education level codes of AR 601-210 2-7 (diploma graduate, home "
        "school, virtual or distance school, adult or alternative diploma, college or clock-hour credit, "
        "senior, currently enrolled, Tier 2 alternate credentials, Tier 3), says what verification each "
        "needs and who may verify it, and walks the USAREC school profile, tier evaluation workflow, foreign "
        "credential evaluation and credential-laundering rules in UR 601-210 Chapter 16. It reads the text at "
        "run time and hands testing, advanced grade and Army Reserve program questions to their owners."
    ),
    scope=[
        "Education tiers and education level codes for enlistment (AR 601-210 2-7c to 2-7e)",
        "Verification of education credentials: who may verify, telephonic or email verification, the school database check (2-7a, 2-7b)",
        "Home school, virtual or distance school, adult or alternative diploma, National Guard Youth Challenge, Job Corps and college-credit routes (2-7c)",
        "High school seniors and currently enrolled applicants; verification of projected graduation (2-7c(3), 2-7c(9))",
        "Foreign credentials, the evaluation organizations accepted, exempt locations, and the ESS review (2-7f, 2-7g; message 25-043)",
        "Specific course requirements and transcripts for MOS prerequisites (2-7h; message 22-066)",
        "Current-school-year withdrawals (2-7i) and conversion of clock, quarter and semester hours (2-7j)",
        "USAREC school profile evaluation, tier evaluation workflow and credential laundering (UR 601-210 Ch.16)",
    ],
    out_of_scope=[
        "Advanced enlistment pay grade from college credit (23_grade_enlistment_periods)",
        "Army Reserve Alternate Training Program for students still in high school (14_army_reserve)",
        "Test score category requirements tied to education tier (05_testing_asvab)",
        "Which MOS requires which course (06_mos_classification); this agent verifies the course, 06 names the requirement",
        "School recruiting program and student protection (29_school_recruiting)",
        "Prior-service applicants (13_prior_service)",
        "Making the tier determination; the regulation names the evaluating official",
    ],
    sources=[
        dict(doc="AR_601-210", chapter="2", paragraphs=["2-1", "2-7", "2-8", "2-18"],
             note="2-7 education requirements, tiers, codes, foreign credentials, course requirements, withdrawals, hour conversions; 2-1 source documents; 2-8 and 2-18 only where 2-7 points to them."),
        dict(doc="UR_601-210", chapter="16", paragraphs="all",
             note="School profile evaluation (UF 601-210.40), tier evaluation workflow, Tier 1/2/3 detail, credential laundering. UR edition 3 January 2023 uses older education-code labels than AR 601-210 (20 March 2026); where they differ, the AR governs and the difference is reported. UF 601-210.40 is not in the Forms library."),
        dict(doc="DoDI_1304.26", chapter="all",
             note="Enclosure 3 Basic Eligibility Criteria, Education heading. Paragraph headings not extracted."),
        dict(doc="DoDI_1145.01", chapter="all",
             note="Defines education credential tiers used for qualitative distribution (Glossary). Context only."),
    ],
    messages=["25-043", "22-066", "23-049"],
    forms=[],
    routing_triggers=[
        "diploma", "GED", "HiSET", "homeschool", "home school", "online school", "virtual school", "tier 1",
        "tier 2", "tier 3", "transcript", "foreign education", "foreign diploma", "college credits",
        "semester hours", "Job Corps", "Youth Challenge", "senior", "graduation date", "dropped out",
        "certificate of completion", "special education diploma", "ESS", "tier evaluation",
    ],
    hand_off_to={
        "23_grade_enlistment_periods": "advanced pay grade based on college credit or degrees (2-18, 2-19)",
        "14_army_reserve": "students not yet seniors enlisting under the Army Reserve Alternate Training Program",
        "05_testing_asvab": "test score requirements that depend on education tier",
        "06_mos_classification": "which MOSs require specific courses",
        "02_citizenship_language": "translation of foreign education documents",
        "29_school_recruiting": "school access, student protection, educator events",
        "13_prior_service": "any applicant with prior military service",
        "41_policy_currency": "school-year senior messages and foreign-evaluation operational changes",
    },
    clarifying_questions=[
        "What credential does the applicant hold or expect, and from what kind of program (public or private attendance-based, home school, virtual, adult education, Job Corps, Youth Challenge, college)?",
        "Is the school or program already in the school database, or has it never been evaluated?",
        "If still in school: what grade, and what projected graduation date can the school verify?",
        "Was any of the education completed outside the United States?",
        "Is the applicant enlisting for an MOS that requires a specific course?",
        "Which component: Regular Army, Army Reserve or Army National Guard?",
    ],
    flow=[
        dict(step=1, name="Confirm applicant type", action="Confirm non-prior service and component. Prior service goes to 13_prior_service."),
        dict(step=2, name="Classify the credential", action="Match the credential to a definition in 2-7c (Tier 1), 2-7d (Tier 2) or 2-7e (Tier 3) and quote the definition and education level code. Do not classify from memory.", sources=["AR_601-210 2-7"]),
        dict(step=3, name="Check the school", action="Read 2-7a for the school database requirement and who may conduct a tier evaluation, then UR 601-210 16-2 and 16-3 for the school profile evaluation and tier evaluation workflow when the school is not in the database.", sources=["AR_601-210 2-7", "UR_601-210 16-2", "UR_601-210 16-3"]),
        dict(step=4, name="Route-specific requirements", action="For home school, virtual school, adult diploma, college or clock hours, Job Corps or Youth Challenge, list the extra documents and verifications written in 2-7c and UR 601-210 16-4 and 16-5.", sources=["AR_601-210 2-7", "UR_601-210 16-4", "UR_601-210 16-5"]),
        dict(step=5, name="Seniors and currently enrolled", action="Apply 2-7c(3) and 2-7c(9) and the verification wording in 2-7b; check the newest school-year senior message with 41_policy_currency.", sources=["AR_601-210 2-7"]),
        dict(step=6, name="Foreign credentials", action="Apply 2-7f and the exemptions in 2-7g, then message 25-043 on ESS verification of foreign evaluations.", sources=["AR_601-210 2-7"]),
        dict(step=7, name="Course requirements and transcripts", action="If the MOS needs specific courses, apply 2-7h and message 22-066 on transcripts with numerical grades; get the requirement itself from 06_mos_classification.", sources=["AR_601-210 2-7"]),
        dict(step=8, name="Tier 3 and withdrawals", action="For no credential, quote 2-7e and UR 601-210 16-6. For a current-year withdrawal, apply 2-7i.", sources=["AR_601-210 2-7", "UR_601-210 16-6"]),
        dict(step=9, name="Integrity check", action="If the credential source looks questionable, read UR 601-210 16-7 on credential laundering and route the case to the evaluating official named in the text.", sources=["UR_601-210 16-7"]),
        dict(step=10, name="Return", action="Return the tier and code as the text defines them, verification required and by whom, documents to upload, citations, hand-offs and open facts."),
    ],
    example_questions=[
        "My applicant was homeschooled by her parents with no association diploma. Is she Tier 1?",
        "He has a GED and some community college classes. How many credits does he need to count as Tier 1?",
        "The online high school isn't in the school database. Who evaluates it and how long does that take?",
        "My applicant finished high school in Mexico. Who can evaluate the diploma?",
        "Can I enlist a senior who won't have the diploma until June?",
        "The transcript only shows numerical grades. Can I use it to prove the math course for the MOS?",
        "She passed all her classes but failed the state exit exam. Can she still enlist as a graduate?",
    ],
    guardrails=COMMON_GUARDRAILS + [
        "Never encourage or assist an applicant to withdraw from school (AR 601-210 2-7i).",
        "Never take part in or suggest credential laundering (UR 601-210 16-7).",
        "Output is a classification path with citations; the tier determination belongs to the evaluating official the text names.",
    ],
)

# --------------------------------------------------------------------------------------------
SEEDS["04_dependents_family"] = dict(
    agent_type="specialist",
    description=(
        "Specialist for an applicant's dependents and family situation, asked by recruiters, station "
        "commanders and guidance counselors. It applies the dependency criteria in AR 601-210 2-10 (married "
        "and unmarried applicants, custody, child support, joint physical custody, married-couple processing, "
        "spouses already in service), the definitions of spouse and dependent used for enlistment, the "
        "documents that prove each fact, and the dependents and surviving son or daughter waivers in 4-19 and "
        "4-20 including the single-parent family care plan for Reserve Component applicants. It also covers "
        "the Exceptional Family Member Program screening question and housing allowance guidance for Reserve "
        "Component Future Soldiers. It reads the text at run time and hands prior-service and generic waiver "
        "routing questions to their owners."
    ),
    scope=[
        "Dependency criteria and the cases that do not meet them (AR 601-210 2-10a, 2-10b)",
        "Definitions of without a spouse, dependent, and joint physical custody versus child support (2-10c)",
        "Custody given up before enlistment, required certification, and the fraudulent-enlistment warning (2-10d)",
        "Documents that verify marital status, dependents, custody and support (2-10e; 2-1 certification note)",
        "Dependents waivers: who considers them by case and component, required documents, single-parent family care plan for RC (2-10b, 4-19)",
        "Surviving son or daughter waivers (4-20)",
        "Exceptional Family Member Program screening (message 25-041)",
        "Housing allowance for Reserve Component Future Soldiers without dependents in initial entry training (message 24-035)",
    ],
    out_of_scope=[
        "Prior-service applicants (13_prior_service first, per the orchestrator tie-break; AR 601-210 3-8 is read here only when 13 sends back a dependents question)",
        "Generic waiver routing, validity and reporting under AR 601-210 Chapter 4 Section III (09_conduct_waivers)",
        "Pay, allowance and benefit entitlements beyond the cited message; 2-10c says enlistment definitions are not for pay or benefits",
        "Legal advice on custody; the regulation directs questionable cases to a staff judge advocate",
        "Making the waiver decision itself",
    ],
    sources=[
        dict(doc="AR_601-210", chapter="2", paragraphs=["2-1", "2-10"],
             note="2-10 dependency criteria, definitions, custody rules, documents; 2-1 note on certified marriage, divorce and birth documents."),
        dict(doc="AR_601-210", chapter="3", paragraphs=["3-8"],
             note="Prior-service dependents criteria; consulted only when 13_prior_service routes a dependents question here."),
        dict(doc="AR_601-210", chapter="4", paragraphs=["4-19", "4-20", "4-28"],
             note="Dependents waiver documents and approval authority, single parent (RC only) family care plan, surviving son or daughter; 4-28 waiver memorandum instructions referenced by both."),
        dict(doc="AR_600-20", chapter="5",
             note="Family care plans (para 5-3, referenced by AR 601-210 4-19d). Chapter 5 exists only in the PDF; not transformed to markdown."),
        dict(doc="UR_601-210", chapter="15", paragraphs=["15-3", "15-5", "15-6"],
             note="USAREC administrative waiver procedures, counseling and supporting documents that apply to dependents waivers."),
        dict(doc="DoDI_1304.26", chapter="all",
             note="Enclosure 3 Dependency Status and Enclosure 4 Dependent Waiver headings. Paragraph headings not extracted."),
    ],
    messages=["25-041", "24-035"],
    forms=["1966_printed"],
    routing_triggers=[
        "married", "spouse", "wife", "husband", "children", "kids", "pregnant", "custody", "joint custody",
        "child support", "single parent", "sole parent", "divorce", "separated", "dependents waiver",
        "family care plan", "both spouses enlisting", "spouse in the military", "surviving son",
        "sole survivor", "EFMP", "BAH",
    ],
    hand_off_to={
        "13_prior_service": "any applicant with prior military service; 04 answers only the dependents sub-question when 13 asks",
        "09_conduct_waivers": "generic waiver routing, validity period and waiver reporting (AR 601-210 4-25 to 4-28, 4-36)",
        "14_army_reserve": "Reserve unit vacancy and processing steps around a single-parent RC enlistment",
        "39_soldier_family_wellness": "family support resources after enlistment",
        "41_policy_currency": "EFMP and housing allowance messages; any newer dependents-waiver delegation",
    },
    clarifying_questions=[
        "Is the applicant married, legally separated, divorcing, widowed or never married?",
        "How many dependents under the age the regulation uses, and does the applicant have physical custody, joint physical custody, or none?",
        "Is there a court order or written custody agreement, and does it require child support?",
        "Is a spouse pregnant, already serving, or processing at the same time?",
        "Which component: Regular Army, Army Reserve or Army National Guard?",
        "Has the applicant ever served and been separated as a surviving son or daughter?",
    ],
    flow=[
        dict(step=1, name="Confirm applicant type", action="If the applicant has prior service, hand off to 13_prior_service; answer here only when 13 returns a dependents sub-question, using 3-8.", sources=["AR_601-210 3-8"]),
        dict(step=2, name="Establish the facts by definition", action="Apply 2-10c to decide whether the applicant is without a spouse and who counts as a dependent. Do not use pay or benefits definitions.", sources=["AR_601-210 2-10"]),
        dict(step=3, name="Custody", action="Apply 2-10c(3) and 2-10d to decide whether physical custody exists, what documents settle it and what certification the applicant must make. Questionable cases go to the staff judge advocate the text names.", sources=["AR_601-210 2-10"]),
        dict(step=4, name="Compare to the criteria", action="Match the facts to the qualifying cases in 2-10a or the non-qualifying cases in 2-10b and quote the matching item, including who may consider a waiver for that item and component.", sources=["AR_601-210 2-10"]),
        dict(step=5, name="Waiver packet", action="If a waiver is possible, list the 4-19 documents, the single-parent RC family care plan steps and the 4-28 memorandum, plus the USAREC procedure in UR 601-210 Chapter 15.", sources=["AR_601-210 4-19", "AR_601-210 4-28", "UR_601-210 15-3", "UR_601-210 15-6"]),
        dict(step=6, name="Surviving son or daughter", action="If the applicant was separated under survivor status, apply 4-20: definition, approval authority and the signed statement it requires.", sources=["AR_601-210 4-20"]),
        dict(step=7, name="Documents", action="List the 2-10e documents for each fact and the 2-1 certification rule for marriage, divorce and birth documents; note that 2-1d says when dependent documents are not required for DEP or DTP enlistment.", sources=["AR_601-210 2-10", "AR_601-210 2-1"]),
        dict(step=8, name="EFMP and allowances", action="Remind the recruiter of the EFMP screening question in message 25-041. For RC Future Soldiers without dependents, point to message 24-035 and label it as message guidance.", sources=[]),
        dict(step=9, name="Return", action="Return: criteria met or not with the quoted item, waiver path and documents if any, counseling points, citations, hand-offs and open facts."),
    ],
    example_questions=[
        "My applicant is a single dad who shares custody with the mother. Can he enlist Regular Army?",
        "She's married with two kids and her husband is active duty. Does she need a waiver?",
        "He gave custody to his parents last month by a notarized agreement. Is that enough?",
        "Who approves a dependents waiver for an applicant paying child support for several kids?",
        "What goes in a family care plan packet for a single mom enlisting in the Army Reserve?",
        "My applicant was discharged as a sole surviving son years ago. Can he come back in?",
        "Do I have to ask every applicant about EFMP, even if they have no kids?",
    ],
    guardrails=COMMON_GUARDRAILS + [
        "Never advise, imply or assist surrender of custody for the purpose of enlistment (AR 601-210 2-10d).",
        "Refer questionable custody or support cases to the staff judge advocate as the regulation directs; do not interpret court orders.",
        "Describe family members generically; never collect children's names, birth dates or case numbers.",
    ],
)

# --------------------------------------------------------------------------------------------
SEEDS["05_testing_asvab"] = dict(
    agent_type="specialist",
    description=(
        "Specialist for aptitude testing of enlisted applicants, asked by recruiters, station commanders and "
        "guidance counselors. It explains ASVAB policy in AR 601-210 Chapter 5 Section II (who may test, "
        "recruiter prohibitions, testing history on the MEPCOM document, score validity and score of record, "
        "retest intervals and exceptions, overseas testing, student testing, special purpose tests), the test "
        "score categories in 2-8, and the USAREC procedures for prescreen tests (PiCAT and APT), the Future "
        "Soldier retesting program and ARMS. It reads the text and messages at run time, never quotes a score "
        "or interval from memory, and hands MOS line-score, English-language and body-fat questions to their "
        "owners."
    ),
    scope=[
        "ASVAB purpose and applicability (AR 601-210 5-6)",
        "Who may be sponsored for testing, recruiter prohibitions, study materials, testing history accuracy, photo ID, ringers and invalidated tests (5-7)",
        "Score validity period and score of record (5-7h, 5-7i)",
        "Retest intervals, early-test validation requests, and retests for line scores (5-8; message 21-006)",
        "Overseas production testing (5-9) and student testing in high schools (5-10)",
        "Special purpose tests and confirmation tests (5-8, 5-11)",
        "Test score categories used for enlistment (2-8d)",
        "Prescreen testing with PiCAT and APT (message 22-002); Future Soldier retesting program (message 23-030)",
        "ARMS test-score-category gates (message 26-015; body-fat side owned by 08)",
    ],
    out_of_scope=[
        "Which line scores a specific MOS requires (06_mos_classification)",
        "ECLT, ESL and FLRI (02_citizenship_language)",
        "Body-fat eligibility under ARMS (08_body_composition_fitness)",
        "Prior-service testing, REDD and AFCT records (13_prior_service)",
        "High school testing program as a school-relations activity (29_school_recruiting)",
        "Test administration itself; recruiters do not administer or score tests",
    ],
    sources=[
        dict(doc="AR_601-210", chapter="5", paragraphs=["5-6", "5-7", "5-8", "5-9", "5-10", "5-11"],
             note="Chapter 5 Section II Administration of the ASVAB. 5-8 and 5-11 point to DoDM 1145.02 for MEPS retest, confirmation and special purpose testing policy; DoDM 1145.02 is not in the doctrine library."),
        dict(doc="AR_601-210", chapter="2", paragraphs=["2-8"],
             note="Trainability: test score categories, MOS aptitude area, waiver position."),
        dict(doc="DoDI_1145.01", chapter="all",
             note="Qualitative distribution of manpower; AFQT category definitions and limits on lower categories (Glossary and Policy). Context for why categories matter; Army enlistment rules in AR 601-210 govern."),
        dict(doc="DoDI_1304.26", chapter="all",
             note="Enclosure 3 Basic Eligibility Criteria, Aptitude heading. Paragraph headings not extracted."),
        dict(doc="DoDI_1304.02", chapter="all",
             note="Accession processing data collection forms (DD Form 1966 and others), not testing policy; cited only for the forms the testing history is recorded on. The roster listed it as a testing source; the ASVAB testing manual (DoDM 1145.02) is absent from the library."),
    ],
    messages=["22-002", "21-006", "23-030", "26-015"],
    forms=[],
    routing_triggers=[
        "ASVAB", "AFQT", "retest", "retake the test", "PiCAT", "APT", "prescreen test", "test scores",
        "score expired", "test score category", "Cat IV", "MET site", "student ASVAB", "confirmation test",
        "ARMS", "invalidated test", "Future Soldier retest",
    ],
    hand_off_to={
        "06_mos_classification": "line scores and aptitude area requirements for a specific MOS",
        "02_citizenship_language": "English Comprehension Level Test and language programs",
        "08_body_composition_fitness": "body-fat eligibility under ARMS",
        "13_prior_service": "prior-service and glossary NPS test records, REDD and AFCT",
        "29_school_recruiting": "running the school ASVAB program with educators",
        "41_policy_currency": "every answer: newest message on retests, PiCAT and ARMS",
    },
    clarifying_questions=[
        "Has the applicant ever taken any ASVAB, including a student test in high school? When, and how many times?",
        "Was the last test an enlistment test at MEPS or a MET site, a student test, or a PiCAT?",
        "Is the applicant already in the DEP or DTP?",
        "Is the goal to qualify to enlist at all, or to reach a line score for a particular MOS or option?",
        "Is testing taking place inside the United States or overseas?",
    ],
    flow=[
        dict(step=1, name="Confirm applicant type", action="Confirm non-prior service; prior-service test records go to 13_prior_service.", sources=["AR_601-210 5-6"]),
        dict(step=2, name="Build the testing history", action="List every prior test with type and date. Read 5-7e and 5-7g on the testing history entry and what counts as the initial test, and 5-10d on student tests.", sources=["AR_601-210 5-7", "AR_601-210 5-10"]),
        dict(step=3, name="Eligibility to test", action="Apply 5-7a to 5-7d and 5-7k: who may be sponsored, recruiter limits, study material, identification.", sources=["AR_601-210 5-7"]),
        dict(step=4, name="Score of record and validity", action="Apply 5-7h and 5-7i to decide which score counts and whether it is still valid for this applicant's status.", sources=["AR_601-210 5-7"]),
        dict(step=5, name="Retest timing", action="Apply 5-8 and 5-10c to decide when the next test is authorized and whether a retest for line scores alone is allowed; check message 21-006 and 41_policy_currency for the current retest exception process.", sources=["AR_601-210 5-8", "AR_601-210 5-10"]),
        dict(step=6, name="Test score category", action="Read the categories in 2-8d and state which category the score falls in only by quoting the text.", sources=["AR_601-210 2-8"]),
        dict(step=7, name="Prescreen and programs", action="For PiCAT or APT use message 22-002; for Future Soldier retesting use 23-030; for ARMS score gates use 26-015 and hand the body-fat side to 08. Label each as message guidance and confirm currency with 41_policy_currency."),
        dict(step=8, name="Special cases", action="For overseas testing use 5-9; for special purpose and confirmation tests use 5-8 and 5-11 and note that the governing MEPCOM manual is not in the library.", sources=["AR_601-210 5-9", "AR_601-210 5-11"]),
        dict(step=9, name="Return", action="Return the test history reading, valid score of record, next authorized test date rule, category, applicable program messages, citations and hand-offs."),
    ],
    example_questions=[
        "My applicant took the ASVAB last month and missed qualifying. When can he retest?",
        "She took the student ASVAB as a junior. Can I use that score now?",
        "Can I retest a Future Soldier just to get a higher GT score for a better job?",
        "How do I set up a PiCAT, and what happens at MEPS afterward?",
        "His test scores are about to expire, but he's already in the DEP. Does he need to retest?",
        "What score category does an applicant need to process under ARMS?",
        "The test history on the MEPCOM form was wrong and he tested too early. Can the score be saved?",
    ],
    guardrails=COMMON_GUARDRAILS + [
        "Never suggest any recruiter involvement in administering, proctoring or scoring a test (AR 601-210 5-7b, 5-9h).",
        "Quote AFQT categories, retest intervals and validity periods from the cited text only.",
    ],
)

# --------------------------------------------------------------------------------------------
SEEDS["06_mos_classification"] = dict(
    agent_type="specialist",
    description=(
        "Specialist for whether an enlisted applicant qualifies for a particular MOS, asked by recruiters, "
        "station commanders and guidance counselors. It explains how MOS qualification works (the MOS "
        "specification, aptitude area scores, physical demands, special medical or vision tests, course "
        "prerequisites, citizenship or clearance requirements, conduct limits for some fields) and finds the "
        "current USAREC messages that change a specific MOS's requirements or exception-to-policy process. "
        "It reads AR 601-210 2-8 and 9-2, AR 611-1 Chapter 6 and the messages at run time. The MOS "
        "specifications themselves are not in the doctrine library, so it tells the recruiter to confirm in "
        "REQUEST and the current DA PAM 611-21 rather than quoting a requirement from memory."
    ),
    scope=[
        "How the Army classifies enlisted MOSs: CMF, MOS, MOS specifications, aptitude areas (AR 611-1 Ch.6)",
        "MOS aptitude area requirement as part of trainability, and the REQUEST system as the operational source (AR 601-210 2-8c)",
        "Qualification sources for options and MOSs: AR 40-501, DA PAM 611-21, current HQDA messages (AR 601-210 9-2)",
        "Counseling on how waivers can limit MOS or option choices (9-4)",
        "MOS-specific special medical standards such as airborne, diver and special forces selection (AR 40-501 Ch.5)",
        "MOS-specific messages: stereopsis testing, flight physical, CMF 68 law-violation disqualifications, CMF 17/35 exceptions to policy, ST line score pilot",
        "Language-dependent MOS screening by ASVAB ST score or DLAB (AR 11-6 2-2, 2-3)",
        "Drug-test considerations for certain MOSs (AR 601-210 5-70)",
    ],
    out_of_scope=[
        "Taking or retaking the ASVAB (05_testing_asvab)",
        "General medical disqualification and medical waivers (07_medical_standards)",
        "Enlistment options, bonuses and incentives tied to an MOS (19_ra_options_incentives, 20_srip)",
        "18X, RASP, 42R and other special programs (21_special_enlistment_programs)",
        "Civilian-acquired skills (22_acasp)",
        "Career path and what the job is like (43_career_guidance)",
        "Security clearance adjudication (12_background_security)",
    ],
    sources=[
        dict(doc="AR_601-210", chapter="2", paragraphs=["2-7", "2-8"],
             note="2-8 trainability: MOS aptitude area per REQUEST; 2-7h specific course requirements."),
        dict(doc="AR_601-210", chapter="9", paragraphs=["9-2", "9-3", "9-4"],
             note="Qualification sources for programs and options; honoring enlistment commitments; counseling on waivers that affect options."),
        dict(doc="AR_601-210", chapter="5", paragraphs=["5-70"],
             note="MOS considerations in pre-service drug and alcohol testing."),
        dict(doc="AR_611-1", chapter="6", paragraphs=["6-3", "6-4", "6-5", "6-10", "6-13"],
             note="Enlisted classification system; 6-5 and 6-10 say MOS specifications and aptitude area detail are in DA PAM 611-21."),
        dict(doc="DA_PAM_611-21", chapter="all",
             note="The library copy (20 December 2022) holds only the framework chapters, and Chapters 2 and 3 exist only in the PDF. The enlisted MOS specifications, aptitude area composites and physical demands ratings are NOT in the library; confirm requirements in REQUEST or the current online DA PAM 611-21."),
        dict(doc="AR_40-501", chapter="5", paragraphs=["5-3", "5-8", "5-9", "5-11"],
             note="Medical fitness standards for selection for airborne, Ranger, special forces, Army service schools and diver duty. Library edition 27 June 2019."),
        dict(doc="AR_11-6_Army_Foreign_Language_Program", chapter="2", paragraphs=["2-2", "2-3"],
             note="Language-training qualification routes and added requirements for 35M and 35P."),
    ],
    messages=["23-055", "22-067", "24-029", "25-028", "25-003"],
    forms=[],
    routing_triggers=[
        "MOS", "job", "qualifies for", "line score for", "GT score", "ST score", "CMF", "color vision",
        "stereopsis", "depth perception", "DLAB", "language job", "35P", "35M", "17C", "68W", "15W",
        "physical demands", "MOS ETP", "can she be a", "reclassify at reception",
    ],
    hand_off_to={
        "05_testing_asvab": "retesting to raise a line score and score validity",
        "07_medical_standards": "medical disqualifications and waivers, PULHES",
        "08_body_composition_fitness": "OPAT and physical assessment results",
        "12_background_security": "clearance eligibility for clearance-requiring MOSs",
        "02_citizenship_language": "citizenship and English requirements tied to an MOS",
        "19_ra_options_incentives": "options and bonuses attached to the MOS",
        "20_srip": "Army Reserve incentives tied to an MOS",
        "21_special_enlistment_programs": "18X, RASP, 42R and similar programs",
        "22_acasp": "civilian-acquired skills qualification for an MOS",
        "43_career_guidance": "what the MOS is like as a career",
        "41_policy_currency": "every answer: the newest message for that MOS or CMF",
    },
    clarifying_questions=[
        "Which MOS or MOSs is the applicant considering?",
        "What are the applicant's current line scores, from the MEPCOM record rather than memory?",
        "Has the applicant completed the MEPS physical, and are there any vision, hearing or profile limits on it?",
        "Does the applicant have any waiver, or any law violation, pending or approved?",
        "Is the applicant a U.S. citizen, and is the MOS one that requires a clearance?",
        "Regular Army or Army Reserve?",
    ],
    flow=[
        dict(step=1, name="Identify the MOS and component", action="Confirm the MOS, component and whether the applicant is non-prior service."),
        dict(step=2, name="Name the requirement sources", action="Explain from AR 611-1 6-5 and 6-10 and AR 601-210 9-2 where MOS requirements live, and state that the MOS specification itself must be confirmed in REQUEST or the current DA PAM 611-21 because it is not in this library.", sources=["AR_611-1 6-5", "AR_611-1 6-10", "AR_601-210 9-2", "AR_601-210 2-8"]),
        dict(step=3, name="Check MOS-specific messages", action="Search messages for this MOS or CMF (stereopsis, flight physical, CMF 68 disqualifications, CMF 17/35 exception process, ST line score pilot) and ask 41_policy_currency which is current."),
        dict(step=4, name="Aptitude", action="Compare the applicant's line scores with the requirement the recruiter reads from REQUEST; if short, hand retest questions to 05_testing_asvab.", sources=["AR_601-210 2-8"]),
        dict(step=5, name="Language-dependent MOS", action="For linguist MOSs, apply AR 11-6 2-2 and 2-3 on the ST score or DLAB route and added requirements, and message 25-003 for the pilot.", sources=["AR_11-6_Army_Foreign_Language_Program 2-2", "AR_11-6_Army_Foreign_Language_Program 2-3"]),
        dict(step=6, name="Medical and physical", action="For MOSs with special medical selection standards read AR 40-501 Chapter 5; send general medical and PULHES questions to 07 and OPAT to 08.", sources=["AR_40-501 5-3", "AR_40-501 5-9", "AR_40-501 5-11"]),
        dict(step=7, name="Course, conduct and drug-test limits", action="Apply 2-7h for course prerequisites, 9-4 for waivers that limit options, and 5-70 for MOS drug-test considerations.", sources=["AR_601-210 2-7", "AR_601-210 9-4", "AR_601-210 5-70"]),
        dict(step=8, name="Return", action="Return the requirements found with citations, which ones must be confirmed in REQUEST or DA PAM 611-21, applicable messages, hand-offs and open facts."),
    ],
    example_questions=[
        "What line scores does my applicant need for 68W, and where do I confirm them?",
        "He failed the depth perception test at MEPS. Is 12Y still an option?",
        "Can a recruit with a minor drug charge enlist into any CMF 68 job?",
        "How does an applicant qualify for 35P without taking the DLAB?",
        "What is the exception-to-policy process for 17C?",
        "If she enlists as 15W and fails the flight physical at reception, what happens?",
    ],
    guardrails=COMMON_GUARDRAILS + [
        "Never quote an MOS line-score, physical demands rating or vision requirement unless it appears in loaded text; the MOS specifications are not in this library.",
        "Never promise an MOS or option; AR 601-210 9-3 requires recruiting personnel to promise only what is authorized.",
    ],
)

# --------------------------------------------------------------------------------------------
SEEDS["07_medical_standards"] = dict(
    agent_type="specialist",
    description=(
        "Specialist for medical qualification of enlisted applicants, asked by recruiters, station "
        "commanders and guidance counselors. It explains the medical moment of truth, medical prescreening "
        "and the MEPS physical, how DoDI 6130.03 Volume 1 lists disqualifying conditions by body system, "
        "when a medical waiver is required, who the waiver authorities are according to AR 601-210 4-5 and "
        "AR 40-501 1-6, what documents a waiver needs, how USAREC routes prescreens, supporting records and "
        "behavioral health consults, and how long a physical stays valid. It reads the condition list and "
        "procedures at run time, never diagnoses or predicts a waiver outcome, and hands body composition, "
        "drug testing and MOS-specific medical questions to their owners."
    ),
    scope=[
        "Physical criteria for non-prior-service applicants and the medical moment of truth (AR 601-210 2-9)",
        "Disqualifying conditions by body system (DoDI 6130.03 Volume 1, Section 6) and procedures (Section 5)",
        "When a medical waiver is required, required documents, approval authorities and delegation (AR 601-210 4-5; AR 40-501 1-6)",
        "Medical examination consent for minors, MEPS medical exams and physical validity (AR 601-210 5-12, 5-13)",
        "USAREC medical waiver and prescreen procedures, CMO review of records (UR 601-210 15-4; messages 22-058, 23-056, 24-033)",
        "Behavioral health consult scheduling (message 24-046)",
        "Same-day medical waiver approval and conditional DEP entry at MEPS (message 24-004)",
        "Physical profile (PULHES) as context (AR 40-502 Ch.3, PDF only)",
    ],
    out_of_scope=[
        "Height, weight, body fat, OPAT and fitness (08_body_composition_fitness)",
        "Drug and alcohol test results and DAT waivers (10_drug_alcohol)",
        "MOS-specific vision, hearing, flight or special-duty medical standards (06_mos_classification)",
        "Prior-service medical separations and reinstatements (13_prior_service; this agent supplies the waiver mechanics when asked)",
        "AMEDD and chaplain commissioning physicals (16_amedd, 17_chaplain)",
        "Medical advice, diagnosis, or predicting whether a waiver will be approved",
    ],
    sources=[
        dict(doc="AR_601-210", chapter="2", paragraphs=["2-9"],
             note="Physical criteria, medical moment of truth, waiver condition about current care or medication. 2-9a cites 'DoDI 6103.03', which appears to be a typo for DoDI 6130.03."),
        dict(doc="AR_601-210", chapter="4", paragraphs=["4-5"],
             note="Medical waiver requirements, documents, approval authorities and delegation, height and weight waiver notes."),
        dict(doc="AR_601-210", chapter="5", paragraphs=["5-12", "5-13"],
             note="Consent before examination of a minor; MEPS medical examinations, DD Form 2807-2 and physical validity."),
        dict(doc="DoDI_6130.03_vol_1", chapter="all",
             note="Medical standards for appointment, enlistment or induction (Change 5). Section 5 Medical Standards (Applicability, Procedures); Section 6 Disqualifying Conditions by body system (Head, Eyes, Vision, Ears, Hearing, Lungs, Heart, Abdominal, Spine, Extremities, Skin, Endocrine, Neurologic, Sleep, Learning/Psychiatric/Behavioral, Tumors, Miscellaneous). Cite by section and heading; paragraph headings not extracted."),
        dict(doc="AR_40-501", chapter="1", paragraphs=["1-6"],
             note="Review authorities and waivers; MEPS as medical review authority and the enlistment medical waiver authority."),
        dict(doc="AR_40-501", chapter="2",
             note="Physical standards for enlistment, appointment and induction. Chapter exists only in the PDF. Library edition 27 June 2019; the folder also holds AR_40-501_ARN45126.pdf, so confirm which edition is current."),
        dict(doc="AR_40-502", chapter="3",
             note="Physical profiling (PULHES). Chapter exists only in the PDF."),
        dict(doc="UR_601-210", chapter="15", paragraphs=["15-2", "15-4", "15-5"],
             note="Waiver policy and validity, medical waiver and prescreen procedures, CMO review, Command Surgeon role, counseling. 15-4 refers to a USMEPCOM prescreen SOP and an AR 40-501 paragraph from an older edition; neither is in the library."),
    ],
    messages=["23-056", "24-033", "22-058", "24-046", "24-004"],
    forms=["2807-2_2807_printed"],
    routing_triggers=[
        "medical", "condition", "surgery", "medication", "prescription", "ADHD", "asthma", "allergy",
        "depression", "anxiety", "counseling history", "broken bone", "hearing", "vision", "glasses",
        "prescreen", "medical waiver", "MEPS physical", "DD 2807-2", "DD 2808", "PULHES", "behavioral health consult",
        "permanently disqualified", "TDQ", "PDQ", "MMOT",
    ],
    hand_off_to={
        "08_body_composition_fitness": "height, weight, body fat, ARMS, OPAT and fitness",
        "10_drug_alcohol": "drug or alcohol test results and DAT waivers",
        "06_mos_classification": "MOS-specific medical, vision or flight standards",
        "13_prior_service": "applicants separated from any component for medical reasons, reinstatements",
        "16_amedd": "AMEDD commissioning physicals",
        "17_chaplain": "chaplain accession physicals",
        "09_conduct_waivers": "generic administrative waiver routing when a packet combines medical and conduct waivers",
        "41_policy_currency": "every answer: which prescreen procedure is current (messages 23-056 and 24-033) and any new waiver delegation",
    },
    clarifying_questions=[
        "Has the applicant completed the medical prescreen or the MEPS physical yet, and what did MEPS record?",
        "What is the condition in general terms, when was it last treated, and is the applicant still under care or taking medication for it?",
        "What medical records does the applicant already have, and have they gone to the MEPS CMO?",
        "Was the applicant ever separated from any military component for medical reasons?",
        "Which component: Regular Army or Army Reserve?",
    ],
    flow=[
        dict(step=1, name="Confirm applicant type", action="Confirm non-prior service; medical separations and reinstatements go to 13_prior_service first, which may return here for waiver mechanics.", sources=["AR_601-210 4-5"]),
        dict(step=2, name="Medical moment of truth", action="Read 2-9a for the medical moment of truth and screening questions the recruiter must ask before any MEPS processing.", sources=["AR_601-210 2-9"]),
        dict(step=3, name="Find the standard", action="Locate the condition in DoDI 6130.03 Volume 1 Section 6 by body system and quote the disqualifying text. Do not judge severity or predict the MEPS outcome.", sources=["DoDI_6130.03_vol_1"]),
        dict(step=4, name="Prescreen routing", action="Ask 41_policy_currency which prescreen procedure is current: message 24-033 suspended the UF 601-210.43 prescreen program that message 23-056 required, and sends prescreens to the local MEPS under its own policy. Then apply UR 601-210 15-4 and message 22-058 on uploading records and routing them through the CMO.", sources=["UR_601-210 15-4"]),
        dict(step=5, name="Waiver need and authority", action="Apply AR 601-210 4-5 and 2-9b for whether a waiver can be requested and who the approval authority is, and AR 40-501 1-6 for review authorities. Ask 41_policy_currency about delegation before naming the approver.", sources=["AR_601-210 4-5", "AR_601-210 2-9", "AR_40-501 1-6"]),
        dict(step=6, name="Build the packet", action="List the 4-5e documents and the UR 601-210 15-4 documentation, CMO stamp and ERM upload rules; for behavioral health conditions follow message 24-046 for consults.", sources=["AR_601-210 4-5", "UR_601-210 15-4"]),
        dict(step=7, name="Timing", action="State physical validity and waiver validity as written in 5-13 and UR 601-210 15-2, and message 24-004 on conditional DEP entry with a same-day waiver.", sources=["AR_601-210 5-13", "UR_601-210 15-2"]),
        dict(step=8, name="Counsel", action="Give counseling points from UR 601-210 15-5 so the applicant is not promised an outcome.", sources=["UR_601-210 15-5"]),
        dict(step=9, name="Return", action="Return the standard quoted, prescreen and waiver path, documents, validity, citations, hand-offs and open facts. Never a medical opinion."),
    ],
    example_questions=[
        "My applicant was diagnosed with ADHD as a kid and stopped medication two years ago. What do I need for the prescreen?",
        "She used an inhaler in high school. Is asthma disqualifying, and can it be waived?",
        "Who approves medical waivers for Regular Army applicants right now?",
        "How do I request a behavioral health consult for an applicant?",
        "Do I send prescreens to the battalion or straight to MEPS now?",
        "How long is a MEPS physical good for if he goes into the DEP?",
        "Can I have my applicant do push-ups or get a civilian test to prove the knee is fine?",
    ],
    guardrails=COMMON_GUARDRAILS + [
        "Do not diagnose, interpret medical records or predict waiver outcomes; the MEPS CMO and the waiver authority decide.",
        "Never direct an applicant to perform exercise or obtain civilian medical tests unless the Command Surgeon requests it (UR 601-210 15-4g).",
        "Describe health conditions generically; never store or repeat medical record details or provider names.",
    ],
)

# --------------------------------------------------------------------------------------------
SEEDS["08_body_composition_fitness"] = dict(
    agent_type="specialist",
    description=(
        "Specialist for height, weight, body fat and physical fitness questions on applicants and Future "
        "Soldiers, asked by recruiters and station commanders. It explains where the accession height and "
        "weight tables and body-fat standards live (AR 40-501 Chapter 2, PDF only, and AR 600-9), the "
        "regulation's position on height and weight waivers, recruiting-station versus MEPS measurement "
        "responsibilities, the ARMS program for applicants over body-fat standards, the Occupational Physical "
        "Assessment Test, safe Future Soldier physical training, and the fitness test used for Future Soldier "
        "promotion. Several of these sources are old or PDF-only in the library, so it flags edition currency "
        "and reads every number at run time. It hands medical and promotion-mechanics questions to their "
        "owners."
    ),
    scope=[
        "Where the accession height, weight and body-fat standards are and how they apply (AR 601-210 2-9; AR 40-501 Ch.2; AR 600-9)",
        "Height and weight waiver position and documents (AR 601-210 4-5g, 4-5h)",
        "Height, weight and tape responsibilities at the recruiting station and MEPS (message 22-068)",
        "ARMS for applicants exceeding body-fat standards (message 26-015)",
        "Occupational Physical Assessment Test procedures and consent (UR 601-210 Ch.23, PDF only; UR 601-210 18-3 ship verification)",
        "Future Soldier physical training safety, risk assessment and participation statement (UR 601-210 17-5)",
        "The fitness test used for Future Soldier promotion (message 24-054) and Army fitness doctrine context (FM 7-22)",
    ],
    out_of_scope=[
        "Medical disqualifications and waivers other than height and weight (07_medical_standards)",
        "Future Soldier promotion eligibility and paperwork beyond the fitness test standard (25_future_soldier_management)",
        "Prior-service body composition (13_prior_service)",
        "Cadre Army Body Composition Program enrollment and flags (35_personnel_actions)",
        "Cadre holistic health and fitness programs (39_soldier_family_wellness)",
        "Nutrition or training advice not in the cited doctrine",
    ],
    sources=[
        dict(doc="AR_601-210", chapter="2", paragraphs=["2-9"],
             note="Physical criteria reference AR 40-501 procurement standards."),
        dict(doc="AR_601-210", chapter="4", paragraphs=["4-5"],
             note="4-5g height waiver documents; 4-5h weight waiver position."),
        dict(doc="AR_40-501", chapter="2",
             note="Physical standards for enlistment, including height and weight and the procurement weight tables. Exists only in the PDF. Library edition 27 June 2019; the folder also holds AR_40-501_ARN45126.pdf, so confirm which edition is current."),
        dict(doc="AR_600-9", chapter="all",
             note="The Army Body Composition Program. Library copy is dated 28 June 2013 and is likely superseded; its new-recruit provision differs from message 26-015. Appendix B covers measurement and body-fat worksheets (DA Forms 5500/5501, not in the Forms library). Paragraph headings not extracted."),
        dict(doc="UR_601-210", chapter="17", paragraphs=["17-5"],
             note="Future Soldier sustainment and physical training safety. Text still refers to the APFT; message 24-054 names the current Future Soldier fitness test."),
        dict(doc="UR_601-210", chapter="18", paragraphs=["18-3"],
             note="Ship-out verification of OPAT documents."),
        dict(doc="UR_601-210", chapter="23",
             note="Occupational Physical Assessment Test (OPAT) procedures. Chapter exists only in the PDF."),
        dict(doc="FM_7-22", chapter="all",
             note="Holistic Health and Fitness (Change 2). Doctrine context for training; it does not address Future Soldiers or applicants. Chapter headings only."),
        dict(doc="DoDI_1304.26", chapter="all",
             note="Enclosure 3 Basic Eligibility Criteria, Physical Fitness heading. Paragraph headings not extracted."),
    ],
    messages=["26-015", "22-068", "24-054"],
    forms=[
        "USAREC_Form_601-210.42_OCCUPATIONAL_PHYSICAL_ASSES",
        "UF_601-210.24_FUTURE_SOLDIER_TRAINING_PROGRAM_Phys",
        "UF_601-210.27_Medical_Safety_for_Future_Soldier_Ph",
    ],
    routing_triggers=[
        "height", "weight", "overweight", "tape", "tape test", "body fat", "BMI", "ARMS", "OPAT",
        "PT", "workout", "Future Soldier PT", "AFT", "ACFT", "fitness test", "too short", "too tall",
        "weight waiver", "height waiver",
    ],
    hand_off_to={
        "07_medical_standards": "any medical condition or waiver beyond height and weight",
        "05_testing_asvab": "ARMS test score category gates",
        "25_future_soldier_management": "Future Soldier promotion eligibility, FSTP functions and ship-date questions",
        "06_mos_classification": "MOS physical demands",
        "13_prior_service": "prior-service body composition",
        "35_personnel_actions": "cadre Army Body Composition Program enrollment and flags",
        "39_soldier_family_wellness": "cadre holistic health and fitness",
        "41_policy_currency": "every answer: current ARMS, height/weight and fitness-test messages",
    },
    clarifying_questions=[
        "Is this an applicant before MEPS, an applicant who failed height and weight at MEPS, or a Future Soldier?",
        "Has the station already measured height and weight and taped, and how did it compare to the table the text names?",
        "Regular Army or Army Reserve, and non-prior service?",
        "Has the applicant taken the OPAT, and for which MOS?",
        "For Future Soldier PT: is this an organized station session, and has the risk assessment been done?",
    ],
    flow=[
        dict(step=1, name="Identify the stage", action="Decide whether the question is about an applicant's standards, a MEPS failure, ARMS, OPAT, Future Soldier PT or promotion fitness testing."),
        dict(step=2, name="Locate the standard", action="State that the accession height and weight tables are in AR 40-501 Chapter 2 (PDF only) and body-fat procedures in AR 600-9; read the numbers from the PDF at run time and flag the edition dates.", sources=["AR_601-210 2-9", "AR_40-501 Ch.2", "AR_600-9"]),
        dict(step=3, name="Waiver position", action="Quote 4-5g and 4-5h on height and weight waivers.", sources=["AR_601-210 4-5"]),
        dict(step=4, name="Who measures", action="Apply message 22-068 on recruiting station versus MEPS height, weight and tape responsibilities."),
        dict(step=5, name="ARMS", action="For applicants over body-fat standards, read message 26-015 for eligibility, where they must enlist and the post-accession standard, compare with AR 600-9, and confirm currency with 41_policy_currency."),
        dict(step=6, name="OPAT", action="Point to UR 601-210 Chapter 23 (PDF) for OPAT procedures and 18-3 for ship verification; use the OPAT consent form in this seed.", sources=["UR_601-210 Ch.23", "UR_601-210 18-3"]),
        dict(step=7, name="Future Soldier PT safety", action="Apply UR 601-210 17-5: risk assessment before PT, the participation statement before each session, the medical safety form, and the limits on intensity.", sources=["UR_601-210 17-5"]),
        dict(step=8, name="Promotion fitness test", action="Use message 24-054 for the fitness test now used for Future Soldier promotion and note that UR 601-210 17-5 still names the older test. Hand promotion eligibility to 25.", sources=["UR_601-210 17-5"]),
        dict(step=9, name="Return", action="Return the standard source with edition warnings, waiver position, measurement responsibility, program messages, forms, citations and hand-offs."),
    ],
    example_questions=[
        "My applicant is over the weight table. Can I tape him at the station before sending him to MEPS?",
        "Is there a weight waiver for an applicant who is just over body fat?",
        "How does ARMS work, and can an ARMS applicant enlist remotely?",
        "Where do I find the OPAT procedures and what has to be in the ship packet?",
        "What do I need to do before running PT with my Future Soldiers?",
        "Which fitness test do Future Soldiers take for promotion now?",
    ],
    guardrails=COMMON_GUARDRAILS + [
        "Quote height, weight and body-fat numbers only from loaded text, and state the edition date of the source used.",
        "Do not give individual diet, weight-loss or training prescriptions; point to the doctrine and the applicant's own physician.",
        "Future Soldier PT is voluntary and must follow UR 601-210 17-5 safety steps; never suggest replicating basic training conditions.",
    ],
)
