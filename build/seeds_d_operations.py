"""Seeds for the Operations and Command-support groups (roster ids 28, 29, 31-35).

Station-level planning (station recruiting plan, MAP, battle rhythm, running estimates, recruiting
zones as the station assigns them) belongs to 30_station_operations (exemplar); these seeds hand it back.
USAREC manuals (UM 3-xx) and training circulars have untitled paragraphs; they are cited by chapter and
by the section headings copied from each manual's table of contents (.transform/00_Front_Matter.md;
UM 3-30's contents page is in .transform/01_UM_3-30.md).
No seed states a threshold, time limit, dollar amount or approval authority as fact; each tells the
agent which section to read at run time.
"""
from exemplars import COMMON_GUARDRAILS

SEEDS = {}

# --------------------------------------------------------------------------------------------
SEEDS["28_prospecting_leads"] = dict(
    agent_type="specialist",
    description=(
        "Specialist for how recruiters generate, refine and work leads, written for recruiters and the "
        "station commanders who coach them. It explains lead generation versus prospecting, lead "
        "refinement and blueprinting, referrals, area canvassing, active and passive prospecting, the "
        "three prospecting methods (telephone, face-to-face, virtual), texting rules, high-potential lead "
        "handling, EMM Connect lead notifications, and the Army interview (guideposts, counseling, the "
        "Army story, engendering a commitment). It reads UM 3-32 for the recruiter's view, UM 3-31 for "
        "what the station commander directs and assesses, UM 3-30 for company expectations, and the "
        "USAREC training circulars on prospecting and interviewing for technique, plus the current USAREC "
        "messages on texting, high-potential leads and EMM Connect. It hands station planning to "
        "30_station_operations, school-program rules to 29_school_recruiting, market data to "
        "31_market_intelligence, and anything about eligibility or processing to the agents that own them."
    ),
    scope=[
        "Lead generation activities and how they differ from prospecting (area canvassing, social media posts, events)",
        "Lead refinement and management, blueprinting, referrals as a lead source",
        "Active versus passive prospecting and when to combine them",
        "Telephone, texting, face-to-face and virtual prospecting methods and the station commander's role in directing them",
        "High-potential lead handling and EMM Connect notifications as set by current USAREC messages",
        "Prohibited mass-texting and unsolicited automated messaging",
        "The Army interview: guideposts, counseling, the Army story and personal Army story, engendering a commitment, overcoming obstacles",
        "Follow-up with leads, prospects and centers of influence as a prospecting activity",
    ],
    out_of_scope=[
        "Building the station recruiting plan, MAP or battle rhythm (30_station_operations)",
        "School Recruiting Program rules, student directory release and high school protection (29_school_recruiting)",
        "Market share, IPOE products, zone boundaries and targeting boards (31_market_intelligence)",
        "COI events and Soldier Referral Program validation (32_coi_support_programs)",
        "Official social media account rules and advertising (33_marketing_public_affairs)",
        "Whether a prospect is eligible (route through the orchestrator to the eligibility agents)",
        "PiCAT/APT prescreen testing rules (05_testing_asvab) and processing steps after commitment (24_processing_meps)",
        "Station-specific scripts, local target lists or named local businesses; these are not in the doctrine library",
    ],
    sources=[
        dict(doc="UM_3-32", chapter="7", sections=["Lead Generation", "Lead Refinement and Management", "Referrals", "Area Canvassing", "High Schools", "Prospecting", "Active Prospecting", "Passive Prospecting", "Active and Passive Prospecting", "Prospecting Methods", "Telephone Prospecting", "Face to Face Prospecting", "Virtual Prospecting", "Summary"],
             note="Recruiter-level doctrine on lead generation and prospecting; Figure 7-1 is the recruiting funnel."),
        dict(doc="UM_3-32", chapter="8", sections=["Guideposts", "Counseling", "The Army Story / Personal Army Story", "Engender a Commitment", "Summary"],
             note="The Army interview; Figure 8-1 (guideposts) and Figure 8-2 (SOLDIER acrostic) are images in the PDF."),
        dict(doc="UM_3-32", chapter="3", sections=["Decisive Operations", "Shaping Operations", "Maintaining Battle Rhythms", "Work Hours"],
             note="Where prospecting sits in the recruiter's plan and battle rhythm."),
        dict(doc="UM_3-31", chapter="3", sections=["Lead Generation and Prospecting", "Prospecting", "Telephone Prospecting", "Face-to-Face Prospecting", "Virtual Prospecting", "Army Interview"],
             note="What the station commander directs and assesses in prospecting and the Army interview."),
        dict(doc="UM_3-31", chapter="4", sections=["Lead Generation", "Referrals", "Lead Refinement"],
             note="Lead generation, referrals and refinement as station shaping operations."),
        dict(doc="UM_3-30", chapter="4", sections=["Decisive Operations", "Lead Generation", "Prospecting", "Interviewing"],
             note="Company command team expectations. Catalog has no chapter file; text is in UM_3-30/.transform/07_Planning.md (contents page in 01_UM_3-30.md)."),
        dict(doc="UTC_5-03.1", chapter="all",
             note="Actual title (front matter): UTC 5-03.1 Prospecting, Processing, and Analysis; catalog title is wrong. Single full-document markdown, 00_Full_Document.md). Use its chapters on Basics of Prospecting, Lead Generation, Telephone, Face-to-Face and Virtual Prospecting, Contact Scripts, Follow-Up and Planning Considerations. Level 4 training product."),
        dict(doc="UTC_5-03.2", chapter="all",
             note="Actual title (front matter): UTC 5-03.2 Influencing and Interviewing; catalog title is wrong. Chapters: The Recruiter, Telling the Army Story, Components and Steps of the Army Interview, Engendering the Commitment, Overcoming Obstacles. Level 4 training product."),
        dict(doc="UTP_3-10.4_(VRA)_V1", chapter="2",
             note="Virtual recruiting operations: messaging text and email, initial contact, virtual appointment. Level 4 training product."),
    ],
    messages=["25-011", "21-040", "21-035"],
    forms=[],
    routing_triggers=[
        "prospecting", "prospect", "phone calls", "telephone prospecting", "texting", "text messages", "mass text",
        "face to face", "virtual prospecting", "leads", "lead refinement", "blueprinting", "area canvassing",
        "high potential lead", "HPL", "EMM", "EMM Connect", "referrals", "Army interview", "guideposts",
        "Army story", "objections", "close", "follow-up",
    ],
    hand_off_to={
        "30_station_operations": "station recruiting plan, MAP, battle rhythm, IPRs and how prospecting is resourced in the plan",
        "29_school_recruiting": "school recruiting program tasks, student lists and directory access, protected high school students",
        "31_market_intelligence": "market share, target market analysis, zone boundaries, targeting board outputs",
        "32_coi_support_programs": "COI events, HRAP/SRAP support Soldiers, Soldier Referral Program validation",
        "33_marketing_public_affairs": "official social media accounts, paid boosting, advertising and branded content",
        "05_testing_asvab": "PiCAT, APT and ASVAB questions raised during prospecting",
        "24_processing_meps": "what happens after the prospect commits (application and processing)",
        "41_policy_currency": "every answer that relies on a USAREC message (texting, HPL, EMM Connect)",
    },
    clarifying_questions=[
        "Is this about generating leads, contacting leads (prospecting) or conducting the Army interview?",
        "Which market: high school senior, graduate, prior service, in-service or medical?",
        "Is the question from the recruiter's view (how to do it) or the station commander's view (how to direct and assess it)?",
    ],
    flow=[
        dict(step=1, name="Place the activity", action="Decide whether the question is lead generation, lead refinement, prospecting (active or passive; telephone, face-to-face or virtual) or the Army interview. Doctrine draws a hard line between lead generation and prospecting; keep it.", sources=["UM_3-32 Ch.7", "UM_3-31 Ch.4"]),
        dict(step=2, name="Answer from the recruiter manual", action="Load the matching UM 3-32 chapter and section and answer from that text.", sources=["UM_3-32 Ch.7", "UM_3-32 Ch.8"]),
        dict(step=3, name="Add the leader view", action="If the asker leads recruiters, add what UM 3-31 says the station commander directs, monitors and assesses for that method, and UM 3-30 for what the company expects.", sources=["UM_3-31 Ch.3", "UM_3-30 Ch.4"]),
        dict(step=4, name="Technique detail", action="For scripts, follow-up rhythm, interview steps or overcoming obstacles, pull the relevant chapter of the training circulars and label it as a Level 4 training product.", sources=["UTC_5-03.1", "UTC_5-03.2", "UTP_3-10.4_(VRA)_V1 Ch.2"]),
        dict(step=5, name="Check message rules", action="For texting, high-potential leads or EMM Connect, read messages 21-035, 21-040 and 25-011 and state their requirements as written, with the message number; ask 41_policy_currency whether anything newer applies."),
        dict(step=6, name="Hand off", action="Send planning, school, market, COI, social media and eligibility parts to the agents in hand_off_to and fold their cited answers in."),
        dict(step=7, name="Answer", action="Return the method or steps, who does them, any message requirement and citations by manual, chapter and section heading. Say plainly that local lead lists and scripts come from the station, not doctrine."),
    ],
    example_questions=[
        "Is area canvassing considered prospecting or lead generation?",
        "What's the difference between active and passive prospecting, and how should I mix them?",
        "Are recruiters allowed to use a mass-texting app to reach leads?",
        "How fast do we have to contact a high-potential lead, and where is that written?",
        "What are the guideposts of the Army interview?",
        "What do I need to set up for EMM Connect on the station phones?",
        "As a station commander, how should I assess a recruiter's Army interview?",
    ],
    guardrails=COMMON_GUARDRAILS + [
        "Never recommend automated or unsolicited mass texting; cite message 21-035 when the topic comes up.",
        "Training circulars and TPs are Level 4; when they and a UM or message differ, the higher level governs.",
    ],
)

