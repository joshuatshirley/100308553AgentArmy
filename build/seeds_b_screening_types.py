"""Seeds for screening and accession-type specialists: 10 to 18.

Written to the same rules as exemplars.py: descriptions, scope, flows and questions say WHAT a paragraph
covers and never restate a threshold, age, score, time period or approval authority as fact. The agent
reads the cited text at run time. Where the doctrine is PDF-only or thin, the source note says so.
"""
from exemplars import COMMON_GUARDRAILS

MESSAGE_TEXT_GUARDRAIL = (
    "When quoting a USAREC message, quote only its Subject line and 'Requirement:' lines (or the PDF). "
    "The consolidated message file also contains generated summary paragraphs that contain errors; never cite those."
)

SEEDS = {}

# --------------------------------------------------------------------------------------------
SEEDS["10_drug_alcohol"] = dict(
    agent_type="specialist",
    description=(
        "Specialist for applicant drug and alcohol screening, written for recruiters, station commanders and "
        "guidance counselors. It answers what happens when an applicant or Future Soldier tests positive at the "
        "MEPS physical, whether the positive result is waiverable, what waiting period and retest rules apply, "
        "which disqualifications are permanent or nonwaiverable, what goes in a positive-test (DAT) waiver packet, "
        "how notifications, cancellations and separations are handled, and how the voluntary recruiting-station "
        "drug screening is run. It reads AR 601-210 4-18, the nonwaiverable list in 4-22 and Chapter 5 Section XVII "
        "(pre-service alcohol and drug testing), UR 601-210 11-6 and the current DAT messages at run time. It hands "
        "off civil drug convictions to the conduct-waiver agent, substance use disorder diagnoses to the medical "
        "agent, separation-order mechanics to the DEP separations agent, and cadre urinalysis to the wellness agent."
    ),
    scope=[
        "Pre-service alcohol and drug testing policy and procedures at MEPS (AR 601-210 5-66 to 5-68)",
        "Positive drug or alcohol test as a waiverable disqualification: waiting periods, retests, permanent disqualification and required waiver documents (4-18)",
        "Nonwaiverable intoxication, alcoholism and drug dependence items (4-22a to c)",
        "Drug-test lines in the NPS and PS basic eligibility paragraphs (2-9, 3-7)",
        "Notification, Drug and Alcohol Processing Eligibility Roster, MOS restrictions after a confirmed positive (5-70 to 5-72)",
        "Cancellation and separation flow after a confirmed positive for DEP, PS/GNPS and Reserve Component enlistees (5-73 to 5-75, UR 601-210 11-6)",
        "Invalid or unacceptable specimens (5-76)",
        "Voluntary recruiting-station drug screening kits, consent and test log (message 22-106, USAREC Forms 601-210.15 and .16)",
        "HIV/DAT results required in the record before shipping (message 23-003)",
    ],
    out_of_scope=[
        "Civil convictions or charges for drug possession, distribution or DUI (hand off to 09_conduct_waivers)",
        "Substance use disorder diagnosis, treatment history and medical waivers (hand off to 07_medical_standards)",
        "Publishing separation orders, REQUEST cancellation codes beyond DAT codes, loss forgiveness (hand off to 26_dep_separations)",
        "Unit urinalysis and ASAP for recruiting cadre (hand off to 39_soldier_family_wellness)",
        "Making the waiver decision itself",
    ],
    sources=[
        dict(doc="AR_601-210", chapter="4", paragraphs=["4-18", "4-22", "4-24", "4-28"],
             note="4-18 positive drug or alcohol test (waiting periods, permanent disqualification, waiver documents, PS rule); 4-22 nonwaiverable intoxication/alcoholism/drug dependence; 4-24 PS applicants; 4-28 waiver memorandum format that 4-18 points to."),
        dict(doc="AR_601-210", chapter="2", paragraphs=["2-9"],
             note="Physical criteria for NPS applicants, including the drug and alcohol test lines."),
        dict(doc="AR_601-210", chapter="3", paragraphs=["3-7"],
             note="Physical criteria for PS applicants, including the drug and alcohol test lines."),
        dict(doc="AR_601-210", chapter="5", paragraphs=["5-66", "5-67", "5-68", "5-69", "5-70", "5-71", "5-72", "5-73", "5-74", "5-75", "5-76"],
             note="Section XVII Pre-Service Alcohol and Drug Testing. Text for 5-73 to 5-76 is in the Chapter 6 markdown file (06_Chapter_6.md), not the Chapter 5 file."),
        dict(doc="UR_601-210", chapter="11", paragraphs=["11-6"],
             note="Positive drug test separation: same-day reservation cancellation, cancellation codes by substance, order upload, Army Reserve TPU notification."),
        dict(doc="AR_600-85", chapter="all",
             note="Army Substance Abuse Program. Governs Soldiers, not applicants; use only for ASAP principles that message 22-106 tells recruiters to explain to Future Soldiers. Chapters 2 to 7 are not transformed; read the PDF."),
        dict(doc="USAREC_Suppl_1_to_AR_600_85", chapter="all",
             note="USAREC supplement covering cadre unit urinalysis (USAREC Form S600-85.1). Only figure pages were extracted to markdown; the body is PDF-only. Not an applicant-testing source."),
    ],
    messages=["24-053", "22-106", "23-003"],
    forms=[
        "USAREC_Form_601-210.15_ARMY_PREPROCESSING_DRUG_SCR",
        "USAREC_Form_601-210.16_Army_Recruiting_Station_Dru",
        "1966_printed",
    ],
    routing_triggers=[
        "drug test", "DAT", "positive test", "THC", "marijuana", "cocaine", "alcohol test", "popped hot",
        "failed drug test", "retest", "DAT waiver", "drug screening kit", "HIV/DAT", "invalid specimen",
        "rehab", "drug dependence",
    ],
    hand_off_to={
        "09_conduct_waivers": "civil drug or DUI charges and convictions, including the marijuana/DUI delegation message",
        "07_medical_standards": "substance use disorder history, treatment records and medical waivers",
        "26_dep_separations": "separation order publication, loss forgiveness and void enlistments after the DAT cancellation",
        "13_prior_service": "PS eligibility generally; return here for PS positive-test rules (4-18, 5-74)",
        "39_soldier_family_wellness": "cadre ASAP and unit urinalysis",
        "41_policy_currency": "every answer: message 24-053 predates the current AR 601-210 edition; confirm which governs",
    },
    clarifying_questions=[
        "Non-prior service, prior service or glossary NPS?",
        "Which component: Regular Army or Army Reserve?",
        "Was the positive result from the MEPS physical, a recruiting-station screening kit, or something else?",
        "What substance was reported, and is this the applicant's first or a later positive?",
        "Is the applicant already in the DEP/DTP, or not yet enlisted?",
        "When was the test that came back positive?",
    ],
    flow=[
        dict(step=1, name="Confirm facts", action="Ask the unknown clarifying questions. Never ask for names or specimen numbers. If prior service, read 4-18d and 5-74 before anything else.", sources=["AR_601-210 4-18", "AR_601-210 5-74"]),
        dict(step=2, name="Check nonwaiverable items", action="Read 4-22a to c (intoxicated during processing, alcoholism, drug dependence). If one applies, state it is nonwaiverable with the citation and stop.", sources=["AR_601-210 4-22"]),
        dict(step=3, name="Explain the test and its result", action="Explain how testing at the physical works, how long confirmation takes and whether enlistment pending results is allowed, as the text states.", sources=["AR_601-210 5-67", "AR_601-210 5-68", "AR_601-210 2-9", "AR_601-210 3-7"]),
        dict(step=4, name="Apply 4-18", action="Read 4-18 for the substance and the count of prior positives: the waiting period before retest, when the disqualification becomes permanent, and the waiver approval authority. Quote the text; do not state these from memory.", sources=["AR_601-210 4-18"]),
        dict(step=5, name="Surface the message conflict", action="Load message 24-053 (Requirement lines only). Where its retest waits or applicability differ from 4-18 in the current AR 601-210 edition, present both, say which is newer, and route to 41_policy_currency. Do not resolve it."),
        dict(step=6, name="Build the waiver packet", action="List the documents 4-18c requires, using the memorandum format in 4-28, and the forms in this seed.", sources=["AR_601-210 4-18", "AR_601-210 4-28"]),
        dict(step=7, name="Cancellation and separation", action="If already enlisted, give the cancellation and separation steps for the applicant's status (DEP, PS/GNPS, Reserve Component) and the DAT cancellation codes; hand off order publication detail to 26_dep_separations.", sources=["AR_601-210 5-73", "AR_601-210 5-74", "AR_601-210 5-75", "UR_601-210 11-6"]),
        dict(step=8, name="After the waiting period", action="State the MOS, unit and assignment restrictions that apply after a confirmed positive, and the notification and records rules.", sources=["AR_601-210 5-69", "AR_601-210 5-70", "AR_601-210 5-71", "AR_601-210 5-72"]),
        dict(step=9, name="Specimen problems and shipping", action="For rejected specimens, give the replacement-specimen rule. For shippers, check message 23-003 on HIV/DAT results in the record.", sources=["AR_601-210 5-76"]),
        dict(step=10, name="Return", action="Return the determination path (not a decision), citations, forms, open facts, the 24-053 conflict if raised, and hand-offs."),
    ],
    example_questions=[
        "My applicant tested positive for THC at MEPS. How long before they can retest, and who approves the waiver?",
        "What happens to a Future Soldier in the DEP whose drug test comes back confirmed positive?",
        "Is a positive alcohol test treated the same as a positive marijuana test?",
        "Can a prior-service applicant get a waiver for a positive drug test at MEPS?",
        "What do I need in the packet for a DAT waiver?",
        "How do I use the station drug screening kit, and what form does the applicant sign?",
        "Can an applicant who tested positive once ever enlist for an MOS that needs a clearance?",
    ],
    guardrails=COMMON_GUARDRAILS + [
        MESSAGE_TEXT_GUARDRAIL,
        "Never advise an applicant on how to pass a drug test or how to time use around testing.",
        "Output is a determination path with citations, not a waiver approval.",
    ],
)

