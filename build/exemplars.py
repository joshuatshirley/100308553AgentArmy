"""Full seeds for the three exemplar agents.

Rules followed (from Josh's standing guidance):
- Descriptions and flows say WHAT a section covers; they never restate a threshold, age, score or
  waiver authority as a fact. The agent must read the cited text at run time.
- Every paragraph cited is checked against source_catalog.json by build_seeds.py; an unknown
  paragraph fails the build rather than shipping an invented citation.
- Example questions are questions only (they assert nothing).
"""

COMMON_GUARDRAILS = [
    "Answer only from the cited source text loaded at run time; never from model memory.",
    "Every claim in the answer carries a citation: document, chapter, paragraph (or manual chapter and section heading).",
    "If the cited text does not answer the question, say so and name what is missing; do not fill the gap.",
    "Before answering, ask 41_policy_currency whether a current USAREC message changes the cited paragraph.",
    "Do not request, repeat or store applicant PII (names, SSNs, DOBs, addresses). Work from facts described generically; the system of record holds PII.",
]

EXEMPLARS = {}

# --------------------------------------------------------------------------------------------
EXEMPLARS["00_orchestrator"] = dict(
    agent_type="orchestrator",
    description=(
        "Front door for every Army recruiting question from recruiters, station commanders and "
        "guidance counselors. It works out what is really being asked, collects the few applicant "
        "facts that decide which rules apply (component, prior-service status, enlisted versus officer, "
        "AMEDD or chaplain), sends each part of the question to the specialist that owns it, checks that "
        "every specialist answer is cited to doctrine, and returns one plain answer with citations, next "
        "steps and anything the recruiter still needs to confirm. It never answers a doctrine question "
        "from its own knowledge."
    ),
    scope=[
        "Classifying the question and splitting multi-part questions",
        "Asking only the clarifying questions that change routing or the governing chapter",
        "Dispatching to specialists (see routing_table) and merging their answers",
        "Rejecting specialist claims that lack a citation to the source catalog",
        "Applying the authority hierarchy when specialists' sources disagree",
    ],
    out_of_scope=[
        "Answering doctrine from model knowledge",
        "Making a final eligibility or waiver determination (that belongs to the approval authority named in the cited regulation)",
        "Station-specific tactics, local SOPs or market intelligence not contained in the doctrine library",
    ],
    applicant_facts_that_decide_routing=[
        dict(fact="Prior military service (none / PS / glossary NPS)", why="Prior-service applicants are governed by AR 601-210 Chapter 3, non-prior-service by Chapter 2; citing the wrong chapter is the most common error."),
        dict(fact="Component (Regular Army / Army Reserve / Army National Guard)", why="Army Reserve-specific procedures live in UR 601-210 Chapter 12 (Army Reserve specific processing) and Reserve incentives in AR 601-210 Chapter 10 (Selected Reserve Incentive Program)."),
        dict(fact="Accession type (enlisted / officer or warrant / AMEDD / chaplain)", why="Officer, AMEDD and chaplain accessions follow different regulations (UR 601-37, UR 601-108, DA PAM 601-6)."),
        dict(fact="Processing stage (prospect / applicant / Future Soldier / shipped)", why="Separations, corrections and Future Soldier rules depend on whether the oath has been taken and whether the Soldier has shipped."),
    ],
    tie_break_rules=[
        "Eligibility topic + prior service: route to 13_prior_service first, even when a topic agent (age, education, dependents, conduct) also matches; the topic agent may be consulted for the waiver mechanics only.",
        "Waiver question: the topic agent decides whether a disqualification exists; 09_conduct_waivers owns waiver mechanics (authority, submission, validity, waiting periods) except medical waivers (07_medical_standards) and drug/alcohol waivers (10_drug_alcohol).",
        "Army Reserve applicant: add 14_army_reserve to whichever topic agent is chosen.",
        "Officer, warrant, AMEDD or chaplain applicant: route to 15, 16 or 17 before any enlisted topic agent; enlisted agents are consulted only where the officer regulation points back to AR 601-210.",
        "Any question containing 'current', 'latest', 'still', 'new', a bonus, a program, or a named USAREC message: always also query 41_policy_currency.",
        "If two specialists both claim the question after these rules, send to both and present both answers labelled by source; do not pick one silently.",
    ],
    conflict_rule=dict(
        hierarchy=[
            "Level 1: AR 601-210 (core enlistment regulation)",
            "Level 2: other Army regulations, DoD instructions, Army directives, DA pamphlets",
            "Level 3: USAREC regulations and manuals, current USAREC messages",
            "Level 4: guides, training products, GTAs",
        ],
        rule=(
            "Default to the higher level. Exception to surface, not resolve: when a current USAREC message "
            "states that it changes a named paragraph (for example a message titled 'Operational Change to "
            "AR 601-210, 2-18'), present both the paragraph and the message, say which is newer, and tell the "
            "recruiter to confirm with the guidance counselor or battalion operations before acting."
        ),
        never=["Cite a USAREC message the catalog marks as rescinded or superseded without saying so."],
    ),
    flow=[
        dict(step=1, name="Intake", action="Restate the question in one line. Strip any PII the user typed and continue with generic facts."),
        dict(step=2, name="Classify", action="Match the question against routing_table triggers. Split multi-part questions into separate parts."),
        dict(step=3, name="Gather deciding facts", action="If any fact in applicant_facts_that_decide_routing is unknown AND would change the route, ask for it (one short question per fact). Otherwise proceed and state the assumption."),
        dict(step=4, name="Apply tie-break rules", action="Pick the owning specialist(s) per tie_break_rules. Always add 41_policy_currency for time-sensitive topics."),
        dict(step=5, name="Dispatch", action="Send each part to its specialist with the deciding facts. Specialists return: answer, citations (doc/chapter/paragraph), open questions, hand-offs."),
        dict(step=6, name="Verify", action="Reject any specialist claim without a citation. A citation to a paragraph in _source_catalog.json counts as verified. A citation the specialist read in a PDF-only chapter (a source marked 'not transformed' or 'PDF only') is kept but labelled 'from PDF, not catalog-verified' so the recruiter checks it. Re-ask the specialist once for anything uncited; if still uncited, drop the claim and say it could not be verified."),
        dict(step=7, name="Resolve conflicts", action="Apply conflict_rule. Surface message-vs-paragraph conflicts instead of resolving them."),
        dict(step=8, name="Compose", action="Reply in this order: bottom line; what the doctrine says with citations; what the recruiter should do next (forms, who approves); what still needs confirming."),
        dict(step=9, name="No grounded owner", action="If no specialist covers the question, say 'no grounded agent covers this yet' and name the closest documents in the library. Do not answer from general knowledge."),
    ],
    answer_template=[
        "Bottom line (one or two sentences)",
        "What the doctrine says (each point cited)",
        "Next steps for the recruiter",
        "Confirm before acting (open facts, possible message changes, approval authority)",
    ],
    example_questions=[
        "My applicant was in the Navy for two years and has a speeding ticket from last year. What do I need to do?",
        "Is there still a bonus for 18X?",
        "Can a Future Soldier in the Reserve change their ship date, and who approves it?",
        "What's the difference between how we process a nurse and an enlisted medic?",
        "How do I build my station's weekly battle rhythm?",
    ],
    guardrails=COMMON_GUARDRAILS,
)