# --------------------------------------------------------------------------------------------
SEEDS["29_school_recruiting"] = dict(
    agent_type="specialist",
    description=(
        "Specialist for the School Recruiting Program, written for recruiters, station commanders and "
        "company leaders. It explains how USAREC expects secondary and postsecondary school programs to "
        "be planned and run: who owns the school plan at each echelon, the Education Services Specialist's "
        "role, high school relations and school folders in School Zone, school guidelines, ASVAB Career "
        "Exploration Program and ConAP, education incentives, release of student recruiting information "
        "(Solomon and Hutchinson Amendments, ESSA, FERPA), the high school testing program, and the current "
        "message on protection of high school students and school assignment to stations. It reads UR 350-13 "
        "(much of it PDF-only), UM 3-31, UM 3-32, UM 3-30, AR 601-210 5-10 and message 24-016. It hands "
        "educator tours and COI events to 32_coi_support_programs, ASVAB score and retest rules to "
        "05_testing_asvab, education tiers to 03_education_credentialing, and the station plan to "
        "30_station_operations."
    ),
    scope=[
        "School Recruiting Program purpose, policy and responsibilities from brigade down to recruiter",
        "Education Services Specialist (ESS) responsibilities for the school program",
        "Station and company school plans; school folders and documentation in School Zone",
        "High school relations, school profiles, school guidelines and expectations between recruiters and school officials",
        "ASVAB Career Exploration Program, March 2 Success and Concurrent Admissions Program (ConAP) as school programs",
        "Release of student recruiting information: Solomon Amendment, Hutchinson Amendment, ESSA, FERPA, student directory requests",
        "High school testing program as a school-program activity (AR 601-210 5-10)",
        "Protection of high school students and assignment of schools to stations (message 24-016)",
        "JROTC and ROTC contact as part of the school program",
    ],
    out_of_scope=[
        "Educator tours and COI events, even when educators are the audience (32_coi_support_programs)",
        "ASVAB scores, retest waiting periods and whether a student test counts for enlistment (05_testing_asvab)",
        "Education tiers, diplomas, transcripts and seniors' education credentialing (03_education_credentialing)",
        "Station recruiting plan, MAP and battle rhythm (30_station_operations)",
        "General prospecting technique (28_prospecting_leads)",
        "School market data and targeting priorities (31_market_intelligence)",
    ],
    sources=[
        dict(doc="UR_350-13", chapter="1", paragraphs=["1-1", "1-4", "1-6"],
             note="Actual title (front matter): UR 350-13 School Recruiting Programs; catalog title is wrong. Purpose, policy and responsibilities by echelon, including brigade and battalion ESS, company commander and station commander duties."),
        dict(doc="UR_350-13", chapter="2", note="The School Recruiting Plan (goals, responsibilities, brigade/battalion, company and station school plans). PDF only; not transformed."),
        dict(doc="UR_350-13", chapter="3", note="High School Relations (rapport, school profile, influencers, E/COI tours, recruiter responsibilities). PDF only."),
        dict(doc="UR_350-13", chapter="4", note="School Guidelines (annual planning meeting, expectations between recruiters and school officials). PDF only."),
        dict(doc="UR_350-13", chapter="5", note="School Zone (responsibilities, school information, filing and disposition). PDF only."),
        dict(doc="UR_350-13", chapter="6", note="School Recruiting Education Programs (ASVAB CEP, March 2 Success, ConAP). PDF only."),
        dict(doc="UR_350-13", chapter="7", note="Education Incentives and recruiter responsibilities. PDF only."),
        dict(doc="UR_350-13", chapter="8", note="Release of Student Recruiting Information (Solomon, Hutchinson, ESSA, FERPA). PDF only; appendix L has the student directory request example."),
        dict(doc="UR_350-13", chapter="9", note="HSS/FAZR and battalion ESS procedures. PDF only."),
        dict(doc="UM_3-31", chapter="4", sections=["School Recruiting Program"],
             note="Station commander's responsibility for developing the SRP and validating school folders, events and documentation."),
        dict(doc="UM_3-31", chapter="2", sections=["Running Estimates"],
             note="Use of school data to build a school prospecting plan."),
        dict(doc="UM_3-32", chapter="7", sections=["High Schools"], note="Recruiter's view of high school presence and lead generation."),
        dict(doc="UM_3-30", chapter="4", sections=["Shaping", "School Recruiting Program (SRP)"],
             note="Company expectations; text in UM_3-30/.transform/07_Planning.md."),
        dict(doc="UM_3-29", chapter="6", sections=["School Recruiting Program"], note="Brigade and battalion view of the school program."),
        dict(doc="AR_601-210", chapter="5", paragraphs=["5-10"], note="High school testing program; hand score-use and retest questions to 05_testing_asvab."),
        dict(doc="DA_PAM_601-208", chapter="7", paragraphs=["7-1"], note="JROTC as an Army outreach program."),
    ],
    messages=["24-016"],
    forms=[],
    routing_triggers=[
        "high school", "school recruiting program", "school plan", "school visit", "school folder", "School Zone",
        "educator", "ESS", "education services specialist", "student protection", "protected student", "junior",
        "student directory", "Solomon Amendment", "FERPA", "ASVAB CEP", "career exploration program", "ConAP",
        "March 2 Success", "JROTC", "college recruiting",
    ],
    hand_off_to={
        "32_coi_support_programs": "educator tours (E/COI tours) and COI events for school officials",
        "05_testing_asvab": "student ASVAB score use for enlistment, retest waiting periods",
        "03_education_credentialing": "education tier, diploma or transcript questions for students and seniors",
        "30_station_operations": "fitting the school program into the station recruiting plan and synch matrix",
        "28_prospecting_leads": "prospecting technique for students and classroom or campus face-to-face",
        "31_market_intelligence": "school market data and which schools to target",
        "33_marketing_public_affairs": "advertising support for school penetration",
        "41_policy_currency": "every answer: newest message on student protection and school assignment",
    },
    clarifying_questions=[
        "Secondary (high school) or postsecondary (college, professional school)?",
        "Is this about planning the school program, access to students and directory information, testing, or a specific student?",
        "Enlisted, AMEDD or chaplain school program?",
    ],
    flow=[
        dict(step=1, name="Identify the topic", action="Classify as program responsibilities, school plan, school relations and guidelines, School Zone documentation, education programs (ASVAB CEP, ConAP), student information release, testing, or student protection."),
        dict(step=2, name="Responsibilities", action="For who does what, read UR 350-13 1-6 for the asker's echelon and quote it; state approval or review timelines only as written there.", sources=["UR_350-13 1-4", "UR_350-13 1-6"]),
        dict(step=3, name="Program detail", action="For school plans, relations, guidelines, School Zone, education programs, incentives or information release, read the matching UR 350-13 chapter from the PDF (chapters 2 to 9 are not transformed) and cite chapter and paragraph from the PDF.", sources=["UR_350-13 Ch.2", "UR_350-13 Ch.8"]),
        dict(step=4, name="Station and company role", action="Add the station commander's SRP duties from UM 3-31 and company expectations from UM 3-30.", sources=["UM_3-31 Ch.4", "UM_3-30 Ch.4"]),
        dict(step=5, name="Student protection", action="For contact with juniors and seniors or schools outside the station's assignment, read message 24-016 and state its rules as written with the message number.", sources=["UM_3-32 Ch.7"]),
        dict(step=6, name="Testing", action="For the high school testing program, cite AR 601-210 5-10 for the program; send score and retest questions to 05_testing_asvab.", sources=["AR_601-210 5-10"]),
        dict(step=7, name="Hand off and answer", action="Fold in hand-off answers and return the requirement, who owns it, citations, and a note where the governing text is PDF-only."),
    ],
    example_questions=[
        "What does the station commander own in the School Recruiting Program?",
        "Can my recruiter contact a junior at a high school assigned to another station?",
        "What law lets us request a college's student directory, and how do we ask for it?",
        "What does the battalion ESS do for my schools?",
        "How should school events be documented in School Zone?",
        "What is ConAP and who manages it?",
    ],
    guardrails=COMMON_GUARDRAILS + [
        "UR 350-13 chapters 2 to 9 exist only in the PDF; say so when citing them and read the PDF text, never paraphrase from memory.",
        "Do not use the bare acronym SRP without spelling out School Recruiting Program (the Soldier Referral Program uses the same letters).",
    ],
)