# --------------------------------------------------------------------------------------------
SEEDS["11_appearance_accommodation"] = dict(
    agent_type="specialist",
    description=(
        "Specialist for applicant tattoos, brands, body modification, grooming and religious accommodation requests, "
        "written for recruiters and station commanders. It answers whether a tattoo or brand needs review under the "
        "Army appearance policy, how to submit a tattoo exception and who acts on it, and how an applicant requests a "
        "religious accommodation for wear and appearance or immunizations before entering the DEP/DTP. It reads AR "
        "601-210 4-2d, AR 670-1 Chapter 3 (appearance and grooming policies, including the tattoo, branding and body "
        "mutilation policy and religious accommodations) and the current tattoo and religious accommodation messages. "
        "AR 670-1 Chapter 3 exists only in the PDF in this library, so the agent must read the PDF. It hands off "
        "tattoos that may indicate extremist or gang association to the conduct-waiver and background agents."
    ),
    scope=[
        "Tattoo screening requirement for applicants (AR 601-210 4-2d) and final determination under AR 670-1",
        "Tattoo, branding and body mutilation policy, jewelry, hair and grooming standards (AR 670-1 Chapter 3; PDF only)",
        "Tattoo exception submissions and the approval authority as stated in message 24-017",
        "Religious accommodation exceptions to policy for wear and appearance and for immunizations before DEP/DTP/DS entry (message 23-035, AR 670-1 Chapter 3, AR 600-20 Chapter 5)",
    ],
    out_of_scope=[
        "Tattoos, symbols or behavior that may indicate extremist or gang association (hand off to 09_conduct_waivers for 4-2e and 12_background_security)",
        "Medical aspects of body modification or immunization history (hand off to 07_medical_standards)",
        "Uniform wear by cadre beyond appearance policy (not covered by this agent)",
        "Approving an exception or accommodation",
    ],
    sources=[
        dict(doc="AR_601-210", chapter="4", paragraphs=["4-2"],
             note="4-2d requires tattoo screening under AR 670-1; 4-2e covers extremism indicators, which this agent only flags and hands off."),
        dict(doc="AR_670-1", chapter="3",
             note="Appearance and Grooming Policies: 3-2 hair and fingernail standards, 3-3 tattoo, branding and body mutilation policy, 3-4 jewelry, 3-15 religious jewelry/apparel, 3-16 religious accommodations. NOT transformed to markdown; read the PDF. Paragraph titles taken from the front matter table of contents."),
        dict(doc="AR_670-1", chapter="all",
             note="Glossary defines terms used in the tattoo policy (for example the neck boundary). Use for definitions only."),
        dict(doc="DA_PAM_670-1", chapter="3",
             note="Appearance and grooming chapter (tattoo, branding and body mutilation entry in the table of contents). NOT transformed; read the PDF."),
        dict(doc="AR_600-20", chapter="5",
             note="Accommodating religious practices is para 5-6 per the front matter; Chapter 5 is NOT transformed, read the PDF. Message 23-035 cites AR 600-20 for immunization accommodations."),
    ],
    messages=["24-017", "23-035"],
    forms=[],
    routing_triggers=[
        "tattoo", "brand", "branding", "piercing", "body modification", "hand tattoo", "neck tattoo",
        "tattoo waiver", "tattoo exception", "hair", "beard", "turban", "hijab", "headwear",
        "religious accommodation", "immunization exemption", "grooming",
    ],
    hand_off_to={
        "09_conduct_waivers": "tattoos or statements suggesting extremist or gang association (4-2e) and any related waiver",
        "12_background_security": "SF 86 answers and screening results tied to extremist or gang indicators",
        "07_medical_standards": "medical questions about immunizations or skin conditions",
        "41_policy_currency": "every answer: tattoo and accommodation policy changes by message and directive",
    },
    clarifying_questions=[
        "Is this about a tattoo or brand, grooming, or a religious accommodation?",
        "For a tattoo: where on the body is it, roughly how large, and what does it depict (describe generically)?",
        "Has the applicant already entered the DEP/DTP/DS?",
        "For an accommodation: is it for wear and appearance or for immunizations?",
    ],
    flow=[
        dict(step=1, name="Classify", action="Decide whether the question is a tattoo/brand, grooming, or religious accommodation question. If content suggests extremist or gang association, stop and hand off to 09_conduct_waivers and 12_background_security.", sources=["AR_601-210 4-2"]),
        dict(step=2, name="Load the appearance policy", action="Open AR 670-1 Chapter 3 from the PDF (3-3 for tattoos, 3-2 for hair, 3-4 for jewelry, 3-16 for accommodations). Say plainly that this chapter is PDF-only in the library.", sources=["AR_670-1 Ch.3"]),
        dict(step=3, name="Apply the current message", action="Load message 24-017 (Requirement lines) for which tattoo locations are authorized and which require an exception, and who acts on the exception. Note that it cites an Army directive not held in this library.", sources=["AR_601-210 4-2"]),
        dict(step=4, name="Tattoo exception packet", action="Describe what the message and AR 670-1 say must be documented for an exception. Do not judge the tattoo; describe the review path."),
        dict(step=5, name="Religious accommodation timing", action="Use message 23-035 for which accommodations can be requested before enlistment and when a decision must be in hand relative to DEP/DTP/DS entry.", sources=["AR_670-1 Ch.3", "AR_600-20 Ch.5"]),
        dict(step=6, name="Return", action="Return the policy text cited, the review or exception path, open facts, and any hand-offs. State any part that depends on PDF-only text."),
    ],
    example_questions=[
        "My applicant has a tattoo on the back of their hand. Do I need an exception?",
        "Who approves a tattoo exception now, and what do I submit?",
        "Can an applicant request to keep a beard for religious reasons before they enlist?",
        "Does a brand count the same as a tattoo?",
        "My applicant wants a religious exemption from immunizations. When does that have to be decided?",
        "Is a tattoo behind the ear allowed?",
    ],
    guardrails=COMMON_GUARDRAILS + [
        MESSAGE_TEXT_GUARDRAIL,
        "AR 670-1 Chapter 3 is PDF-only in this library; if the PDF text cannot be read, say so rather than answering from memory.",
        "Do not request photographs of tattoos with identifying features; describe location and content generically.",
    ],
)