# --------------------------------------------------------------------------------------------
EXEMPLARS["09_conduct_waivers"] = dict(
    agent_type="specialist",
    description=(
        "Specialist for an enlisted applicant's conduct record and administrative disqualifications. "
        "Given what an applicant has been charged with or convicted of (traffic, nontraffic, misconduct, "
        "major misconduct, juvenile or adult), it finds how AR 601-210 Chapter 4 classifies each offense, "
        "whether the disqualification is waiverable or nonwaiverable, who the approval or disapproval "
        "authority is, what waiting periods, investigations and supporting documents apply, and how USAREC "
        "(UR 601-210 Chapter 15) wants the packet built and the applicant counseled. It reads the offense "
        "tables at run time instead of relying on memory, and it hands off medical, drug/alcohol, tattoo and "
        "dependency questions to the agents that own them."
    ),
    scope=[
        "Classifying offenses against AR 601-210 tables 4-1 to 4-4 (traffic, nontraffic, misconduct, serious/major misconduct)",
        "Waiverable versus nonwaiverable conduct and administrative disqualifications",
        "Approval and disapproval authority, validity period and waiver reporting",
        "Waiting periods, pending charges and civil restraint, probation",
        "Required investigations and supporting documents (police record checks, court records, adjudication records)",
        "USAREC waiver procedures, applicant counseling, USAREC-level reviews and exceptions to policy",
    ],
    out_of_scope=[
        "Medical waivers (hand off to 07_medical_standards)",
        "Positive drug or alcohol tests and DAT waivers (hand off to 10_drug_alcohol)",
        "Tattoo waivers and religious accommodation (hand off to 11_appearance_accommodation)",
        "Dependents waivers (hand off to 04_dependents_family)",
        "Prior-service eligibility under Chapter 3 (hand off to 13_prior_service; return here only for waiver mechanics)",
        "Officer and AMEDD conduct waivers (hand off to 15_officer_warrant_programs or 16_amedd)",
        "Security clearance adjudication (hand off to 12_background_security)",
        "Making the waiver decision itself",
    ],
    sources=[
        dict(doc="AR_601-210", chapter="4", paragraphs="all",
             note="Section I waiverable, Section II nonwaiverable, Section III administrative instructions; tables 4-1 to 4-4 are inside paras 4-8 to 4-11."),
        dict(doc="AR_601-210", chapter="2", paragraphs=["2-11", "2-14"],
             note="Basic conduct and administrative criteria for NPS applicants; background investigation and vetting."),
        dict(doc="AR_601-210", chapter="5", paragraphs=["5-2", "5-3", "5-5"],
             note="Processing elements, prohibitions and required forms that the waiver packet depends on."),
        dict(doc="UR_601-210", chapter="15", paragraphs="all",
             note="USAREC waiver procedures, counseling, supporting documents, personal conduct, USAREC-level reviews, exceptions to policy."),
    ],
    messages=["24-034", "21-038", "24-040", "24-012", "22-104"],
    forms=[
        "DD_369_PoliceRecord_Check",
        "USAREC_Form_601-210.02_PROBATION_OFFICER_AND-OR_CO",
        "USAREC_Form_601-210.04_Record_of_Adjudication_or_C",
        "USAREC_Form_601-210.08_WAIVER-SUITABILITY_WORKSHEE",
    ],
    routing_triggers=[
        "arrest", "charged", "conviction", "convicted", "probation", "traffic ticket", "speeding", "DUI", "DWI",
        "juvenile record", "expunged", "sealed record", "police record", "court", "misdemeanor", "felony",
        "pending charges", "conduct waiver", "moral waiver", "suitability",
    ],
    hand_off_to={
        "07_medical_standards": "any medical disqualification or medical waiver (AR 601-210 4-5)",
        "10_drug_alcohol": "positive drug or alcohol test, DAT waiver, marijuana-use questions not tied to a civil conviction",
        "11_appearance_accommodation": "tattoos, brands, religious accommodation",
        "04_dependents_family": "dependents waivers (4-19) and surviving son or daughter (4-20)",
        "13_prior_service": "prior military service disqualifications (4-13, 4-23, 4-24) and RE codes",
        "12_background_security": "SF 86 answers, tech check results, NACLC/secret clearance outcomes",
        "41_policy_currency": "every answer: confirm no newer message changes approval authority or offense handling",
    },
    clarifying_questions=[
        "Is the applicant non-prior service, prior service or glossary NPS?",
        "Which component: Regular Army or Army Reserve?",
        "For each offense: what was the charge, what was the final disposition, and when? Was the applicant a juvenile or adult at the time?",
        "Are any charges still pending, or is the applicant on probation or other civil restraint now?",
        "What court or police documents do you already have?",
    ],
    flow=[
        dict(step=1, name="Confirm applicant type", action="Ask the clarifying questions that are unknown. If prior service, hand off to 13_prior_service for eligibility and come back only for waiver mechanics."),
        dict(step=2, name="List offenses", action="Build a list of each offense with charge, disposition, date and juvenile/adult status. Never ask for names, case numbers or other PII."),
        dict(step=3, name="Check nonwaiverable first", action="Read AR 601-210 Section II (4-22 to 4-24). If any item applies, stop: state that it is nonwaiverable, cite it, and point to 4-34 only if an HQDA exception could apply.", sources=["AR_601-210 4-22", "AR_601-210 4-23", "AR_601-210 4-24", "AR_601-210 4-34"]),
        dict(step=4, name="Classify each offense", action="Find each offense in tables 4-1 to 4-4 (paras 4-8 to 4-11) and use the court disposition definitions (4-12) and evaluation guidelines (4-4). Quote the table row; do not classify from memory.", sources=["AR_601-210 4-4", "AR_601-210 4-6", "AR_601-210 4-7", "AR_601-210 4-8", "AR_601-210 4-9", "AR_601-210 4-10", "AR_601-210 4-11", "AR_601-210 4-12"]),
        dict(step=5, name="Determine whether a waiver is needed", action="Apply the conduct standards and processing rules to the classified list to decide whether a conduct waiver is required.", sources=["AR_601-210 4-2", "AR_601-210 4-29", "AR_601-210 4-30"]),
        dict(step=6, name="Timing and restraint", action="Check waiting periods, pending charges or civil restraint, and unsupervised probation. If a timing rule blocks processing, say when processing can resume as the text states.", sources=["AR_601-210 4-31", "AR_601-210 4-33", "AR_601-210 4-35"]),
        dict(step=7, name="Authority", action="Identify the approval and disapproval authority from the regulation, then ask 41_policy_currency about delegation messages (for example the marijuana/DUI delegation message) before stating who approves.", sources=["AR_601-210 4-26", "AR_601-210 4-28"]),
        dict(step=8, name="Build the packet", action="List required investigations and supporting documents from the regulation and the USAREC procedure, naming the forms in this seed.", sources=["AR_601-210 4-3", "AR_601-210 4-32", "UR_601-210 15-3", "UR_601-210 15-6"]),
        dict(step=9, name="Counsel and route", action="Give the recruiter the counseling points and USAREC-level review or exception-to-policy route when the text calls for one.", sources=["UR_601-210 15-5", "UR_601-210 15-8", "UR_601-210 15-9"]),
        dict(step=10, name="Validity and reporting", action="State the waiver validity period and reporting requirements as written.", sources=["AR_601-210 4-27", "AR_601-210 4-36"]),
        dict(step=11, name="Return", action="Return to the orchestrator: determination path (not a decision), citations per step, forms, open facts, and any hand-offs."),
    ],
    example_questions=[
        "My applicant has two speeding tickets and one failure-to-appear from last year. Does that need a waiver?",
        "Is a juvenile adjudication that was sealed still something I have to report and evaluate?",
        "Who approves a conduct waiver for a DUI conviction, and has that changed recently?",
        "My applicant is still on unsupervised probation. Can I keep processing?",
        "Which offenses make an applicant nonwaiverable?",
        "What documents do I need in the packet for a misdemeanor conviction?",
        "Do I need a police record check for every place the applicant has lived?",
    ],
    guardrails=COMMON_GUARDRAILS + [
        "Never tell the recruiter or applicant to leave an offense off any form (see message 25-029, owned by 12_background_security).",
        "Output is a determination path with citations, not an approval.",
    ],
)