# --------------------------------------------------------------------------------------------
SEEDS["31_market_intelligence"] = dict(
    agent_type="specialist",
    description=(
        "Specialist for recruiting market intelligence and targeting, written for station commanders, "
        "company command teams and battalion staff. It explains intelligence preparation of the "
        "operational environment (IPOE/IPB) as USAREC applies it, market analysis tools and reports "
        "(Market Intelligence Dashboard, G2 market analysis tools, market share, production to population, "
        "FQMA penetration, lifestyle segmentation), competition analysis, PMESII-PT and ASCOPE, the "
        "targeting process (event and geographic targeting, D3A), targeting boards and fusion cells, and "
        "positioning analysis and evaluation (PAE) and mission distribution. It reads UM 3-29, UM 3-30, "
        "UM 3-31, UM 3-32, UM 3-0, UTC 5-02, UR 601-73, and FM 2-0 / ADP 2-0 for the Army intelligence "
        "process. It does not supply local market facts; those come from the G2 tools at run time. It hands "
        "station zone assignment and the station plan to 30_station_operations."
    ),
    scope=[
        "Intelligence and market analysis as a recruiting function at station, company, battalion and brigade",
        "IPOE / recruiting IPB steps: define the environment, describe its effects, evaluate the competition, assess market potential",
        "PMESII-PT, METT-TC and ASCOPE as applied to a recruiting market",
        "Market analysis products and how to read them: market share, P2P, FQMA, TMA, penetration, segmentation reports",
        "Competition analysis (other services, academia, industry)",
        "Targeting process, event and geographic targeting, high-payoff event lists, targeting boards and fusion cells",
        "Positioning Analysis and Evaluation (PAE), recruiter allocation and mission analysis and distribution",
    ],
    out_of_scope=[
        "Assigning recruiting zones inside a station and building the station plan or running estimates (30_station_operations)",
        "Prospecting methods against a chosen target (28_prospecting_leads)",
        "School program rules (29_school_recruiting)",
        "Advertising buys and marketing ROI (33_marketing_public_affairs)",
        "Actual local market numbers, demographics or named local businesses: these come from G2 tools at run time, never from the agent",
    ],
    sources=[
        dict(doc="UM_3-29", chapter="3", sections=["Intelligence Preparation of the Operational Environment", "Recruiting Market Environment", "Market Competition", "Targeting Process", "Running Estimates", "Information Collection", "Information Distribution"],
             note="Brigade and battalion intelligence and market analysis, IPOE, event and geographic targeting."),
        dict(doc="UM_3-29", chapter="4", sections=["Positioning", "Mission Distribution", "Targeting Board", "Fusion Cell"],
             note="Figure 4-4 high payoff event list and Figure 4-5 synchronization matrix are in this chapter."),
        dict(doc="UM_3-30", chapter="3", sections=["The Command Team's Role In the Intelligence Process", "Intelligence Preparation", "Information Collection", "Information Dissemination", "Company Level Targeting Process"],
             note="Company level. Catalog has no chapter file; text is in UM_3-30/.transform/06_Intelligence_Information_and_Targeting.md."),
        dict(doc="UM_3-31", chapter="2", sections=["Intelligence and Market Analysis", "Recruiting Zones"],
             note="Station level: recruiters as sensors, open-source and publicly available information, ASCOPE, zone tools."),
        dict(doc="UM_3-32", chapter="6", sections=["Intelligence", "Market Analysis", "Intelligence and Market Analysis"],
             note="Recruiter's view; Figure 6-1 G-2 Market Intelligence Dashboard."),
        dict(doc="UM_3-0", chapter="4", sections=["Position, Analysis and Evaluation (PAE)", "Synchronizing Effects through the Targeting Process", "Targeting Boards", "Fusion Cells"],
             note="Command-level doctrine; appendix B (PMESII-PT and METT-TC) is in the same markdown file."),
        dict(doc="UTC_5-02", chapter="2", note="Actual title (front matter): UTC 5-02 Intelligence; catalog title is wrong. Market Analysis: steps of the recruiting IPB."),
        dict(doc="UTC_5-02", chapter="3", note="Types and location of intelligence data sources: MID, G-2 market analysis tools, G2 Maps, MAR, Power BI."),
        dict(doc="UTC_5-02", chapter="4", note="Defining the operational environment: PMESII-PT, ASCOPE, TMA, FQMA, segmentation, demographics, propensity."),
        dict(doc="UTC_5-02", chapter="5", note="Describe the environmental effects: span of control, P2P, penetration, schools."),
        dict(doc="UTC_5-02", chapter="6", note="Evaluate the threat: competition and market share, with its pitfalls."),
        dict(doc="UTC_5-02", chapter="7", note="Assess market potential: SAMA, MAR, SMR."),
        dict(doc="UR_601-73", chapter="all",
             note="Market Analysis to Support Recruiting Operations. Uses dotted numbering (5.1, 6.2); catalog extracted only 5-1/5-2. Sections 5 Recruiter Allocation, 6 Position Analysis and Evaluation, 7 Mission Analysis and Distribution, 8 Review and Implementation are in .transform/03_Contents_Listed_by_paragraph_and_page_number.md. Edition 2015; check for newer guidance."),
        dict(doc="FM_2-0", chapter="1", note="Army intelligence doctrine; use only to explain intelligence process terms the USAREC manuals borrow."),
        dict(doc="ADP_2-0", chapter="3", note="The intelligence process; background only."),
    ],
    messages=[],
    forms=[],
    routing_triggers=[
        "market", "market analysis", "market share", "IPOE", "IPB", "PMESII", "ASCOPE", "targeting",
        "targeting board", "fusion cell", "high payoff event", "event targeting", "geographic targeting",
        "demographics", "P2P", "production to population", "FQMA", "penetration", "segmentation", "MID",
        "PAE", "positioning", "mission distribution", "competition",
    ],
    hand_off_to={
        "30_station_operations": "assigning recruiting zones within the station, station running estimates, RFA/SWOT, station recruiting plan",
        "28_prospecting_leads": "how to prospect the market once targets are chosen",
        "29_school_recruiting": "school program requirements behind school targeting",
        "33_marketing_public_affairs": "advertising and marketing assets used against targeted events",
        "42_leadership_doctrine": "MDMP and general Army operations process doctrine",
    },
    clarifying_questions=[
        "Which echelon: station, company, battalion or brigade?",
        "Is this about understanding a market (analysis), choosing where and when to commit resources (targeting), or boundaries and recruiter allocation (PAE)?",
        "Which tool or report are you looking at, if any (MID, MAR, Power BI, G2 Maps)?",
    ],
    flow=[
        dict(step=1, name="Fix the echelon and question type", action="Classify as analysis (IPOE, market products), targeting (events, geography, boards, fusion cells) or positioning (PAE, allocation, mission distribution)."),
        dict(step=2, name="Load the echelon text", action="Station: UM 3-31 Ch.2. Company: UM 3-30 Ch.3. Battalion/brigade: UM 3-29 Ch.3 and Ch.4. Answer from that text with section headings.", sources=["UM_3-31 Ch.2", "UM_3-30 Ch.3", "UM_3-29 Ch.3", "UM_3-29 Ch.4"]),
        dict(step=3, name="Method and products", action="For how to run the IPB steps or read a product, use the matching UTC 5-02 chapter and label it a Level 4 training product.", sources=["UTC_5-02 Ch.2", "UTC_5-02 Ch.4", "UTC_5-02 Ch.6", "UTC_5-02 Ch.7"]),
        dict(step=4, name="Targeting", action="Explain the targeting process, event and geographic targeting, targeting boards and fusion cells from UM 3-29 and UM 3-0; name the products (high payoff event list, synch matrix).", sources=["UM_3-29 Ch.4", "UM_3-0 Ch.4"]),
        dict(step=5, name="Positioning", action="For boundary, facility or recruiter allocation questions, read UR 601-73 sections 5 to 8 and the PAE section of UM 3-0; state who approves only as written.", sources=["UR_601-73", "UM_3-0 Ch.4"]),
        dict(step=6, name="Flag data limits", action="State that numbers (market share, P2P, demographics) must come from the current G2 tools; never supply or estimate them. Note pitfalls of market share as an objective where UTC 5-02 Ch.6 discusses them.", sources=["UTC_5-02 Ch.6"]),
        dict(step=7, name="Answer and hand off", action="Return the method, the products, who owns each step, citations, and send station zone assignment and planning to 30_station_operations."),
    ],
    example_questions=[
        "What are the steps of the recruiting IPB and what product comes out of each?",
        "How do I read market share in the MID, and what are its pitfalls?",
        "What's the difference between event targeting and geographic targeting?",
        "What does a battalion targeting board do, and how does the station feed it?",
        "What is PAE and who takes part in it?",
        "How is P2P different from FQMA penetration?",
    ],
    guardrails=COMMON_GUARDRAILS + [
        "Never invent or estimate market figures, demographics or named local organizations; empty is better than wrong.",
        "Use only open-source and publicly available information as UM 3-31 Ch.2 describes; never compile information on private individuals.",
    ],
)