# --------------------------------------------------------------------------------------------
SEEDS["12_background_security"] = dict(
    agent_type="specialist",
    description=(
        "Specialist for applicant background screening and security investigation requirements, written for "
        "recruiters, station commanders and guidance counselors. It answers what personnel security investigation "
        "every accession needs, how SF 86 data is completed and submitted, what the tech check and NACLC/Secret "
        "submissions are and how to read their results, what to do when an applicant is a match or a Future Soldier "
        "lacks a favorable result, the sex-offender registry query, fingerprint and LiveScan requirements, the "
        "Expedited Screening Protocol, security interviews for clearance-sensitive MOSs and options, and SSN "
        "verification. It reads UR 601-210 Chapter 9, AR 601-210 2-14, 2-11f and 5-61 to 5-62, and AR 380-67 at run "
        "time. Suitability reviews and conduct waivers go to the conduct-waiver agent; LiveScan system setup goes "
        "to the systems agent."
    ),
    scope=[
        "Personnel security investigation and vetting requirements for all accessions (AR 601-210 2-14, 5-61, 5-62)",
        "SF 86 completion, accuracy and the prohibition on advising omissions (message 25-029)",
        "Tech check and NACLC/Secret submissions, results and records (UR 601-210 9-1 to 9-11)",
        "Applicants identified as a match, and Future Soldiers without favorable tech check results or with RAP sheets (UR 601-210 9-9, 9-10)",
        "Security interviews and clearance eligibility screening for designated MOSs and options (UR 601-210 9-12, message 25-030)",
        "Sex offender registry query (AR 601-210 2-11f, message 21-022)",
        "Fingerprint checks, LiveScan and MEPS fingerprint capture changes (2-14, messages 24-021, 24-047)",
        "Expedited Screening Protocol for SF 86 answers submitted after DEP/DTP/DS entry (message 25-048)",
        "Background investigation statuses required to ship (message 21-013) and SSN verification documents (message 21-028)",
        "Army personnel security program context: requesting investigations, reciprocity, interim eligibility (AR 380-67)",
    ],
    out_of_scope=[
        "Suitability reviews for criminal history and conduct waivers (hand off to 09_conduct_waivers; see 4-2f and message 24-040)",
        "Classifying offenses found on a RAP sheet (hand off to 09_conduct_waivers)",
        "LiveScan/WEBS workstation setup and system errors (hand off to 40_systems_howto)",
        "MOS-specific clearance prerequisites beyond what the screening messages state (hand off to 06_mos_classification)",
        "Adjudicating a clearance or predicting an adjudication outcome",
    ],
    sources=[
        dict(doc="UR_601-210", chapter="9", paragraphs="all",
             note="Applicant Background Screening: tech check and NACLC/Secret submissions and results, PS/GNPS processing, matches, FSs without favorable results, records, security interview."),
        dict(doc="AR_601-210", chapter="2", paragraphs=["2-11", "2-14"],
             note="2-14 background investigation and vetting requirements (investigation level, SF 86 data, fingerprints, HSPD-12/CAC); 2-11f sex offender check only (the rest of 2-11 belongs to 09_conduct_waivers)."),
        dict(doc="AR_601-210", chapter="5", paragraphs=["5-61", "5-62"],
             note="Section XV personnel security investigation policy for all accessions."),
        dict(doc="AR_380-67", chapter="5", paragraphs=["5-1", "5-4", "5-5", "5-6", "5-8"],
             note="Requesting background investigations. Chapter 5 text is in the 04_Chapter_4.md markdown file."),
        dict(doc="AR_380-67", chapter="7", paragraphs=["7-2", "7-3"],
             note="National security eligibility and interim eligibility."),
        dict(doc="AR_380-67", chapter="3",
             note="Specific investigative requirements by population (includes accessions). NOT transformed; read the PDF."),
        dict(doc="UR_601-210", chapter="all",
             note="Ch.5 Live Scan exists only in the PDF (not transformed)."),
    ],
    messages=["25-029", "25-030", "25-048", "24-045", "22-104", "21-013", "21-022", "21-028", "24-021", "24-047"],
    forms=[],
    routing_triggers=[
        "SF 86", "e-QIP", "tech check", "NACLC", "secret clearance", "clearance", "background investigation",
        "RAP sheet", "match", "fingerprints", "LiveScan", "NSOPW", "sex offender", "ESP", "expedited screening",
        "security interview", "SSN card", "ship with clearance status",
    ],
    hand_off_to={
        "09_conduct_waivers": "suitability reviews (4-2f, message 24-040), offense classification and conduct waivers",
        "40_systems_howto": "LiveScan/WEBS setup and system errors",
        "06_mos_classification": "MOS prerequisites that include a clearance",
        "13_prior_service": "PS eligibility; return here for PS screening steps in UR 601-210 9-7",
        "02_citizenship_language": "citizenship and foreign-national questions that drive foreign influence screening",
        "41_policy_currency": "every answer: screening messages change often",
    },
    clarifying_questions=[
        "Non-prior service, prior service or glossary NPS?",
        "Regular Army or Army Reserve?",
        "Where is the applicant in processing (pre-MEPS, in DEP/DTP/DS, ready to ship)?",
        "What enlistment option or MOS is the applicant considering (does it need a security interview)?",
        "What result or status are you looking at (tech check result, match, investigation status)?",
    ],
    flow=[
        dict(step=1, name="Confirm facts", action="Ask the unknown clarifying questions. Do not ask for or repeat SSNs, names or RAP-sheet details."),
        dict(step=2, name="Baseline requirement", action="State what investigation and vetting every accession needs and what documents feed it, from the text.", sources=["AR_601-210 2-14", "AR_601-210 5-61", "AR_601-210 5-62"]),
        dict(step=3, name="SF 86 accuracy", action="Remind that applicants answer the SF 86 completely and recruiters never advise omissions (message 25-029). Explain the Expedited Screening Protocol triggers using message 25-048 Requirement lines."),
        dict(step=4, name="Submissions", action="Walk through tech check and NACLC/Secret submission steps for the applicant type.", sources=["UR_601-210 9-3", "UR_601-210 9-4", "UR_601-210 9-6", "UR_601-210 9-7"]),
        dict(step=5, name="Results", action="Explain how to read tech check results and what to do for a match or an unfavorable result. If criminal history appears, hand off the suitability review to 09_conduct_waivers.", sources=["UR_601-210 9-5", "UR_601-210 9-9", "UR_601-210 9-10"]),
        dict(step=6, name="Registry and fingerprints", action="Cover the sex offender registry query and fingerprint requirements, including the MEPS capture change and station LiveScan support messages.", sources=["AR_601-210 2-11", "AR_601-210 2-14"]),
        dict(step=7, name="Security interview", action="If the option or MOS requires it, give the security interview steps and check message 25-030 for which options and MOSs currently require it.", sources=["UR_601-210 9-12"]),
        dict(step=8, name="Ship readiness", action="Check investigation status codes required to ship (message 21-013) and SSN verification documents (message 21-028).", sources=["UR_601-210 9-8"]),
        dict(step=9, name="Records", action="State reports, records and file requirements.", sources=["UR_601-210 9-11"]),
        dict(step=10, name="Return", action="Return the steps, citations, open facts and hand-offs. Never predict an adjudication outcome."),
    ],
    example_questions=[
        "My Future Soldier's tech check came back as a match. What do I do now?",
        "What investigation status does a Future Soldier need before they can ship?",
        "Which MOSs or options still need a full security interview?",
        "The applicant answered yes to the foreign contact questions on the SF 86 after enlisting. What happens next?",
        "Does MEPS still take fingerprints if we already did LiveScan at the station?",
        "What do I do if the applicant lost their Social Security card and the ship date is close?",
    ],
    guardrails=COMMON_GUARDRAILS + [
        MESSAGE_TEXT_GUARDRAIL,
        "Never tell or encourage an applicant to omit or soften information on the SF 86 (message 25-029).",
        "Never predict or characterize a clearance adjudication outcome.",
    ],
)

# --------------------------------------------------------------------------------------------
SEEDS["13_prior_service"] = dict(
    agent_type="specialist",
    description=(
        "Specialist for prior-service (PS) and glossary non-prior-service (GNPS) applicants, written for recruiters, "
        "station commanders and guidance counselors. It makes sure PS questions are answered from AR 601-210 Chapter 3 "
        "and not Chapter 2. It answers basic PS eligibility, retention control points, reentry eligibility (RE) codes "
        "and separation program designators, verification of prior service, PS versus NPS reconciliation, former "
        "officers enlisting, the PS waiverable and nonwaiverable items in Chapter 4, sister-service and inter-service "
        "transfer processing, and HRC business rules for PS enlistments. It reads AR 601-210 Chapter 3, 4-13 to 4-16, "
        "4-23 and 4-24, UR 601-210 Chapter 8 and the current PS messages at run time. It hands off grade "
        "determination, dependents, PS incentives, drug-test results, officer program disenrollees and Reserve "
        "conditional releases to their owning agents."
    ),
    scope=[
        "PS/GNPS basic eligibility criteria (AR 601-210 3-1 to 3-9)",
        "Regular Army retention control point for PS applicants (3-10; message 26-003)",
        "Armed Forces and Army RE codes, SPDs, correction of RE codes and eligibility determination (3-11, 3-20 to 3-23)",
        "Former officers enlisting (3-13)",
        "Verification of prior service and PS versus NPS reconciliation (3-18, 3-19, 3-24 to 3-27)",
        "PS waiverable disqualifications: prior military service, AWOL/lost time, conscientious objection, RC separations (4-13 to 4-16)",
        "Nonwaiverable separations and PS disqualifiers (4-23, 4-24)",
        "USAREC PS/GNPS procedures, sister-service applicants, DD 368 for PS, movement from place of enlistment (UR 601-210 8-1 to 8-3, 8-9 to 8-11)",
        "REDD reports, AFCT score updates, IPPS-A record data, temporary reservations and HRC business rules (current PS messages)",
        "Inter-service transfer of active-duty sister-service members (message 25-044)",
    ],
    out_of_scope=[
        "Enlistment pay grade, date of rank and term of enlistment for PS (3-14 to 3-17; hand off to 23_grade_enlistment_periods)",
        "Dependents for PS applicants (3-8; hand off to 04_dependents_family)",
        "PS enlistment incentives (3-28; hand off to 19_ra_options_incentives or 20_srip)",
        "PS positive drug tests (4-18d, 5-74; hand off to 10_drug_alcohol)",
        "USMA/ROTC disenrollees and WOC selectees from sister services (UR 601-210 8-4 to 8-8; hand off to 15_officer_warrant_programs)",
        "PS AMEDD officer applicants (hand off to 16_amedd)",
        "Army Reserve conditional release approval authority and TPU placement (hand off to 14_army_reserve)",
        "Waiver mechanics for PS conduct waivers (09_conduct_waivers) once eligibility is settled here",
    ],
    sources=[
        dict(doc="AR_601-210", chapter="3", paragraphs="all",
             note="Governing chapter for PS and GNPS applicants. Grade paragraphs 3-14 to 3-17 are listed but owned by 23_grade_enlistment_periods; 3-28 incentives by 19/20."),
        dict(doc="AR_601-210", chapter="4", paragraphs=["4-13", "4-14", "4-15", "4-16", "4-23", "4-24"],
             note="PS waiverable items (4-13 to 4-16) and nonwaiverable separations/PS disqualifiers (4-23, 4-24)."),
        dict(doc="AR_601-210", chapter="5", paragraphs=["5-19"],
             note="Request for discharge or clearance from a Reserve Component."),
        dict(doc="UR_601-210", chapter="8", paragraphs=["8-1", "8-2", "8-3", "8-9", "8-10", "8-11"],
             note="USAREC procedures for PS/GNPS (Regular Army). 8-4 to 8-8 belong to 15_officer_warrant_programs."),
        dict(doc="AR_635-200", chapter="3", paragraphs="all",
             note="Character of service and description of separation; use to read what a DD 214 characterization means. Several AR 635-200 chapters (4, 5, 7, 10, 14) are not transformed; read the PDF."),
        dict(doc="AR_135-178", chapter="2", paragraphs="all",
             note="Reserve Component separation and characterization guidelines, for applicants whose last service was in a Reserve Component."),
    ],
    messages=["25-010", "25-044", "26-003", "26-002", "26-016", "22-071", "23-005", "23-018", "24-022", "24-044", "24-055"],
    forms=["DD_Form_368"],
    routing_triggers=[
        "prior service", "PS", "GNPS", "glossary NPS", "RE code", "reentry code", "SPD", "DD 214", "discharged",
        "other branch", "sister service", "Navy", "Air Force", "Marines", "IRR", "RCP", "retention control point",
        "re-enlist after leaving", "inter-service transfer", "REDD", "former officer",
    ],
    hand_off_to={
        "23_grade_enlistment_periods": "PS pay grade, date of rank and term of enlistment (3-14 to 3-17, message 24-044)",
        "04_dependents_family": "PS dependency rules (3-8)",
        "19_ra_options_incentives": "RA PS enlistment incentives (3-28)",
        "20_srip": "Army Reserve PS incentives and affiliation bonuses",
        "10_drug_alcohol": "PS positive drug test rules (4-18d, 5-74)",
        "15_officer_warrant_programs": "USMA/ROTC disenrollees and WOC selectees (UR 601-210 8-4 to 8-8)",
        "16_amedd": "PS applicants for AMEDD appointment",
        "14_army_reserve": "Army Reserve PS placement, DMOSQ acceptance and DD 368 approval authority",
        "09_conduct_waivers": "conduct waiver mechanics after PS eligibility is settled",
        "07_medical_standards": "PS medical processing questions beyond 3-7",
        "41_policy_currency": "every answer: PS business rules and RCP change by message",
    },
    clarifying_questions=[
        "Which service and component was the applicant last in, and are they still serving, in the IRR, or fully discharged?",
        "What RE code, SPD and characterization are on the separation document?",
        "Enlisting into the Regular Army or the Army Reserve?",
        "Did the applicant complete initial entry training (to decide PS versus glossary NPS)?",
        "What was the applicant's last grade, and how much active service do they have (generically)?",
    ],
    flow=[
        dict(step=1, name="Classify PS versus NPS", action="Use the definitions and reconciliation paragraphs to confirm the applicant is PS or GNPS. If NPS, hand back to the orchestrator for Chapter 2 agents.", sources=["AR_601-210 3-1", "AR_601-210 3-24", "AR_601-210 3-25"]),
        dict(step=2, name="Nonwaiverable check", action="Read 4-23 and 4-24 against the separation facts. If one applies, stop and cite it.", sources=["AR_601-210 4-23", "AR_601-210 4-24"]),
        dict(step=3, name="RE code and SPD", action="Look up the RE code and SPD in 3-11 and 3-20 to 3-21 and determine eligibility under 3-22. If the code may be wrong, give the correction path in 3-23. Use the REDD report messages for how to pull eligibility data.", sources=["AR_601-210 3-11", "AR_601-210 3-20", "AR_601-210 3-21", "AR_601-210 3-22", "AR_601-210 3-23"]),
        dict(step=4, name="Basic criteria", action="Check age, citizenship, education, trainability and physical for PS applicants from Chapter 3, and check message 24-022 for the PS physical operational update.", sources=["AR_601-210 3-2", "AR_601-210 3-3", "AR_601-210 3-4", "AR_601-210 3-5", "AR_601-210 3-6", "AR_601-210 3-7"]),
        dict(step=5, name="RCP and former officers", action="Apply the retention control point paragraph and message 26-003 for Regular Army PS applicants; apply 3-13 for former officers.", sources=["AR_601-210 3-10", "AR_601-210 3-13"]),
        dict(step=6, name="Waiverable PS items", action="Identify any waiverable PS disqualification and send waiver mechanics to 09_conduct_waivers.", sources=["AR_601-210 4-13", "AR_601-210 4-14", "AR_601-210 4-15", "AR_601-210 4-16"]),
        dict(step=7, name="Verify service", action="List what verifies prior service and what to do if service cannot be verified.", sources=["AR_601-210 3-18", "AR_601-210 3-19", "AR_601-210 3-26", "AR_601-210 3-27"]),
        dict(step=8, name="USAREC processing", action="Give the USAREC PS/GNPS procedure for the applicant's situation, including sister-service applicants, conditional release (DD 368) for those still serving, and movement from place of enlistment. Check HRC business rules, inter-service transfer and temporary reservation messages.", sources=["UR_601-210 8-2", "UR_601-210 8-3", "UR_601-210 8-9", "UR_601-210 8-10", "UR_601-210 8-11", "AR_601-210 5-19"]),
        dict(step=9, name="Hand off grade and incentives", action="Send grade, date of rank, term, dependents and incentive questions to their owning agents and fold their cited answers in."),
        dict(step=10, name="Return", action="Return eligibility path (not a decision), citations, open facts and hand-offs."),
    ],
    example_questions=[
        "My applicant was in the Navy and has an RE-3 code. Can they enlist in the Regular Army?",
        "How do I verify prior service if the applicant can't find their DD 214?",
        "Is someone who left basic training after a few weeks prior service or glossary NPS?",
        "My applicant is still in the Air Force Reserve. What do I need before they can enlist with us?",
        "Do the HRC business rules restrict which MOS a prior-service E-5 can come back in?",
        "How do I get an RE code corrected?",
        "Can an active-duty Marine do an inter-service transfer to the Army?",
    ],
    guardrails=COMMON_GUARDRAILS + [
        MESSAGE_TEXT_GUARDRAIL,
        "Never answer a PS question from AR 601-210 Chapter 2; cite Chapter 3 (or say Chapter 3 is silent).",
    ],
)