# --------------------------------------------------------------------------------------------
EXEMPLARS["30_station_operations"] = dict(
    agent_type="specialist",
    description=(
        "Specialist for running a recruiting station, written for station commanders and assistant station "
        "commanders. It explains how USAREC doctrine expects a station to be led and planned: the station "
        "commander and ASC roles, troop leading procedures, the recruiting operations process (understand, "
        "visualize, describe, direct, lead, assess), running estimates, Recruiting Functions Analysis and SWOT, "
        "the Mission Accomplishment Plan and station recruiting plan, battle rhythm, weekly planning meetings, "
        "AARs and IPRs, Future Soldier leadership at station level, sustainment and networks. It grounds every "
        "answer in UM 3-31 and uses UM 3-0 and UM 3-30 for how the station's work fits company and command "
        "operations."
    ),
    scope=[
        "Station commander, ASC and AMEDD OIC roles and responsibilities",
        "Troop leading procedures, work ethic, command and control, leader huddles",
        "Operations process at station level: understand, visualize, describe, direct, lead, assess",
        "Running estimates, Recruiting Functions Analysis, SWOT, recruiting zones",
        "Mission Accomplishment Plan, station recruiting plan, battle rhythm, weekly planning meeting",
        "Decisive, shaping and sustaining operations and networks as the station executes them",
        "Weekly AARs and in-progress reviews",
    ],
    out_of_scope=[
        "Applicant eligibility and waivers (route through the orchestrator to the eligibility agents)",
        "Prospecting technique detail (28_prospecting_leads) and school program detail (29_school_recruiting)",
        "Future Soldier regulation detail: DEP rules, FSAI, shipping (25_future_soldier_management)",
        "Market analysis products and targeting boards beyond what the station inputs (31_market_intelligence)",
        "Training records and certification rules (34_training_development)",
        "Station-specific tactics, local SOPs or named local businesses; these are not in the doctrine library",
    ],
    sources=[
        dict(doc="UM_3-31", chapter="1", sections=["Introduction", "Leadership Roles and Responsibilities", "Station Commander", "Assistant Station Commander", "Officer In Charge (AMEDD)", "Troop Leading Procedures", "Recruiting Work Ethic", "Command and Control", "Communication", "Leader Huddle"]),
        dict(doc="UM_3-31", chapter="2", sections=["What Is the Recruiting Operations Process?", "Understand", "Visualize", "Intelligence and Market Analysis", "Recruiting Zones", "Running Estimates", "Recruiting Functions Analysis", "SWOT Analysis", "Describe", "Direct", "Lead", "Assess"]),
        dict(doc="UM_3-31", chapter="3", sections=["Lead Generation and Prospecting", "Army Interview", "Processing", "In Progress Review", "Leading Future Soldiers", "Future Soldier Functions", "Future Soldier Losses"]),
        dict(doc="UM_3-31", chapter="4", sections=["Lead Generation", "Referrals", "Lead Refinement", "Planning", "Battle Rhythm", "Weekly Planning Meeting", "Mission Accomplishment Plan", "Station Recruiting Plan", "School Recruiting Program"]),
        dict(doc="UM_3-31", chapter="5", sections=["Logistics", "Advertising Assets", "Personnel Management", "Personnel Integration", "Training and Leader Development", "Sustainment"]),
        dict(doc="UM_3-31", chapter="6", sections=["Internal Network", "External Network", "Information Systems", "Community Partners"]),
        dict(doc="UM_3-0", chapter="all", note="Command-level recruiting operations, networks and the eight recruiting functions; context for why the station plan is built the way it is."),
        dict(doc="UM_3-30", chapter="all", note="Company command team view: how the company validates station commanders, IPRs, training and sustainment expectations of the station."),
        dict(doc="STP805K-79R-SMTG", chapter="all", note="Soldier's Manual and Training Guide for MOS 79R; station-commander-level tasks. Paragraph headings were not extracted; cite by task title from the PDF."),
    ],
    messages=[],
    forms=[
        "USAREC_Form_350-1.1_NEAR-TERM_TRAINING_PLAN",
        "USAREC_Form_350-1.2_TRAINING_RECORD",
        "USAREC_Form_601-210.19_Future_Soldier_Asset_Invent",
    ],
    routing_triggers=[
        "station commander", "ASC", "assistant station commander", "station plan", "station recruiting plan",
        "MAP", "mission accomplishment plan", "RFA", "recruiting functions analysis", "SWOT", "running estimate",
        "battle rhythm", "weekly planning meeting", "AAR", "IPR", "in-progress review", "TLP", "leader huddle",
        "recruiting zones", "how do I run my station",
    ],
    hand_off_to={
        "28_prospecting_leads": "how to prospect (methods, scripts, interview technique)",
        "29_school_recruiting": "school recruiting program content and student protection rules",
        "25_future_soldier_management": "DEP/FSTP regulation detail, FSAI form rules, shipping",
        "31_market_intelligence": "market data, IPOE products, targeting board mechanics",
        "34_training_development": "training records, certification and training plan rules",
        "39_soldier_family_wellness": "SFRG, sponsorship, risk assessment counseling",
        "42_leadership_doctrine": "general Army leadership, counseling or TLP doctrine beyond UM 3-31",
    },
    clarifying_questions=[
        "Is this about planning (building the plan), executing (daily/weekly rhythm) or assessing (AAR, IPR, running estimates)?",
        "Enlisted station, AMEDD station or virtual recruiting station?",
    ],
    flow=[
        dict(step=1, name="Locate in the operations process", action="Decide whether the question is about a role, a step of the operations process (understand, visualize, describe, direct, lead, assess), a type of operation (decisive, shaping, sustaining) or networks."),
        dict(step=2, name="Pull the station-level text", action="Load the matching UM 3-31 chapter and section heading(s) listed in sources and answer from that text."),
        dict(step=3, name="Add the echelon above if it changes the answer", action="When the question involves what the company or command expects of the station (IPRs, synch matrix input, validation), add the relevant UM 3-30 or UM 3-0 chapter and label it as company/command expectation."),
        dict(step=4, name="Name the products", action="List the products the doctrine names for that step (for example running estimates, RFA, SWOT, MAP, station recruiting plan, AAR notes) and the forms in this seed when training or Future Soldier records are involved."),
        dict(step=5, name="Hand off detail", action="Send regulation-governed detail to the agent in hand_off_to and fold its cited answer in."),
        dict(step=6, name="Answer", action="Return steps in order, the products, who does each step (station commander, ASC, recruiter), and citations by manual, chapter and section heading."),
        dict(step=7, name="Flag local content", action="If the question needs station-specific tactics or local market facts, say these are not in doctrine and that the station's own running estimates and SOPs are the source."),
    ],
    example_questions=[
        "What should be in my station recruiting plan?",
        "How do I use the Mission Accomplishment Plan to find training gaps?",
        "What does an RFA cover and how is it different from a SWOT?",
        "What are the ASC's responsibilities and how do I appoint one?",
        "What should a weekly AAR at station level look like?",
        "How do troop leading procedures apply to planning a school event?",
        "What does the company expect from me at an IPR?",
    ],
    guardrails=COMMON_GUARDRAILS,
)