# --------------------------------------------------------------------------------------------
SEEDS["32_coi_support_programs"] = dict(
    agent_type="specialist",
    description=(
        "Specialist for centers of influence and Army recruiting support programs, written for recruiters, "
        "station commanders and company leaders who plan COI events or use support Soldiers. It covers COI "
        "event policy, funding and prohibitions, educator/COI tours, community partners and advocates, "
        "employer partnerships (PaYS), the Hometown and Special Recruiter Assistance Programs, Total Army "
        "Involvement in Recruiting, the Recruiting and Reserve Partnership Council, and the Soldier Referral "
        "Program and its validation. It reads AR 601-2, UR 601-2, UTC 5-03.3, UM 3-31 Ch.6 and messages "
        "22-092 and 24-006, and tells the agent to read funding and approval rules at run time rather than "
        "restating them. It hands school program rules to 29_school_recruiting, public affairs and media to "
        "33_marketing_public_affairs, and awards for referrals to 35_personnel_actions."
    ),
    scope=[
        "COI events: objectives, approved functions, frequency, funding and spending limits, procurement, prohibitions, requests and after action reports",
        "Educator/COI tours: objectives, policy, roles, tour types, nominations and evaluation",
        "Community partners, advocates, key leader engagements and community action committees",
        "Employer partnerships including Partnership for Youth Success",
        "Hometown Recruiter Assistance Program, Special Recruiter Assistance Program and ADOS-RC support Soldiers",
        "Total Army Involvement in Recruiting, GO/SES recruiting support, Recruiting and Reserve Partnership Council",
        "Soldier Referral Program referral capture and validation",
    ],
    out_of_scope=[
        "School Recruiting Program, ASVAB CEP and student directory rules (29_school_recruiting)",
        "Media engagement, public affairs and official social media (33_marketing_public_affairs)",
        "Awards such as the Army Recruiting Ribbon or recruiter badges (35_personnel_actions)",
        "Future Soldier functions and DEP/DTP gatherings detail (25_future_soldier_management)",
        "Government purchase card and property procedures beyond COI policy (37_logistics_property)",
        "Prospecting the referrals once received (28_prospecting_leads)",
    ],
    sources=[
        dict(doc="AR_601-2", chapter="2", paragraphs=["2-1", "2-2", "2-3"], note="Total Army Involvement in Recruiting program."),
        dict(doc="AR_601-2", chapter="3", paragraphs=["3-1", "3-2", "3-3"], note="General Officer/Senior Executive Service Recruiting Support Program."),
        dict(doc="AR_601-2", chapter="4", paragraphs=["4-1", "4-2", "4-3"], note="Educator/Centers of Influence Tour Program; group size and participant rules are in 4-2."),
        dict(doc="AR_601-2", chapter="5", paragraphs=["5-1", "5-2"], note="Centers of Influence Events Program; meal and funding authority in 5-2. Paragraph 5-3 (program roles) is in the PDF only."),
        dict(doc="AR_601-2", chapter="6", note="DEP/DTP gatherings. Not transformed; read the PDF."),
        dict(doc="AR_601-2", chapter="7", note="Hometown and Special Recruiter Assistance Program (HRAP 7-3, SRAP 7-4 per contents). Not transformed; read the PDF."),
        dict(doc="AR_601-2", chapter="8", paragraphs="all", note="Recruiting and Reserve Partnership Council."),
        dict(doc="UR_601-2", chapter="2", paragraphs=["2-5", "2-6", "2-7"], note="Company commander, center leader and recruiter COI responsibilities. Text in UR_601-2/.transform/00_USAREC_Regulation_601-2.md."),
        dict(doc="UR_601-2", chapter="3", paragraphs="all", note="COI policy: authority, oversight, procurement, fund utilization, spending limits, approved functions, grassroots outreach, frequency, prohibitions."),
        dict(doc="UR_601-2", chapter="4", paragraphs="all", note="Educator/COI tour program objectives, policy, responsibilities, tour types."),
        dict(doc="UR_601-2", chapter="5", note="Procedures (request process through EMM). In the same markdown file; paragraphs not extracted."),
        dict(doc="UR_601-2", chapter="6", note="After action reports. In the same markdown file; paragraphs not extracted."),
        dict(doc="UTC_5-03.3", chapter="2", note="Actual title (front matter): UTC 5-03.3 Partnerships; catalog title is wrong. Engaging community partners, advocates, key leader engagements. Level 4."),
        dict(doc="UTC_5-03.3", chapter="3", note="Employer partnerships, PaYS, P3. Level 4."),
        dict(doc="UTC_5-03.3", chapter="4", note="Partnerships with educators and educator tours (types, nominations, activities). Level 4."),
        dict(doc="UTC_5-03.3", chapter="6", note="Community action committees. Level 4."),
        dict(doc="UM_3-31", chapter="6", sections=["Internal Network", "External Network", "Community Partners"], note="Station networks and community partners."),
        dict(doc="UM_3-29", chapter="6", sections=["Community Partners (CP) and Advocates"], note="Battalion/brigade view."),
    ],
    messages=["22-092", "24-006"],
    forms=[
        "USAREC_Form_601-2.1_COI_Event_Request",
        "USAREC_Form_601-2.2_COI_Event_Afteraction_Report",
        "USAREC_Form_601-2.3_E-COI_Tour_Program_Report",
        "USAREC_Form_601-2.4_E-COI_TOUR_EVALUATION",
        "USAREC_Form_601-2.5_HRAP,_SRAP,_AND_ADOS-RC_SOLDIE",
    ],
    routing_triggers=[
        "COI", "center of influence", "COI event", "educator tour", "E/COI", "community partner", "advocate",
        "key leader engagement", "PaYS", "HRAP", "hometown recruiter", "SRAP", "special recruiter assistance",
        "ADOS-RC", "Soldier Referral Program", "referral validation", "goarmy refer", "community action committee",
        "small meal", "refreshments",
    ],
    hand_off_to={
        "29_school_recruiting": "school program, ASVAB CEP, student directory and access questions",
        "33_marketing_public_affairs": "media at events, public affairs and official social media posts about events",
        "35_personnel_actions": "Army Recruiting Ribbon and other awards tied to referrals or HRAP",
        "25_future_soldier_management": "Future Soldier functions and gatherings beyond AR 601-2 Ch.6",
        "37_logistics_property": "purchase card, procurement and property procedures",
        "28_prospecting_leads": "working the referral leads",
        "41_policy_currency": "every answer: newest message on HRAP and referral validation",
    },
    clarifying_questions=[
        "Is this a COI event, an educator tour, a support-Soldier program (HRAP/SRAP/ADOS-RC) or a Soldier referral?",
        "What stage: planning and request, execution, or after action report?",
        "Who is the audience (educators, community leaders, employers, Future Soldiers)?",
    ],
    flow=[
        dict(step=1, name="Identify the program", action="Map the question to COI events, E/COI tours, community or employer partnerships, HRAP/SRAP/ADOS-RC, Army-wide support programs, or the Soldier Referral Program."),
        dict(step=2, name="Army policy first", action="Read the AR 601-2 chapter for that program (Level 2). For HRAP/SRAP and DEP gatherings, read chapters 6 and 7 from the PDF.", sources=["AR_601-2 Ch.4", "AR_601-2 Ch.5", "AR_601-2 Ch.7"]),
        dict(step=3, name="USAREC procedure", action="Add UR 601-2 responsibilities, policy and prohibitions; quote funding limits, frequency and approval rules only as written.", sources=["UR_601-2 Ch.2", "UR_601-2 Ch.3", "UR_601-2 Ch.4"]),
        dict(step=4, name="Check prohibitions", action="Before recommending any activity or expense, read the prohibitions and approved functions and say whether the activity is listed.", sources=["UR_601-2 3-8", "UR_601-2 3-12", "AR_601-2 5-2"]),
        dict(step=5, name="Messages", action="For HRAP read message 22-092; for referrals read 24-006. State their requirements with the message number and ask 41_policy_currency for anything newer."),
        dict(step=6, name="Technique", action="For how to build partnerships, plan educator tours or run community action committees, use UTC 5-03.3 (Level 4) and UM 3-31 Ch.6.", sources=["UTC_5-03.3 Ch.2", "UTC_5-03.3 Ch.4", "UM_3-31 Ch.6"]),
        dict(step=7, name="Forms and AAR", action="Name the UF 601-2 series forms that apply (request, AAR, tour report, tour evaluation, support Soldier form).", sources=["UR_601-2 Ch.6"]),
        dict(step=8, name="Answer", action="Return policy, procedure, forms, prohibitions and citations; route awards, school and media parts per hand_off_to."),
    ],
    example_questions=[
        "Can I pay for a meal at a COI event, and where are the limits written?",
        "Who should I invite on an educator tour, and who shouldn't go?",
        "How does a Soldier's referral get credited, and how do we validate it?",
        "What does the station commander have to do when an HRAP Soldier reports in?",
        "What activities are prohibited at a COI event?",
        "Which form do I use to request a COI event and to report on it afterward?",
    ],
    guardrails=COMMON_GUARDRAILS + [
        "Never state a dollar limit, group size or frequency from memory; quote the paragraph or say it must be read.",
        "Spell out Soldier Referral Program; do not use the bare acronym SRP (it also means School Recruiting Program).",
    ],
)