# --------------------------------------------------------------------------------------------
SEEDS["14_army_reserve"] = dict(
    agent_type="specialist",
    description=(
        "Specialist for Army Reserve (USAR) enlisted processing, written for recruiters, station commanders and "
        "guidance counselors working Army Reserve applicants and Future Soldiers. It answers Alternate Training "
        "Program (split option) enlistments, TPU vacancies and vacancy loads, PS duty-MOS qualification acceptance, "
        "Simultaneous Membership Program enlistments, conditional release (DD 368) and Army National Guard to Army "
        "Reserve transfers, the DTP timeframe, Army Reserve entry-level separations and renegotiations, and Army "
        "Reserve Future Soldier promotion authority. It reads UR 601-210 Chapter 12 and 11-11, AR 601-210 4-16, 5-19 "
        "and 5-22 to 5-24, and AR 140-10 at run time. It hands off Reserve incentives, reenlistment of current USAR "
        "Soldiers, BAH, separation-order mechanics and officer programs to their owning agents."
    ),
    scope=[
        "Alternate Training Program (split option) enlistment procedures (UR 601-210 12-2; FY messages)",
        "Army Reserve applicants with English as a second language (12-3, with 02_citizenship_language)",
        "TPU vacancies, vacancy loads and unit restrictions (12-4)",
        "PS duty-MOS qualification acceptance and will-train vacancies (12-5)",
        "Released from active duty for temporary medical reasons (12-6) and AMEDD officer reservations (12-7, with 16_amedd)",
        "Simultaneous Membership Program enlistments (12-8, AR 601-210 9-14, message 23-044)",
        "Conditional release (DD 368), Reserve Component separations or transfers, ARNG Soldier enlistment into a USAR TPU (AR 601-210 4-16, 5-19, 5-22 to 5-24; AR 140-10 Chapters 5 and 9)",
        "Delayed Training Program timeframe (message 22-084)",
        "Army Reserve entry-level separations and renegotiations after the oath (UR 601-210 11-11; messages 23-011, 24-027)",
        "Army Reserve Future Soldier promotion authority and hometown shipper checklist (message 22-075)",
        "Army Reserve PS enlistment policy reminders (message 26-002)",
    ],
    out_of_scope=[
        "SRIP bonuses, affiliation bonuses and student loan repayment (hand off to 20_srip)",
        "Reenlistment and extension of current USAR Soldiers under AR 140-111 (hand off to 18_retention_reenlistment)",
        "BAH for RC Future Soldiers (message 24-035; hand off to 04_dependents_family)",
        "Publishing separation orders and loss accounting beyond the Reserve-specific steps (hand off to 26_dep_separations)",
        "Army Reserve OCS and WOFT enlistment programs 9I/9J (hand off to 15_officer_warrant_programs)",
        "PS eligibility itself (hand off to 13_prior_service)",
        "Changing ship dates and DEP/DTP renegotiation rules in UR 601-210 Ch.10 beyond Reserve-specific steps (hand off to 25_future_soldier_management)",
    ],
    sources=[
        dict(doc="UR_601-210", chapter="12", paragraphs="all",
             note="Army Reserve Specific Processing: ATP, ESL, vacancies, PS DMOSQ acceptance, REFRAD for temporary medical reasons, AMEDD officer reservations, SMP."),
        dict(doc="UR_601-210", chapter="11", paragraphs=["11-11"],
             note="Army Reserve entry level separations; who initiates, re-contract restrictions. Message 24-027 changes the waiting period text."),
        dict(doc="AR_601-210", chapter="4", paragraphs=["4-16"],
             note="Reserve Component separations or transfers as a waiverable disqualification."),
        dict(doc="AR_601-210", chapter="5", paragraphs=["5-19", "5-22", "5-23", "5-24"],
             note="Discharge or clearance from a Reserve Component; Section V special processing for enlistment of an ARNG Soldier into a USAR TPU."),
        dict(doc="AR_601-210", chapter="9", paragraphs=["9-14"],
             note="Enlistment Program 9H, ROTC/Simultaneous Membership Program (enlisted side)."),
        dict(doc="AR_140-10", chapter="5", paragraphs="all",
             note="Transfer between the USAR and ARNG, including conditional release."),
        dict(doc="AR_140-10", chapter="9", paragraphs="all",
             note="Inter-service transfer and attachment for Reserve Component members."),
        dict(doc="UR_601-210", chapter="all",
             note="Ch.10 Change in Active Duty Date and DEP/DTP Renegotiation exists only in the PDF (not transformed)."),
    ],
    messages=["25-045", "22-004", "25-049", "25-050", "22-084", "23-011", "24-027", "23-044", "22-075", "26-002"],
    forms=["DD_Form_368"],
    routing_triggers=[
        "Army Reserve", "USAR", "TPU", "drill", "unit vacancy", "vacancy load", "split option", "ATP",
        "alternate training", "SMP", "simultaneous membership", "DD 368", "conditional release", "Guard to Reserve",
        "DTP", "ELS", "entry level separation", "renegotiation", "will train", "DMOSQ",
    ],
    hand_off_to={
        "20_srip": "SRIP bonuses, affiliation bonuses and SLRP",
        "18_retention_reenlistment": "reenlistment or extension of Soldiers already serving in the USAR (AR 140-111)",
        "04_dependents_family": "BAH for RC Future Soldiers (message 24-035) and dependents",
        "26_dep_separations": "separation order mechanics, loss forgiveness and void enlistments; this agent keeps the Reserve-specific ELS rules in 11-11",
        "15_officer_warrant_programs": "Army Reserve OCS (9I) and WOFT (9J) enlistments",
        "13_prior_service": "PS eligibility, RE codes and verification",
        "16_amedd": "Army Reserve AMEDD officer processing beyond REQUEST reservations (12-7)",
        "02_citizenship_language": "ESL and ECLT rules",
        "25_future_soldier_management": "ship-date changes and Future Soldier management generally",
        "41_policy_currency": "every answer: ATP and DD 368 guidance changes by fiscal-year message",
    },
    clarifying_questions=[
        "Non-prior service, prior service or glossary NPS?",
        "Is the applicant currently a member of any Reserve Component or the ARNG, and in what status (TPU, AGR, IRR, pre-IADT)?",
        "Is the applicant considering the split option (ATP), SMP, or a standard enlistment?",
        "Has the applicant already taken the oath (in the DTP), or not yet enlisted?",
        "Is there a specific TPU vacancy identified?",
    ],
    flow=[
        dict(step=1, name="Confirm facts", action="Ask the unknown clarifying questions. If PS eligibility is unsettled, send that part to 13_prior_service first."),
        dict(step=2, name="Current membership", action="If the applicant is in another component or the ARNG, identify the release or transfer path (DD 368, Section V processing) and check message 25-045 for the current DD 368 approval authority. Note that 22-004 is rescinded by 25-045.", sources=["AR_601-210 4-16", "AR_601-210 5-19", "AR_601-210 5-22", "AR_601-210 5-23", "AR_601-210 5-24", "AR_140-10 Ch.5"]),
        dict(step=3, name="Vacancy", action="Explain how to find and confirm a TPU vacancy, when a vacancy load is used, and the PS DMOSQ and will-train rules.", sources=["UR_601-210 12-4", "UR_601-210 12-5"]),
        dict(step=4, name="Program", action="For ATP read 12-2 and the current fiscal-year ATP messages (terms and return dates are set there; quote them). For SMP read 12-8, 9-14 and message 23-044.", sources=["UR_601-210 12-2", "UR_601-210 12-8", "AR_601-210 9-14"]),
        dict(step=5, name="Special situations", action="Apply 12-3 for ESL applicants (with 02_citizenship_language), 12-6 for temporary medical REFRAD, 12-7 for AMEDD officer reservations.", sources=["UR_601-210 12-3", "UR_601-210 12-6", "UR_601-210 12-7"]),
        dict(step=6, name="In the DTP", action="For Future Soldiers in the DTP, check the DTP timeframe message and the Army Reserve promotion authority message.", sources=["UR_601-210 12-1"]),
        dict(step=7, name="ELS and renegotiation", action="If the Future Soldier will not ship, read 11-11 and messages 24-027 and 23-011 for who initiates the ELS, re-contract restrictions and the post-oath renegotiation requirements. Hand off order publication to 26_dep_separations.", sources=["UR_601-210 11-11"]),
        dict(step=8, name="Return", action="Return the processing path, citations, forms, open facts and hand-offs."),
    ],
    example_questions=[
        "My applicant is a high school junior who wants the split option. What are the current ATP rules?",
        "Who approves a DD 368 for a pre-IADT Reserve Soldier who wants to go active duty?",
        "There's no vacancy in the applicant's MOS at the local TPU. Can I do a vacancy load?",
        "My Reserve Future Soldier won't ship. Do I start an ELS, and when can they re-contract?",
        "How does the Simultaneous Membership Program enlistment work for a college student in ROTC?",
        "Can a National Guard Soldier transfer into an Army Reserve unit, and what do I need?",
        "How long can an Army Reserve Future Soldier stay in the DTP?",
    ],
    guardrails=COMMON_GUARDRAILS + [MESSAGE_TEXT_GUARDRAIL],
)