# --------------------------------------------------------------------------------------------
SEEDS["33_marketing_public_affairs"] = dict(
    agent_type="specialist",
    description=(
        "Specialist for Army marketing, local advertising, public affairs, media and official social media "
        "as they touch recruiting, written for recruiters, station commanders and battalion advertising and "
        "public affairs staff. It explains the Army Marketing Program and its ROI framework, regional "
        "marketing, outreach programs, public affairs principles and responsibilities, media engagement and "
        "commanders' communication, Army funding for public affairs events, the USAREC Social Media SOP "
        "(OPSEC, PII, online conduct, branding, account requirements, records, paid promotion), virtual "
        "recruiting content, advertising assets at station level, and USAREC business cards. It reads DA PAM "
        "601-208, AR 360-1, the USAREC Social Media SOP, UTP 3-10.4, UR 25-30 and the UM chapters on "
        "advertising and public affairs. It hands prospecting use of social media to 28_prospecting_leads "
        "and COI events to 32_coi_support_programs."
    ),
    scope=[
        "Army Marketing Program fundamentals, marketing processes, ROI framework and marketing data",
        "Regional marketing system and outreach programs (JROTC, STEM, Army museums, Meet Your Army)",
        "Public affairs principles of information, responsibilities, commander's communication synchronization, countering misinformation",
        "Media visits, accreditation and official discussions with the media",
        "Public affairs resourcing and events qualifying for Army funding",
        "Official social media use in USAREC: OPSEC, PII, online conduct, messaging, branding, account requirements, records, paid promotion, reporting",
        "Virtual recruiting content creation and boosting procedures",
        "Advertising assets and battalion advertising and public affairs support to stations",
        "USAREC business cards and electronic business cards",
    ],
    out_of_scope=[
        "Using social media or texting to prospect specific leads (28_prospecting_leads)",
        "COI events and educator tours (32_coi_support_programs)",
        "Market analysis and targeting decisions (31_market_intelligence)",
        "Records retention schedules and IT security beyond the social media SOP (38_it_records_knowledge)",
        "Recruiter conduct investigations arising from online conduct (36_military_justice_command)",
    ],
    sources=[
        dict(doc="DA_PAM_601-208", chapter="1", paragraphs=["1-1", "1-5"], note="Purpose and importance of the Army Marketing Program."),
        dict(doc="DA_PAM_601-208", chapter="2", note="Fundamentals of Army Marketing. Not transformed; read the PDF."),
        dict(doc="DA_PAM_601-208", chapter="3", paragraphs="all", note="New marketing initiatives and annual marketing requirements."),
        dict(doc="DA_PAM_601-208", chapter="4", paragraphs="all", note="Return on investment framework and funnel metrics."),
        dict(doc="DA_PAM_601-208", chapter="6", paragraphs="all", note="Army Regional Marketing System."),
        dict(doc="DA_PAM_601-208", chapter="7", paragraphs="all", note="Outreach programs."),
        dict(doc="AR_360-1", chapter="1", paragraphs=["1-7", "1-11", "1-12", "1-13"], note="Principles of information, direct communication, communication synchronization, countering misinformation."),
        dict(doc="AR_360-1", chapter="2", paragraphs=["2-4", "2-5"], note="Commanders' and public affairs officers' responsibilities."),
        dict(doc="AR_360-1", chapter="3", note="Public affairs policies. Not transformed; read the PDF."),
        dict(doc="AR_360-1", chapter="5", paragraphs=["5-2", "5-3", "5-4"], note="Use of Army funds and events qualifying for Army or outside funding."),
        dict(doc="AR_360-1", chapter="6", paragraphs="all", note="Media coverage, accreditation and official discussions with the media."),
        dict(doc="AR_360-1", chapter="7", note="Public communication. Not transformed; read the PDF."),
        dict(doc="AR_360-1", chapter="8", note="Digital media management and publications (Army social media policy). Not transformed; read the PDF."),
        dict(doc="USAREC_Social_Media_SOP_21_JUN_18", chapter="all",
             note="USAREC Social Media SOP (May 2018, signed 21 Jun 2018): OPSEC and training, PII, online conduct, messaging, branding, account requirements, records, paid promotion, platforms, reporting, cease and desist. Check for a newer SOP."),
        dict(doc="UTP_3-10.4_(VRA)_V1", chapter="3", note="Roles of the commander and USAREC virtual recruiting and advertising assets. Level 4."),
        dict(doc="UTP_3-10.4_(VRA)_V1", chapter="7", note="Social media boosting procedures. Level 4."),
        dict(doc="UM_3-29", chapter="6", sections=["Advertising and Public Affairs", "Training for Media Awareness"], note="Battalion advertising and public affairs and media awareness."),
        dict(doc="UM_3-29", chapter="2", sections=["The News Media"], note="News media as part of the recruiting network."),
        dict(doc="UM_3-31", chapter="5", sections=["Advertising Assets"], note="Station use of advertising assets."),
        dict(doc="UR_25-30", chapter="all", note="Actual subject: USAREC Business Cards (roster calls it visual information; no visual information publication is in the library) (formal printed and electronic). Chapter 2 ordering detail is PDF only."),
    ],
    messages=[],
    forms=[],
    routing_triggers=[
        "social media", "post", "Facebook", "Instagram", "TikTok", "boost", "paid promotion", "advertising",
        "marketing", "public affairs", "press", "media", "reporter", "interview with a reporter", "photos",
        "video", "branding", "business cards", "RPI", "Meet Your Army", "OPSEC online",
    ],
    hand_off_to={
        "28_prospecting_leads": "direct messages and texts to specific leads as prospecting",
        "32_coi_support_programs": "COI events, educator tours and community partner events",
        "31_market_intelligence": "which markets and events to target",
        "38_it_records_knowledge": "records retention and cybersecurity beyond the social media SOP",
        "36_military_justice_command": "misconduct or investigations arising from online conduct",
        "41_policy_currency": "any newer USAREC message or SOP on social media",
    },
    clarifying_questions=[
        "Is this about an official account post, paid promotion, a media request, a local advertising or marketing asset, or business cards?",
        "Who is acting: an individual recruiter, a station page manager, or battalion APA staff?",
    ],
    flow=[
        dict(step=1, name="Classify", action="Sort the question into marketing program, public affairs or media, official social media, virtual content, advertising assets or business cards."),
        dict(step=2, name="Social media", action="Read the relevant section of the USAREC Social Media SOP (OPSEC, PII, conduct, branding, account requirements, paid promotion) and note its date; read AR 360-1 Ch.8 from the PDF when Army policy is needed.", sources=["USAREC_Social_Media_SOP_21_JUN_18", "AR_360-1 Ch.8"]),
        dict(step=3, name="Public affairs and media", action="For media requests or public communication, read AR 360-1 principles and responsibilities, media chapter, and UM 3-29 on news media and media awareness; tell the asker which office the text says to coordinate with.", sources=["AR_360-1 1-7", "AR_360-1 2-4", "AR_360-1 Ch.6", "UM_3-29 Ch.6"]),
        dict(step=4, name="Funding", action="For paying for events or advertising, read AR 360-1 5-2 to 5-4 and quote the conditions; do not state amounts.", sources=["AR_360-1 5-2", "AR_360-1 5-3"]),
        dict(step=5, name="Marketing program", action="For marketing initiatives, ROI or regional marketing, answer from DA PAM 601-208.", sources=["DA_PAM_601-208 Ch.3", "DA_PAM_601-208 Ch.4", "DA_PAM_601-208 Ch.6"]),
        dict(step=6, name="Station assets", action="For advertising assets and virtual content at station level, use UM 3-31 Ch.5 and UTP 3-10.4 (Level 4).", sources=["UM_3-31 Ch.5", "UTP_3-10.4_(VRA)_V1 Ch.7"]),
        dict(step=7, name="Answer", action="Return the rule, who approves or coordinates as written, citations, and a note that the social media SOP predates current platforms and should be confirmed with 41_policy_currency."),
    ],
    example_questions=[
        "Can my recruiter post a photo of a Future Soldier on the station's Facebook page?",
        "What OPSEC training do station social media managers need?",
        "A local reporter wants to interview my recruiter. What do I do first?",
        "Can recruiters pay to boost a social media post, and how is it reimbursed?",
        "How is marketing ROI measured in the Army Marketing Program?",
        "How do I order USAREC business cards?",
    ],
    guardrails=COMMON_GUARDRAILS + [
        "Never advise posting applicant or Future Soldier PII or images without the consent and review steps the SOP requires.",
        "Never draft content that impersonates a person or organization or uses unofficial branding.",
    ],
)

# --------------------------------------------------------------------------------------------
SEEDS["34_training_development"] = dict(
    agent_type="specialist",
    description=(
        "Specialist for training management and leader development in USAREC, written for station "
        "commanders, first sergeants, company commanders and master trainers. It explains USAREC training "
        "and leader development policy, training management and development processes (DTMS, CSTAR, ADDIE), "
        "responsibilities by echelon including the station commander as primary trainer, institutional "
        "recruiting courses and order of merit lists, mandatory training, certification programs, the "
        "Advanced Training Program and new recruiter development, training records (UF 350-1.1 near-term "
        "training plan, UF 350-1.2 training record, UF 350-1.4 reception and integration), NCO professional "
        "development, self-development and the 79R Leader Development Program, and how Army training "
        "doctrine (FM 7-0, AR 350-1) applies. It reads UR 350-1 (largely PDF-only), UM 3-31 Ch.5, UM 3-32 "
        "Ch.11, UM 3-29 Ch.7, AR 350-1, FM 7-0 and STP 805K-79R-SMTG. It hands general leadership and "
        "counseling doctrine to 42_leadership_doctrine and evaluations to 35_personnel_actions."
    ),
    scope=[
        "USAREC training and leader development policy, goals and the training management and development processes",
        "Training responsibilities by echelon, including station commanders as primary trainers",
        "Institutional recruiting courses, order of merit lists, deferments and NCOPDS for recruiters",
        "Mandatory training, certification programs and training records in DTMS and on UF 350-1 series forms",
        "Advanced Training Program and assessment of new recruiting NCOs",
        "Leader professional development, NCO professional development, self-development and the 79R Leader Development Program",
        "Reception and integration of new cadre and leader transition",
        "Army training management cycle, training meetings, AARs and evaluation as FM 7-0 describes them",
        "79R individual tasks, conditions and standards (STP 805K-79R-SMTG)",
    ],
    out_of_scope=[
        "Station planning, MAP and IPRs (30_station_operations), except where the MAP points to training gaps",
        "Prospecting and interview technique content itself (28_prospecting_leads)",
        "Evaluations, awards and assignments (35_personnel_actions)",
        "Leadership, counseling and mission command doctrine in general (42_leadership_doctrine)",
        "Height/weight certification of tapers beyond pointing to the responsibility (08_body_composition_fitness)",
        "Reclassification packets and 42T PAR submissions (35_personnel_actions)",
    ],
    sources=[
        dict(doc="UR_350-1", chapter="1", paragraphs=["1-1", "1-6", "1-7", "1-8", "1-9", "1-10"],
             note="Purpose, training challenge, goals, training management and development processes, unit training in DTMS. Paragraphs 1-11 to 1-13 (institutional training, evaluation, risk management) are in the PDF only."),
        dict(doc="UR_350-1", chapter="all",
             note="Most of UR 350-1 is PDF only: Ch.2 responsibilities by echelon (2-14 company commanders, 2-16 medical station OIC, 2-17 station commanders); Ch.3 institutional training (course information, OML, deferments, Army Recruiter Course, Station Commander Course, Master Trainer Course and others); Ch.4 training in units (mandatory training, Advanced Training Program, certification programs, training records, LPD/OPD/NCOPD, self-development); appendixes on certification, CSTAR, leader transition and new recruiting NCO boards. The catalog's 3-1, 3-2 and 4-1 entries are table captions, not paragraphs."),
        dict(doc="UM_3-31", chapter="5", sections=["Personnel Integration", "Training and Leader Development"], note="Station commander's training role; references STP 805K-79R-SMTG."),
        dict(doc="UM_3-32", chapter="11", sections=["Institutional Training Domain", "Operational Training Domain", "Self-Development", "USAREC Leader Development Program (LDP)", "Reclassification to 79R"], note="Recruiter's view of training domains and the LDP."),
        dict(doc="UM_3-30", chapter="1", sections=["Training and Leader Development"], note="Company command team view. Text in UM_3-30/.transform/04_Command_at_Company_Level.md."),
        dict(doc="UM_3-29", chapter="7", sections=["Training"], note="Brigade and battalion training; Figure 7-1 three domains of training."),
        dict(doc="AR_350-1", chapter="1", paragraphs=["1-8", "1-9", "1-12"], note="Army Training System, authorities, training domains."),
        dict(doc="AR_350-1", chapter="3", paragraphs=["3-31", "3-32", "3-33"], note="NCO Professional Development System guidance and requirements."),
        dict(doc="AR_350-1", chapter="5", note="Training in units and organizations. Not transformed; read the PDF."),
        dict(doc="FM_7-0", chapter="1", sections=["Principles of Training", "Training as Leader Development", "Training Management Cycle"]),
        dict(doc="FM_7-0", chapter="3", sections=["Training Battle Rhythm", "Long-Range Planning and Preparation", "Mid-Range Planning and Preparation", "Short-Range Planning and Preparation"]),
        dict(doc="FM_7-0", chapter="4", sections=["Training Techniques", "After Action Review", "Recording Results"]),
        dict(doc="FM_7-0", chapter="5", sections=["Evaluation", "Assessment"]),
        dict(doc="ADP_7-0", chapter="all", note="Training doctrine principles; chapters not extracted in the catalog."),
        dict(doc="STP805K-79R-SMTG", chapter="all", note="Soldier's Manual and Training Guide, MOS 79R (2018 edition): tasks, conditions, standards. Cite by task title from the PDF; check whether a 42T product supersedes it."),
        dict(doc="UTC_5-03.4", chapter="10", note="Actual title (front matter): UTC 5-03.4 Training and Leader Development; catalog title is wrong. CSTAR example and use. Level 4."),
        dict(doc="UTC_5-03.4", chapter="11", note="DTMS user guide and resources. Level 4."),
    ],
    messages=[],
    forms=[
        "USAREC_Form_350-1.1_NEAR-TERM_TRAINING_PLAN",
        "USAREC_Form_350-1.2_TRAINING_RECORD",
        "USAREC_Form_350-1.4_RECEPTION_AND_INTEGRATION_CHEC",
    ],
    routing_triggers=[
        "training plan", "near-term training plan", "training record", "UF 350-1", "DTMS", "CSTAR", "certification",
        "mandatory training", "Advanced Training Program", "new recruiter", "reception and integration",
        "NCOPDS", "NCOPD", "NCODP", "sergeant's time", "leader development program", "LDP", "self-development",
        "Army Recruiter Course", "Station Commander Course", "OML", "master trainer", "T&EO",
    ],
    hand_off_to={
        "30_station_operations": "how training fits the station battle rhythm and what the MAP shows",
        "28_prospecting_leads": "content of prospecting and Army interview training",
        "35_personnel_actions": "NCOERs, awards, assignments, reclassification and 42T PAR packets",
        "42_leadership_doctrine": "counseling, mission command and general leadership doctrine",
        "08_body_composition_fitness": "height, weight and tape procedures for cadre",
        "39_soldier_family_wellness": "risk assessment counseling and wellness programs",
    },
    clarifying_questions=[
        "Is this about planning training, recording it, a course or certification, or developing a specific recruiter or leader?",
        "Which echelon is asking: station, company or battalion?",
        "Enlisted station or AMEDD station?",
    ],
    flow=[
        dict(step=1, name="Classify", action="Sort into training management (plan, execute, record, assess), institutional courses, unit programs (mandatory training, certification, ATP), or leader development."),
        dict(step=2, name="USAREC policy", action="Read UR 350-1 Ch.1 for policy and processes; for responsibilities, courses, mandatory training, certification and ATP read the matching chapter from the PDF and cite paragraph numbers from the PDF.", sources=["UR_350-1 1-8", "UR_350-1 1-10", "UR_350-1"]),
        dict(step=3, name="Station and company role", action="Add the station commander's training role from UM 3-31 Ch.5 and company expectations from UM 3-30 Ch.1.", sources=["UM_3-31 Ch.5", "UM_3-30 Ch.1"]),
        dict(step=4, name="Records and forms", action="Name the system of record (DTMS) and the UF 350-1 forms the regulation requires, quoting where each is kept.", sources=["UR_350-1 1-10"]),
        dict(step=5, name="Army doctrine", action="When the question is how to plan or run training, use FM 7-0 (training management cycle, planning horizons, AARs, evaluation) and AR 350-1 for the Army training system and NCOPDS.", sources=["FM_7-0 Ch.1", "FM_7-0 Ch.3", "FM_7-0 Ch.4", "AR_350-1 1-12", "AR_350-1 3-31"]),
        dict(step=6, name="Tasks and standards", action="For 79R task standards, cite STP 805K-79R-SMTG by task title and note its edition date.", sources=["STP805K-79R-SMTG"]),
        dict(step=7, name="Answer", action="Return requirements, who is responsible, forms and records, citations, and state where the text is PDF-only."),
    ],
    example_questions=[
        "What has to go on my station's near-term training plan, and where is it posted?",
        "How do I record individual training done outside the training schedule?",
        "What does the Advanced Training Program require me to do with a new recruiter?",
        "How is the order of merit list used for recruiting courses?",
        "What is a CSTAR and who prepares it?",
        "How does the 79R Leader Development Program work at station level?",
    ],
    guardrails=COMMON_GUARDRAILS + [
        "UR 350-1 chapters 2 to 4 and its appendixes are PDF-only; read them, never reconstruct them from memory.",
        "Do not list UF 350-1.7 as current; the UR 350-1 summary of change says it was rescinded.",
    ],
)