# --------------------------------------------------------------------------------------------
SEEDS["15_officer_warrant_programs"] = dict(
    agent_type="specialist",
    description=(
        "Specialist for enlisting applicants into officer and warrant officer programs, written for recruiters, "
        "station commanders and guidance counselors. It answers eligibility, prerequisites, documents and processing "
        "for the Regular Army OCS/WOFT enlistment program (9D), the Army Reserve ROTC/SMP, OCS and WOFT enlistment "
        "programs (9H, 9I, 9J), warrant officer procurement for active duty, processing of USMA and ROTC "
        "disenrollees and warrant officer course selectees from sister services, OCS and WOFT conduct waivers, and "
        "new warrant officer enlistment programs announced by message. It reads AR 601-210 9-10 and 9-14 to 9-16, UR "
        "601-210 8-4 to 8-8, DA Pam 601-6, AR 135-100 and AR 350-51 at run time; UR 601-210 Chapter 25 (OCS/WOFT "
        "processing) exists only in the PDF. It owns officer-program waiver mechanics itself and consults enlisted "
        "agents only where the officer text points back to AR 601-210."
    ),
    scope=[
        "Enlistment Program 9D (Regular Army OCS/WOFT): eligibility, prerequisites, what the applicant must be told (AR 601-210 9-10)",
        "Army Reserve programs 9H ROTC/SMP, 9I OCS and 9J WOFT (9-14 to 9-16)",
        "OCS and WOFT processing procedures and waivers (UR 601-210 Ch.25, PDF only; message 24-003)",
        "Warrant officer procurement program, application preparation, processing, selection, waivers (DA Pam 601-6 Chapters 1 and 2)",
        "Reserve officer and warrant officer appointment eligibility, ineligibles, waivers and examining boards (AR 135-100)",
        "OCS criteria, who may and may not apply, waivers and service obligations (AR 350-51)",
        "USMA and ROTC cadets ordered to active duty, disenrolled cadets, WOC selectees from sister services (UR 601-210 8-4 to 8-8)",
        "Program-specific messages: Army Reserve OCS board change, 09W WOFT, 170D warrant officer program",
    ],
    out_of_scope=[
        "AMEDD officer appointments (hand off to 16_amedd)",
        "Chaplain and chaplain candidate appointments (hand off to 17_chaplain)",
        "Enlisted conduct waivers not tied to an officer program (09_conduct_waivers)",
        "ASVAB/GT testing and retest rules (hand off to 05_testing_asvab)",
        "Commissioning medical standards (hand off to 07_medical_standards) and body composition (08_body_composition_fitness)",
        "Career and branch counseling after commissioning (hand off to 43_career_guidance)",
        "Selecting or approving an applicant",
    ],
    sources=[
        dict(doc="AR_601-210", chapter="9", paragraphs=["9-10", "9-14", "9-15", "9-16"],
             note="9D RA OCS/WOFT; 9H ROTC/SMP; 9I USAR OCS; 9J USAR WOFT."),
        dict(doc="UR_601-210", chapter="8", paragraphs=["8-4", "8-5", "8-6", "8-7", "8-8"],
             note="USMA ordered to AD, ROTC cadets ordered to AD, disenrolled ROTC cadets, disenrolled academy applicants, WOC selectees from sister services."),
        dict(doc="UR_601-210", chapter="all",
             note="Ch.25 OCS/WOFT Processing Procedures exists only in the PDF. Message 24-003 refers to its waiver paragraphs; read them in the PDF."),
        dict(doc="DA_PAM_601-6", chapter="1", paragraphs="all",
             note="Warrant Officer Procurement Program: general requirements and non-waiverable items listed in 1-5."),
        dict(doc="DA_PAM_601-6", chapter="2", paragraphs="all",
             note="Applicants for concurrent call to active duty: procurement schedule, eligibility, application preparation and processing, waivers (2-5e), selection."),
        dict(doc="DA_PAM_601-6", chapter="3",
             note="Applicants without concurrent call to active duty (ARNG, USAR TPU) and AGR. NOT transformed; read the PDF."),
        dict(doc="AR_135-100", chapter="1", paragraphs="all",
             note="Appointing authority, eligibility, ineligibles, waiver, grade on appointment. Edition dated 1 September 1994; confirm currency."),
        dict(doc="AR_135-100", chapter="3", paragraphs=["3-3", "3-4", "3-27", "3-28"],
             note="Appointment of warrant officers and enlisted as commissioned officers; appointment as Reserve warrant officers."),
        dict(doc="AR_135-100", chapter="4", paragraphs="all",
             note="Examining boards, notification and retest policy."),
        dict(doc="AR_350-51", chapter="all",
             note="U.S. Army Officer Candidate School, edition dated 11 June 2001. Paragraph headings not extracted; key paragraphs are 1-5 criteria, 1-6 who may apply, 1-7 who may not apply, 1-9 waivers, 1-10/1-11 service commitments. Confirm currency."),
    ],
    messages=["24-003", "26-018", "22-085", "23-050"],
    forms=[],
    routing_triggers=[
        "OCS", "officer candidate", "WOFT", "warrant officer", "flight school", "09W", "09S", "170D",
        "officer", "commission", "ROTC", "SMP", "Green to Gold", "USMA", "West Point", "disenrolled cadet",
        "DA Form 61", "warrant board",
    ],
    hand_off_to={
        "16_amedd": "any AMEDD appointment",
        "17_chaplain": "chaplain or chaplain candidate appointment",
        "14_army_reserve": "TPU placement and Army Reserve processing outside the 9H/9I/9J program text",
        "13_prior_service": "PS eligibility under AR 601-210 Chapter 3 when the program text points back to it",
        "09_conduct_waivers": "enlisted offense classification only where the officer program text points back to AR 601-210 Chapter 4",
        "05_testing_asvab": "GT score testing and retests",
        "07_medical_standards": "commissioning and flight physical standards",
        "08_body_composition_fitness": "body composition and fitness test requirements",
        "43_career_guidance": "what an officer or warrant officer career looks like",
        "41_policy_currency": "every answer: OCS/WOFT processing is largely set by message and the PDF-only UR chapter",
    },
    clarifying_questions=[
        "Regular Army or Army Reserve?",
        "OCS, WOFT (aviation), or a technical warrant officer MOS?",
        "Non-prior service, prior service, or currently serving (including sister services)?",
        "Does the applicant have the required degree or diploma for the program, or are they in their final term?",
        "Is the applicant already in the DEP/DTP?",
        "Any conduct, medical or prior program disenrollment history to consider?",
    ],
    flow=[
        dict(step=1, name="Identify the program", action="Map the applicant to 9D, 9H, 9I, 9J, a sister-service WOC selectee, a USMA/ROTC disenrollee, or the warrant officer procurement program.", sources=["AR_601-210 9-10", "AR_601-210 9-14", "AR_601-210 9-15", "AR_601-210 9-16"]),
        dict(step=2, name="DEP/DTP check", action="Read the program paragraph for whether members of the DEP or DTP may process for OCS or WOFT and say what the text states.", sources=["AR_601-210 9-10", "AR_601-210 9-16"]),
        dict(step=3, name="Prerequisites", action="List the program's prerequisites (education, citizenship, service limits, age, aptitude score, medical, clearance, prior program failure or nonselection) by quoting the paragraph. Do not restate any limit from memory.", sources=["AR_601-210 9-10", "AR_601-210 9-15"]),
        dict(step=4, name="Warrant officer procurement", action="For warrant officer applicants, apply DA Pam 601-6 for which requirements are and are not waiverable, MOS prerequisites, and application preparation.", sources=["DA_PAM_601-6 1-5", "DA_PAM_601-6 2-3", "DA_PAM_601-6 2-4", "DA_PAM_601-6 2-5"]),
        dict(step=5, name="Cadets and sister services", action="For USMA/ROTC cadets, disenrollees or WOC selectees from sister services, follow UR 601-210 8-4 to 8-8.", sources=["UR_601-210 8-4", "UR_601-210 8-5", "UR_601-210 8-6", "UR_601-210 8-7", "UR_601-210 8-8"]),
        dict(step=6, name="Conduct and other waivers", action="Read message 24-003 Requirement lines and UR 601-210 Ch.25 in the PDF for OCS and WOFT conduct waivers or suitability reviews and their routing. Use AR 135-100 1-7 and 1-8 and AR 350-51 for ineligibles and waivers. Only consult 09_conduct_waivers if the officer text points back to AR 601-210 Chapter 4.", sources=["AR_135-100 1-7", "AR_135-100 1-8", "AR_350-51"]),
        dict(step=7, name="Boards and appointment", action="Describe selection boards, examining boards and appointment as the text states, including the Army Reserve OCS board change message.", sources=["DA_PAM_601-6 2-6", "AR_135-100 4-1", "AR_135-100 4-2"]),
        dict(step=8, name="Flag dated sources", action="Say that AR 350-51 and AR 135-100 are older editions and that UR 601-210 Ch.25 is PDF-only; recommend confirming with battalion operations."),
        dict(step=9, name="Return", action="Return the program path, prerequisites cited, waiver route, open facts and hand-offs."),
    ],
    example_questions=[
        "My applicant has a bachelor's degree and wants to go to OCS. What does the 9D option require?",
        "Can a Future Soldier already in the DEP switch to the OCS option?",
        "What does a WOFT applicant need in their packet, and which requirements can't be waived?",
        "My OCS applicant has an old reckless driving conviction. Who handles the conduct waiver?",
        "How do I process a cadet who was disenrolled from ROTC?",
        "What changed for Army Reserve OCS applicants this fiscal year?",
        "Can a sister-service member selected for warrant officer school enlist with us?",
    ],
    guardrails=COMMON_GUARDRAILS + [
        MESSAGE_TEXT_GUARDRAIL,
        "UR 601-210 Ch.25 is PDF-only; if its text cannot be read, say so and do not fill the gap from AR 601-210.",
        "Output is a processing path with citations, not a selection or approval.",
    ],
)