# --------------------------------------------------------------------------------------------
SEEDS["35_personnel_actions"] = dict(
    agent_type="specialist",
    description=(
        "Specialist for personnel actions affecting recruiting cadre, written for station commanders, first "
        "sergeants and company commanders. It covers military awards and the USAREC awards supplement "
        "(including recruiter badges), NCO and officer evaluation reports, suspension of favorable personnel "
        "actions (flags), unfavorable information and its appeal, military personnel records, enlisted "
        "assignments, assignment and reassignment to and from recruiting duty (AR 601-1), and the current "
        "79R and DASR to 42T personnel action request messages. It reads AR 600-8-22 and its USAREC "
        "supplement, AR 623-3, DA PAM 623-3, AR 600-8-2, AR 600-37, AR 600-8-104, AR 614-200 and AR 601-1, "
        "several of which have key chapters only in the PDF. It hands Article 15, investigations and "
        "recruiter impropriety to 36_military_justice_command, retention to 18_retention_reenlistment and "
        "training records to 34_training_development."
    ),
    scope=[
        "Award principles, categories, time limits, processing and revocation; USAREC awards supplement and recruiter badges",
        "NCOER and OER preparation, rating chain, special circumstances, relief-for-cause reports and appeals",
        "Flags: actions prohibited by a flag, policy and management of flags",
        "Unfavorable information: filing in the AMHRR, memoranda of reprimand, appeals",
        "Military human resource records management and access",
        "Enlisted assignment system, deletions and deferments, stabilization",
        "Selection, assignment, reassignment, reclassification, suspension and involuntary removal from recruiting duty",
        "79R and DASR to 42T personnel action request (PAR) submissions per current messages",
    ],
    out_of_scope=[
        "Article 15, AR 15-6 investigations, recruiter impropriety and incident reporting (36_military_justice_command)",
        "Reenlistment, extensions and retention control points (18_retention_reenlistment)",
        "Training records, certifications and NCOPDS course requirements (34_training_development)",
        "Sponsorship, SFRG and family programs (39_soldier_family_wellness)",
        "Applicant enlistment records (24_processing_meps)",
        "Deciding an award, evaluation or flag; the agent gives the path, the authority decides",
    ],
    sources=[
        dict(doc="AR_600-8-22", chapter="1", paragraphs=["1-10", "1-12", "1-13", "1-14", "1-16", "1-17", "1-20", "1-21", "1-27", "1-30"],
             note="Award principles, categories, time limitation, reconsideration, character of service, interim and impact awards, announcement, revocation."),
        dict(doc="AR_600-8-22", chapter="3", note="U.S. Army individual decorations. Not transformed; read the PDF."),
        dict(doc="AR_600-8-22", chapter="4", paragraphs=["4-3", "4-4", "4-10"], note="Army Good Conduct Medal approval and processing."),
        dict(doc="AR_600-8-22", chapter="5", note="Service medals and ribbons. Not transformed; read the PDF."),
        dict(doc="AR_600-8-22", chapter="8", note="Badges and tabs, including recruiter badges. Not transformed; read the PDF."),
        dict(doc="USAREC_Suppl_1_to_AR_600_8_22", chapter="all", note="USAREC awards supplement (6 June 2019): USAREC awards program, Basic, Gold and Master Recruiter Badge criteria and permanent wear (appendix F), revocation. Predates the current AR 600-8-22 edition; check alignment."),
        dict(doc="AR_623-3", chapter="1", paragraphs=["1-9", "1-10", "1-11", "1-12"], note="Assessments, changes to reports, commander's inquiry, access."),
        dict(doc="AR_623-3", chapter="2", note="The rating chain. Not transformed; read the PDF."),
        dict(doc="AR_623-3", chapter="3", note="Army evaluation principles. Not transformed; read the PDF."),
        dict(doc="AR_623-3", chapter="4", note="Evaluation report redress program. Not transformed; read the PDF."),
        dict(doc="DA_PAM_623-3", chapter="3", paragraphs="all", note="NCOER forms and preparation, rater tendency and senior rater profile, relief for cause, addenda, corrections."),
        dict(doc="DA_PAM_623-3", chapter="2", note="OER forms and preparation (for company and battalion officers)."),
        dict(doc="DA_PAM_623-3", chapter="6", paragraphs="all", note="Constructing an evaluation report appeal."),
        dict(doc="AR_600-8-2", chapter="2", note="Policy and management of flags. Not transformed; read the PDF."),
        dict(doc="AR_600-8-2", chapter="3", paragraphs=["3-1", "3-2"], note="Actions prohibited by a flag; retention of flagged personnel."),
        dict(doc="AR_600-37", chapter="3", paragraphs="all", note="Unfavorable information in the AMHRR, including memoranda of reprimand."),
        dict(doc="AR_600-37", chapter="7", paragraphs="all", note="Appeals."),
        dict(doc="AR_600-8-104", chapter="1", paragraphs="all", note="Military human resource records management overview."),
        dict(doc="AR_614-200", chapter="1", paragraphs=["1-11"], note="Deletions and deferments."),
        dict(doc="AR_614-200", chapter="3", paragraphs=["3-1", "3-2", "3-3", "3-7"], note="Enlisted assignment system, selection criteria, preferences, stabilization."),
        dict(doc="AR_614-200", chapter="8", note="Assignment to specific type organizations or duty positions. Not transformed; read the PDF."),
        dict(doc="AR_601-1_10112016_Asg_of_Enl_Pers_to_USAREC", chapter="all",
             note="AR 601-1 (11 October 2016): Ch.2 selection and training for recruiting duty, Ch.3 assignment and reassignment, Ch.4 completion of DA-selected period and reclassification to 79R, Ch.5 voluntary and involuntary reassignment, suspension, unqualified/ineffective/unsuitable recruiters, Ch.6 AGR recruiters. Predates the 42T conversion; check current messages."),
        dict(doc="UM_3-31", chapter="5", sections=["Personnel Management", "Personnel Integration"], note="Station commander's personnel management role."),
    ],
    messages=["25-039", "25-038"],
    forms=[],
    routing_triggers=[
        "award", "AAM", "ARCOM", "MSM", "impact award", "recruiter badge", "gold badge", "NCOER", "OER",
        "evaluation", "rating chain", "relief for cause", "flag", "suspension of favorable actions", "reprimand",
        "GOMOR", "unfavorable information", "records", "iPERMS", "assignment", "PCS", "deferment", "deletion",
        "involuntary reassignment", "ineffective recruiter", "unsuitable recruiter", "PAR", "79R", "42T", "DASR",
    ],
    hand_off_to={
        "36_military_justice_command": "Article 15, AR 15-6 investigation, recruiter impropriety, incident reports behind a flag or removal",
        "18_retention_reenlistment": "reenlistment, extension or service remaining requirements raised by a PAR or assignment",
        "34_training_development": "training records, certification and course requirements",
        "39_soldier_family_wellness": "sponsorship, family and wellness programs during PCS",
        "42_leadership_doctrine": "counseling doctrine supporting evaluations or adverse actions",
        "41_policy_currency": "every answer: newest message on 42T PARs and recruiter assignment",
    },
    clarifying_questions=[
        "Which action: award, evaluation, flag, unfavorable information, records, assignment or reassignment, or 42T PAR?",
        "Is the Soldier Regular Army, Army Reserve or AGR?",
        "What is the Soldier's status on recruiting duty (new, within the DA-selected period, 79R or 42T)?",
    ],
    flow=[
        dict(step=1, name="Classify the action", action="Identify the action and the governing regulation: awards (AR 600-8-22 and USAREC supplement), evaluations (AR 623-3, DA PAM 623-3), flags (AR 600-8-2), unfavorable information (AR 600-37), records (AR 600-8-104), assignments (AR 614-200, AR 601-1)."),
        dict(step=2, name="Read the governing paragraphs", action="Load the cited paragraphs; where the governing chapter is PDF-only (flag policy, rating chain, individual decorations, badges, specific-type assignments), read the PDF and cite chapter and paragraph from it.", sources=["AR_600-8-22 1-14", "AR_623-3 Ch.2", "AR_600-8-2 Ch.2", "AR_614-200 Ch.8"]),
        dict(step=3, name="USAREC layer", action="Add the USAREC supplement for awards and badges and AR 601-1 for recruiting-duty assignment, suspension and removal.", sources=["USAREC_Suppl_1_to_AR_600_8_22", "AR_601-1_10112016_Asg_of_Enl_Pers_to_USAREC"]),
        dict(step=4, name="Flag interactions", action="When a flag exists, check what it prohibits before advising on awards, evaluations or assignments.", sources=["AR_600-8-2 3-1"]),
        dict(step=5, name="Evaluation mechanics", action="For NCOERs, use DA PAM 623-3 Ch.3 for form preparation, relief for cause and addenda, and Ch.6 for appeals.", sources=["DA_PAM_623-3 3-21", "DA_PAM_623-3 3-22", "DA_PAM_623-3 Ch.6"]),
        dict(step=6, name="42T messages", action="For 79R or DASR conversion to 42T, read messages 25-039 and 25-038 and state eligibility and procedure as written with the message number; ask 41_policy_currency for anything newer."),
        dict(step=7, name="Hand off", action="Send justice, investigation, retention and training-record parts per hand_off_to."),
        dict(step=8, name="Answer", action="Return the process, the authority named in the text, the documents involved, citations, and which parts were read from PDF-only chapters."),
    ],
    example_questions=[
        "What's the time limit for submitting an award recommendation, and where is it written?",
        "Can a flagged recruiter receive an award or PCS?",
        "How does a recruiter earn permanent wear of the Basic Recruiter Badge?",
        "What has to happen before I submit a relief-for-cause NCOER?",
        "What's the process to remove an ineffective recruiter from recruiting duty?",
        "How does a 79R submit a PAR to become a 42T?",
        "Where does a memorandum of reprimand get filed, and how can the Soldier appeal it?",
    ],
    guardrails=COMMON_GUARDRAILS + [
        "Do not request or repeat a Soldier's name, SSN or record details; work from the facts described generically.",
        "Output is a process path with citations, not a decision on an award, evaluation, flag or reassignment.",
        "AR 601-1 (2016) predates the 42T conversion; when it conflicts with a current message, present both and say which is newer.",
    ],
)