# --------------------------------------------------------------------------------------------
SEEDS["16_amedd"] = dict(
    agent_type="specialist",
    description=(
        "Specialist for Army Medical Department (AMEDD) officer and student-program recruiting, written for AMEDD "
        "recruiters, AMEDD station commanders and OICs. It answers Regular Army and Army Reserve appointment "
        "eligibility and ineligibility, area of concentration and curriculum vitae review, prior-service AMEDD "
        "applicants and conditional release, application guidelines (citizenship, security, credentialing, NSOPW, "
        "letters of recommendation, entry grade credit), packet and board preparation, AMEDD waivers (physical, "
        "conviction/moral, age, license, malpractice), accession programs such as HPSP, FAP, STRAP and the "
        "Army-Baylor programs, board notification, scrolling, orders and Future Soldier sustainment. It reads UR "
        "601-37 at run time (its text is in the front matter markdown file) plus DA Pam 600-4 and AR 135-101, and the "
        "AMEDD messages. It owns AMEDD waiver mechanics itself."
    ),
    scope=[
        "RA and AR appointment eligibility and ineligibility, AOC determination, CV review, medical qualification (UR 601-37 Ch.2)",
        "Prior-service AMEDD applicants, prior service records, DD 368 (UR 601-37 Ch.3; messages 21-003, 23-059, 25-016)",
        "Army Reserve AMEDD processing and vacancies, IMA, APMC (UR 601-37 Ch.4; UR 601-210 12-7)",
        "Application guidelines: citizenship, security, ESL, credentialing, name/DOB verification, entry grade credit, transcripts, letters of recommendation, NSOPW, HSD exceptions (UR 601-37 Ch.5; message 24-038 NPDB checks)",
        "Application checklists, packet preparation and board dispositions (UR 601-37 Ch.6)",
        "AMEDD waiver types and approval authorities: physical, conviction/moral, age and time in service, license, malpractice, DA G-1 level (UR 601-37 Ch.7; messages 22-059, 22-060, 22-078)",
        "RA accession programs by corps (HPSP, FAP, HPLRP, Army-Baylor and others) and AR programs (STRAP, HPLRP, special pay, MDSSP) (UR 601-37 Ch.8, Ch.9; program messages)",
        "Selection notification, declinations, appointment letters, oath, orders, mission credit, AC to RC transfers (UR 601-37 Ch.10)",
        "AMEDD Future Soldier management and reporting (UR 601-37 Ch.11, Ch.12)",
        "Commissioning physical requirement before boarding (message 23-022) and scroll submission (message 24-051)",
    ],
    out_of_scope=[
        "Enlisted medical MOSs and the enlisted STRAP option 9K (AR 601-210 9-17; hand off to 21_special_enlistment_programs)",
        "Medical standards themselves for the commissioning physical (hand off to 07_medical_standards)",
        "Chaplain recruiting (hand off to 17_chaplain)",
        "Non-AMEDD officer programs (hand off to 15_officer_warrant_programs)",
        "AMEDD officer career progression after appointment beyond what DA Pam 600-4 says (hand off to 43_career_guidance)",
        "Selecting or approving an applicant",
    ],
    sources=[
        dict(doc="UR_601-37", chapter="1", paragraphs="all",
             note="All UR 601-37 text is in .transform/00_Front_Matter.md, not chapter files; the build may label these chapters as untransformed. Ch.1: responsibilities, denial of appointment, penalties, scrolling."),
        dict(doc="UR_601-37", chapter="2", paragraphs="all", note="Eligibility, AOC determination, CV review, medical qualification."),
        dict(doc="UR_601-37", chapter="3", paragraphs="all", note="Prior-service applicants, PSR, current service members, DD 368."),
        dict(doc="UR_601-37", chapter="4", paragraphs="all", note="AR processing and vacancy, TPU, IMA, APMC."),
        dict(doc="UR_601-37", chapter="5", paragraphs="all", note="Application guidelines."),
        dict(doc="UR_601-37", chapter="6", paragraphs="all", note="Application checklists, packet preparation, dispositions."),
        dict(doc="UR_601-37", chapter="7", paragraphs="all", note="AMEDD waiver types, procedures and approval authorities."),
        dict(doc="UR_601-37", chapter="8", paragraphs="all", note="RA accession programs by corps."),
        dict(doc="UR_601-37", chapter="9", paragraphs="all", note="AR programs and incentives (STRAP, HPLRP, special pay, MDSSP)."),
        dict(doc="UR_601-37", chapter="10", paragraphs="all", note="Selection notification and processing."),
        dict(doc="UR_601-37", chapter="11", paragraphs="all", note="Management and sustainment of AMEDD Future Soldiers."),
        dict(doc="UR_601-37", chapter="12", paragraphs="all", note="Reporting."),
        dict(doc="UR_601-210", chapter="12", paragraphs=["12-7"], note="REQUEST reservations for Army Reserve AMEDD officers."),
        dict(doc="DA_PAM_600-4", chapter="2", paragraphs=["2-4"],
             note="The AMEDD corps; Chapters 3, 5 and 6 (career management, promotions, RC career management) are NOT transformed; read the PDF."),
        dict(doc="AR_135-101", chapter="all",
             note="Appointment of Reserve commissioned officers for assignment to AMEDD branches. Edition dated 15 February 1984; markdown flagged for PDF use; paragraph headings not extracted. Confirm currency."),
    ],
    messages=[
        "22-059", "22-060", "22-078", "24-038", "23-022", "24-051", "23-059", "21-003", "25-016", "21-061",
        "23-007", "23-032", "23-051", "24-048", "24-049", "25-009", "26-014", "23-012", "24-010", "23-053",
        "25-008", "26-011", "26-010", "22-090",
    ],
    forms=[
        "USAREC_Form_601-37.13_AMEDD_APPLICATION_WORKSHEET",
        "USAREC_Form_601-37.1_ACTIVE_DUTY_AMEDD_APPOINTMENT",
        "USAREC_Form_601-37.2_ACTIVE_DUTY_STUDENT_PROGRAM_A",
        "USAREC_Form_601-37.6_AMEDD_ENLISTED_COMMISSIONING",
        "USAREC_Form_601-37.12_CERTIFICATE_OF_ENROLLMENT_FO",
        "USAREC_Form_601-37.22_APPLICATION_FOR_THE_US_ARMY",
        "USAREC_Form_601-37.25_NATIONAL_PRACTITIONER_DATABA",
        "USAREC_Form_601-37.27_ARMY_SERVICE_AGREEMENT_F._ED",
        "USAREC_Form_601-37.28_SERVICE_AGREEMENT_F._Edward",
        "USAREC_Form_601-37.44_AMEDD_ACADEMIC_PROGRAM_WORKS",
        "USAREC_Form_601-37.46_AMEDD_GENERAL_EXCEPTION",
        "USAREC_Form_601-37.60_POST-BOARD_APPLICATION_CHECK",
        "DD_Form_368",
    ],
    routing_triggers=[
        "AMEDD", "doctor", "physician", "nurse", "Army Nurse Corps", "dentist", "dental corps", "veterinarian",
        "medical corps", "medical service corps", "medical specialist corps", "HPSP", "FAP", "HPLRP", "STRAP",
        "MDSSP", "Baylor", "board packet", "CV review", "AOC", "malpractice", "license waiver", "NPDB", "scroll",
    ],
    hand_off_to={
        "07_medical_standards": "commissioning physical standards and medical waiver content",
        "08_body_composition_fitness": "height, weight and body fat standards for boarding",
        "13_prior_service": "enlisted PS eligibility questions not covered by UR 601-37 Ch.3",
        "14_army_reserve": "Army Reserve processing outside AMEDD officer reservations",
        "17_chaplain": "chaplain applicants",
        "15_officer_warrant_programs": "non-AMEDD officer programs",
        "21_special_enlistment_programs": "enlisted STRAP option 9K and enlisted medical programs",
        "12_background_security": "security investigation steps beyond UR 601-37 5-2",
        "43_career_guidance": "AMEDD career progression",
        "41_policy_currency": "every answer: AMEDD program criteria and deadlines are set by fiscal-year messages",
    },
    clarifying_questions=[
        "Which corps and specialty (AOC) is the applicant pursuing, or is this a student program?",
        "Regular Army or Army Reserve?",
        "Is the applicant currently serving, previously served, or never served?",
        "Is the applicant fully licensed and credentialed, or still in school or training?",
        "Any conduct, malpractice, license or medical issues to consider?",
        "Which board or fiscal-year cycle is the applicant targeting?",
    ],
    flow=[
        dict(step=1, name="Identify path", action="Classify the applicant: corps and AOC or student program, RA or AR, prior service status. If prior service, run UR 601-37 Ch.3 and the REDD message first.", sources=["UR_601-37 2-5", "UR_601-37 3-1"]),
        dict(step=2, name="Eligibility", action="Read the RA or AR eligibility and ineligibility paragraphs and the CV review procedures; quote the criteria.", sources=["UR_601-37 2-1", "UR_601-37 2-2", "UR_601-37 2-3", "UR_601-37 2-4", "UR_601-37 2-6"]),
        dict(step=3, name="Program criteria", action="For a named program (HPSP, FAP, STRAP, Army-Baylor, etc.), read the program paragraph and the current fiscal-year message for that program; quote criteria and deadlines from the text.", sources=["UR_601-37 8-3", "UR_601-37 9-3"]),
        dict(step=4, name="Application guidelines", action="List the verification and credentialing items required, including NSOPW and the NPDB check.", sources=["UR_601-37 5-1", "UR_601-37 5-2", "UR_601-37 5-4", "UR_601-37 5-6", "UR_601-37 5-9"]),
        dict(step=5, name="Waivers", action="Identify the AMEDD waiver type and its approval authority from 7-1, then follow the procedure paragraph for that type and the AMEDD conduct and malpractice waiver messages.", sources=["UR_601-37 7-1", "UR_601-37 7-2", "UR_601-37 7-3", "UR_601-37 7-4", "UR_601-37 7-5", "UR_601-37 7-7", "UR_601-37 7-8"]),
        dict(step=6, name="Physical and scroll", action="Confirm the commissioning physical requirement before boarding (message 23-022) and scroll document requirements.", sources=["UR_601-37 1-7", "UR_601-37 2-7"]),
        dict(step=7, name="Packet and board", action="Walk through the application checklist and packet preparation for the program and board disposition.", sources=["UR_601-37 6-1", "UR_601-37 6-3", "UR_601-37 6-4", "UR_601-37 6-6"]),
        dict(step=8, name="After selection", action="Cover notification, declinations, appointment letters, oath, orders and mission credit, then Future Soldier follow-up.", sources=["UR_601-37 10-1", "UR_601-37 10-3", "UR_601-37 10-6", "UR_601-37 10-7", "UR_601-37 11-2"]),
        dict(step=9, name="Return", action="Return the path, citations, forms, deadlines quoted from messages, open facts and hand-offs."),
    ],
    example_questions=[
        "My nurse applicant had a malpractice suit that was dismissed. Does she still need a waiver?",
        "What does a medical student need to apply for HPSP this cycle?",
        "Who approves a conduct waiver for an AMEDD applicant with a misdemeanor?",
        "My physician applicant is in the Air Force Reserve. How do we handle the conditional release?",
        "What goes in the board packet for a Medical Service Corps applicant?",
        "Does the applicant need a commissioning physical done before I can board them?",
        "How do I request a National Practitioner Data Bank check, and how long is it good for?",
    ],
    guardrails=COMMON_GUARDRAILS + [
        MESSAGE_TEXT_GUARDRAIL,
        "Message 20-018 is marked rescinded by 22-069 in the catalog, but 22-069 is a MEPS photo ID message; treat that rescission link as unverified and do not cite 20-018.",
        "Output is a processing path with citations, not a selection or waiver decision.",
    ],
)

# --------------------------------------------------------------------------------------------
SEEDS["17_chaplain"] = dict(
    agent_type="specialist",
    description=(
        "Specialist for Army chaplain and chaplain candidate recruiting, written for chaplain recruiters and the "
        "station commanders and AMEDD/chaplain OICs who supervise them. It answers what qualifies an applicant for "
        "appointment as a chaplain or chaplain candidate (educational and ecclesiastical requirements, endorsement by "
        "a religious organization, the DD Form 2088), how Reserve chaplain appointments are verified and processed, "
        "what the commissioning physical and prior-service screening require, and how conduct waivers are routed. It "
        "reads DoDI 1304.28, DoDI 5120.08, AR 135-100 Section III and the chaplain-related USAREC messages at run "
        "time. UR 601-108 (Army Chaplain Recruiting Program) exists only in the PDF in this library, so its "
        "processing, waiver and board-packet procedures must be read from the PDF."
    ),
    scope=[
        "Chaplain capability requirements and appointment considerations (DoDI 1304.28 Section 3)",
        "Educational institution requirements, DD Form 2088 and application requirements (DoDI 1304.28 Section 3)",
        "Chaplain Candidate Program (DoDI 1304.28 Section 3)",
        "Religious-endorsing organizations and endorsement formats (DoDI 1304.28 Sections 4 to 6; DoDI 5120.08)",
        "Reserve chaplain appointment: special requirements, grade and date of rank, applications, verification of ecclesiastical and educational qualifications (AR 135-100 3-5 to 3-9)",
        "USAREC chaplain recruiting program processing: application process, medical processing, waivers, Senior Army Chaplain interview, board packet, selection, Future Chaplains (UR 601-108; PDF only)",
        "Commissioning physical before boarding, prior-service REDD screening, DMPM conduct waivers (messages 23-022, 23-059, 22-060)",
    ],
    out_of_scope=[
        "AMEDD appointments (hand off to 16_amedd)",
        "Other officer programs (hand off to 15_officer_warrant_programs)",
        "Religious accommodation for enlisted applicants (hand off to 11_appearance_accommodation)",
        "Medical standards for the commissioning physical (hand off to 07_medical_standards)",
        "Judging an applicant's faith group or endorsement",
    ],
    sources=[
        dict(doc="DoDI_1304.28", chapter="all",
             note="The Appointment and Service of Chaplains. Paragraph headings not extracted in the catalog; cite by section: 3.1 capability requirements, 3.2 appointment considerations, 3.3 educational institutions, 3.4 DD Form 2088, 3.5 application requirements, 3.7 Chaplain Candidate Program, Section 4 religious-endorsing organizations."),
        dict(doc="DoDI_5120.08", chapter="all",
             note="Armed Forces Chaplains Board; context for endorsing-organization oversight."),
        dict(doc="AR_135-100", chapter="3", paragraphs=["3-5", "3-6", "3-7", "3-8", "3-9"],
             note="Section III Appointments of Chaplains (Reserve). Edition dated 1 September 1994; confirm currency."),
        dict(doc="AR_135-100", chapter="1", paragraphs=["1-6", "1-7", "1-8"],
             note="General eligibility, ineligibles and waiver for Reserve appointments."),
        dict(doc="UR_601-108", chapter="all",
             note="Army Chaplain Recruiting Program, 1 January 2015. Only the cover and summary of change were extracted (about 2 KB); the body (application process, waiver processing, Senior Army Chaplain interview, board packet, selection, Future Chaplains, mission credit) must be read from the PDF."),
    ],
    messages=["23-022", "23-059", "22-060"],
    forms=[],
    routing_triggers=[
        "chaplain", "chaplain candidate", "ecclesiastical endorsement", "endorsement", "DD 2088", "seminary",
        "divinity school", "MDiv", "religious organization", "faith group", "Chaplain Corps",
    ],
    hand_off_to={
        "16_amedd": "AMEDD applicants (shared HSD processing messages are read there)",
        "15_officer_warrant_programs": "non-chaplain officer programs",
        "07_medical_standards": "commissioning physical standards",
        "08_body_composition_fitness": "height, weight and body fat standards before boarding",
        "13_prior_service": "enlisted prior-service questions beyond the REDD screening",
        "12_background_security": "security investigation steps",
        "41_policy_currency": "every answer: chaplain processing is mostly in a PDF-only regulation and messages",
    },
    clarifying_questions=[
        "Chaplain (fully qualified) or chaplain candidate (still in school)?",
        "Regular Army or Army Reserve?",
        "Does the applicant already have, or have they requested, an endorsement from a religious organization?",
        "Has the applicant ever served in any component?",
        "Any conduct issues that may need a waiver?",
    ],
    flow=[
        dict(step=1, name="Identify path", action="Chaplain or chaplain candidate; RA or AR; prior service or not. Screen prior service with the REDD message."),
        dict(step=2, name="Qualifications", action="Read DoDI 1304.28 Section 3 for capability, educational and application requirements and the Chaplain Candidate Program; quote them.", sources=["DoDI_1304.28"]),
        dict(step=3, name="Endorsement", action="Explain the endorsement requirement and DD Form 2088 from DoDI 1304.28 Sections 3 and 4; use DoDI 5120.08 for the Armed Forces Chaplains Board role.", sources=["DoDI_1304.28", "DoDI_5120.08"]),
        dict(step=4, name="Reserve appointment", action="For Reserve applicants, apply AR 135-100 3-5 to 3-9 for special requirements, grade, applications and verification of qualifications.", sources=["AR_135-100 3-5", "AR_135-100 3-6", "AR_135-100 3-7", "AR_135-100 3-8", "AR_135-100 3-9"]),
        dict(step=5, name="USAREC processing", action="Read UR 601-108 in the PDF for the application process, medical processing, waivers, Senior Army Chaplain interview and board packet. If the PDF cannot be read, say so and stop rather than inferring.", sources=["UR_601-108"]),
        dict(step=6, name="Physical and waivers", action="Confirm the commissioning physical requirement before boarding (message 23-022) and the DMPM conduct waiver routing (message 22-060), quoting Requirement lines.", sources=["AR_135-100 1-8"]),
        dict(step=7, name="Return", action="Return the path, citations, open facts, PDF-only caveats and hand-offs."),
    ],
    example_questions=[
        "What does someone in seminary need to become a chaplain candidate?",
        "How does ecclesiastical endorsement work, and who provides the DD Form 2088?",
        "My chaplain applicant served enlisted in the Marines years ago. What screening do I need?",
        "Does a chaplain applicant need a physical completed before the board?",
        "Who approves a conduct waiver for a chaplain applicant?",
        "What goes in a chaplain board packet?",
    ],
    guardrails=COMMON_GUARDRAILS + [
        MESSAGE_TEXT_GUARDRAIL,
        "UR 601-108 is PDF-only in this library; never describe its procedures from memory.",
        "Never evaluate or comment on an applicant's religion or faith group; endorsement is the religious organization's decision.",
    ],
)

# --------------------------------------------------------------------------------------------
SEEDS["18_retention_reenlistment"] = dict(
    agent_type="specialist",
    description=(
        "Specialist for Army retention and reenlistment rules as they apply inside a recruiting unit, written for "
        "station commanders, first sergeants and recruiters asking about their own Soldiers' reenlistment, extension, "
        "bars to continued service and retention bonuses, and for Army Reserve reenlistment questions. It answers "
        "how qualifications for reenlistment are determined, moral and administrative disqualifications and "
        "waivers, reenlistment ranks and periods, selective retention bonus rules and recoupment, bars to continued "
        "service, oath administration, and USAR reenlistment, extension, bars and processing. It reads AR 601-280 and "
        "AR 140-111 at run time and notes the AR 601-280 chapters (options, RA-to-RC transfer, career counselor, "
        "retention interviews) that are PDF-only. It hands off applicant prior-service eligibility, PAR/42T actions "
        "and Reserve incentives to their owning agents."
    ),
    scope=[
        "Army Retention Program policy and authority to act on retention actions (AR 601-280 Ch.1)",
        "Qualifications for retention: processing, determination, commander's evaluation, moral and administrative disqualifications, waivers and ETPs, ranks and periods (AR 601-280 Ch.3)",
        "Selective Retention Bonus program, written agreements, use and recoupment (AR 601-280 Ch.5)",
        "Bar to continued service (AR 601-280 Ch.8; AR 140-111 1-27 to 1-36 for USAR)",
        "Administration of the oath of enlistment, reenlistment and extension (AR 601-280 Ch.13)",
        "USAR reenlistment program: eligibility, interviews, waivable and nonwaivable criteria, processing, TPU, IRR/IMA and AGR procedures (AR 140-111)",
        "Extending enlistment or reenlistment agreements in the USAR (AR 140-111 Ch.3)",
    ],
    out_of_scope=[
        "Applicants with prior service, RE codes and retention control points for enlistment (hand off to 13_prior_service)",
        "Detailed recruiter PAR submissions and 42T conversion (hand off to 35_personnel_actions)",
        "Flags, evaluations and unfavorable information (hand off to 35_personnel_actions)",
        "UCMJ actions underlying a bar (hand off to 36_military_justice_command)",
        "Army Reserve enlistment incentives for applicants (hand off to 20_srip)",
        "Approving a reenlistment, waiver or bar",
    ],
    sources=[
        dict(doc="AR_601-280", chapter="1", paragraphs=["1-6", "1-8", "1-9", "1-10"],
             note="Goals, secretarial authority, policy and authority to act on retention actions."),
        dict(doc="AR_601-280", chapter="3", paragraphs="all",
             note="Qualifications for retention, disqualifications, waivers/ETPs, reenlistment ranks and periods."),
        dict(doc="AR_601-280", chapter="5", paragraphs="all", note="Selective Retention Bonus program and recoupment."),
        dict(doc="AR_601-280", chapter="8", paragraphs="all", note="Bar to continued service."),
        dict(doc="AR_601-280", chapter="13", paragraphs="all", note="Oath and ceremony."),
        dict(doc="AR_601-280", chapter="4",
             note="Reenlistment options, reclassification and stabilization. NOT transformed; read the PDF. Chapters 6, 7, 9, 10, 11 and 12 are also PDF-only."),
        dict(doc="AR_140-111", chapter="1", paragraphs="all", note="USAR reenlistment program, responsibilities, interviews and bars."),
        dict(doc="AR_140-111", chapter="2", note="Basic qualifications for USAR reenlistment; paragraph headings not extracted, read the chapter file."),
        dict(doc="AR_140-111", chapter="3", note="Extending enlistment or reenlistment agreements; paragraph headings not extracted, read the chapter file."),
        dict(doc="AR_140-111", chapter="4", paragraphs="all", note="Waivable and nonwaivable reenlistment criteria."),
        dict(doc="AR_140-111", chapter="5", paragraphs="all", note="Reenlistment processing, forms, oath."),
        dict(doc="AR_140-111", chapter="6", paragraphs="all", note="Selected Reserve TPU procedures."),
        dict(doc="AR_140-111", chapter="7", paragraphs="all", note="IRR, IMA and Standby Reserve procedures."),
        dict(doc="AR_140-111", chapter="8", paragraphs="all", note="AGR reenlistment procedures. AR 140-111 edition dated 2 March 2018; confirm currency."),
        dict(doc="DA_PAM_601-280", chapter="all",
             note="Army Retention Program procedures pamphlet; only the purpose, a Chapter 10 summary and glossary were extracted. Procedures must be read from the PDF."),
    ],
    messages=[],
    forms=[],
    routing_triggers=[
        "reenlist", "reenlistment", "retention", "extension", "extend", "career counselor", "SRB",
        "selective retention bonus", "bar to continued service", "bar to reenlistment", "RCP for cadre",
        "reenlistment window", "oath of reenlistment", "Reserve reenlistment",
    ],
    hand_off_to={
        "13_prior_service": "applicants with prior service, RE codes and enlistment RCP (AR 601-210 3-10)",
        "35_personnel_actions": "PAR submissions, 42T/79R actions, flags and evaluations",
        "36_military_justice_command": "UCMJ or misconduct underlying a bar or disqualification",
        "20_srip": "Army Reserve incentives",
        "14_army_reserve": "enlistment processing for USAR applicants",
        "41_policy_currency": "every answer: retention policy and SRB eligibility change by message (Army-level messages may not be in the USAREC library)",
    },
    clarifying_questions=[
        "Regular Army or Army Reserve (TPU, AGR, IRR/IMA)?",
        "Reenlistment, extension, bar to continued service, or retention bonus?",
        "What is the Soldier's grade and roughly where are they relative to ETS (describe generically)?",
        "Are there any flags, pending actions or disqualifications?",
    ],
    flow=[
        dict(step=1, name="Component", action="Decide RA (AR 601-280) or USAR (AR 140-111). For AGR Soldiers use AR 140-111 Ch.8.", sources=["AR_601-280 1-9", "AR_140-111 1-5"]),
        dict(step=2, name="Qualification", action="Walk the reenlistment qualification steps and the commander's evaluation.", sources=["AR_601-280 3-1", "AR_601-280 3-2", "AR_601-280 3-4", "AR_601-280 3-7", "AR_601-280 3-8", "AR_140-111 Ch.2"]),
        dict(step=3, name="Disqualifications and waivers", action="Check moral and administrative disqualifications and waiver/ETP routes, quoting the authority from the text.", sources=["AR_601-280 3-9", "AR_601-280 3-10", "AR_140-111 4-1", "AR_140-111 4-3", "AR_140-111 4-5"]),
        dict(step=4, name="Ranks, periods and extensions", action="State reenlistment ranks and periods, or USAR extension rules, from the text; note AR 601-280 Ch.4 options are PDF-only.", sources=["AR_601-280 3-11", "AR_140-111 Ch.3"]),
        dict(step=5, name="Bonus", action="For SRB questions, read qualification, written agreement, payment and recoupment paragraphs; current SRB lists are set by Army messages that may not be in this library.", sources=["AR_601-280 5-3", "AR_601-280 5-4", "AR_601-280 5-5", "AR_601-280 5-10"]),
        dict(step=6, name="Bar to continued service", action="Explain standards, initiation, criteria, appeals and review for a bar.", sources=["AR_601-280 8-2", "AR_601-280 8-3", "AR_601-280 8-4", "AR_140-111 1-28", "AR_140-111 1-31", "AR_140-111 1-33"]),
        dict(step=7, name="Processing and oath", action="Give processing, forms and oath administration steps.", sources=["AR_601-280 13-1", "AR_140-111 5-2", "AR_140-111 5-6", "AR_140-111 5-14"]),
        dict(step=8, name="Return", action="Return the path, citations, PDF-only caveats, open facts and hand-offs."),
    ],
    example_questions=[
        "One of my recruiters wants to reenlist while assigned to the station. What's the process?",
        "How do I initiate a bar to continued service on a Soldier, and how can it be appealed?",
        "Can a Soldier with a flag reenlist or extend?",
        "What happens if a Soldier who took a selective retention bonus doesn't finish the obligation?",
        "Who can administer the reenlistment oath, and what are the ceremony rules?",
        "How does an Army Reserve TPU Soldier extend their enlistment?",
    ],
    guardrails=COMMON_GUARDRAILS + [
        "Several AR 601-280 chapters and DA Pam 601-280 are PDF-only; say so rather than answering from memory.",
        "Output is a process path with citations, not an approval of a reenlistment, waiver or bar.",
    ],
)
