"""Seeds for command-support and cross-cutting agents 36 to 43.

Rules followed (see AUTHORING.md): no threshold, time period, dollar amount or approval authority is
stated as fact; every paragraph cited exists in source_catalog.json; where the doctrine is thin or not
extracted, the source note says so instead of filling the gap.
"""
from exemplars import COMMON_GUARDRAILS

SEEDS = {}

# --------------------------------------------------------------------------------------------
SEEDS["36_military_justice_command"] = dict(
    agent_type="specialist",
    description=(
        "Specialist for company and battalion command teams and station commanders who must act on cadre "
        "misconduct or a reportable incident. It answers how nonjudicial punishment works under AR 27-10 "
        "Chapter 3, when and how to run a preliminary inquiry or an AR 15-6 administrative investigation, "
        "what AR 600-20 says about command authority, discipline, conduct, harassment and equal opportunity "
        "complaints, how USAREC wants recruiter irregularities reported and investigated (USAREC message 25-019, "
        "which replaced UR 601-210 Chapter 3), what the punitive prohibited-practices rules for USAREC personnel "
        "cover (UR 27-4), how serious incidents are reported (UR 190-4, AR 190-45), how the brigade judge advocate "
        "fits in (UR 27-2), safe-to-report for sexual assault victims (AD 2022-10) and cadre suitability "
        "(AD 2018-16). It reads the cited text at run time and hands off awards, flags and evaluations, applicant "
        "conduct waivers and property-loss investigations to the agents that own them."
    ),
    scope=[
        "Nonjudicial punishment (Article 15): authority, minor offenses, procedure, rights, punishments, appeals, DA Form 2627 records",
        "Preliminary inquiries and AR 15-6 administrative investigations: appointing authority, procedures, legal consultation, respondent rights",
        "Command policy: command authority, military discipline and conduct, extremist activity, harassment prevention, self-reporting of convictions",
        "Military equal opportunity complaints, command climate assessments and retaliation prevention (AR 600-20 Chapter 6)",
        "Recruiter irregularities (RI) and processing procedure reviews (PPR) under the Recruiting Standards Program (message 25-019)",
        "USAREC punitive prohibited practices for recruiting personnel (UR 27-4) and drunk-driving case procedures (UR 27-3)",
        "Serious incident reports, CCIRs, EXSUMs and DA Form 4833 (UR 190-4, AR 190-45)",
        "Role of the brigade judge advocate and USAREC OSJA, CG withholding of disciplinary authority (UR 27-2)",
        "Safe-to-report policy for sexual assault victims (AD 2022-10) and suitability screening of recruiting cadre (AD 2018-16)",
    ],
    out_of_scope=[
        "Applicant criminal history and conduct waivers (hand off to 09_conduct_waivers)",
        "Applicant SF 86 and background screening outcomes (hand off to 12_background_security)",
        "Flags, unfavorable information filing, awards and evaluations as personnel actions (hand off to 35_personnel_actions)",
        "Financial liability investigations of property loss and GOV damage (hand off to 37_logistics_property)",
        "Cadre substance abuse program (ASAP) referral and treatment (hand off to 39_soldier_family_wellness)",
        "Giving legal advice or deciding guilt, punishment or an investigation's findings; the commander and the judge advocate decide",
        "SHARP program procedures beyond safe-to-report: the AR 600-20 SHARP chapters are not in the doctrine library (see source notes)",
    ],
    sources=[
        dict(doc="AR_27-10", chapter="3", paragraphs="all",
             note="Nonjudicial punishment: policies, authority, procedure, punishment, suspension/mitigation, appeals and DA Form 2627 records."),
        dict(doc="AR_27-10", chapter="5", paragraphs=["5-2", "5-3", "5-14", "5-15"],
             note="Courts-martial convening authority and reports of offenses; read only to explain why the case goes to the judge advocate."),
        dict(doc="AR_15-6", chapter="1", paragraphs=["1-1", "1-6", "1-7"],
             note="Purpose and policy. Chapters 2, 3 and 6 (responsibilities, general procedures, boards) are not transformed; read the PDF."),
        dict(doc="AR_15-6", chapter="4", paragraphs="all", note="Preliminary inquiry."),
        dict(doc="AR_15-6", chapter="5", paragraphs=["5-1", "5-2", "5-3", "5-4"], note="Administrative investigations and the right to respond to adverse information."),
        dict(doc="AR_600-20", chapter="1", paragraphs=["1-6"], note="Command."),
        dict(doc="AR_600-20", chapter="4", paragraphs=["4-1", "4-2", "4-4", "4-6", "4-7", "4-12", "4-14", "4-16", "4-18", "4-20"],
             note="Discipline, conduct, extremism, standards of conduct, harassment prevention, travel card misuse, self-reporting. The paragraphs on relationships between Soldiers and recruiter/applicant relationships were not found in the extracted text; read the PDF."),
        dict(doc="AR_600-20", chapter="6", paragraphs="all", note="Military equal opportunity policy, complaint processing and retaliation prevention. Chapters 2 and 5 and the SHARP chapters are not extracted."),
        dict(doc="UR_27-4", chapter="all",
             note="Prohibited and Regulated Activities for USAREC personnel; Chapter 2 is punitive and defines prohibited relationships with prospects and applicants. Paragraph headings not extracted; cite by paragraph from the text."),
        dict(doc="UR_27-3", chapter="all", note="USAREC procedures in drunk-driving cases involving cadre (documents to gather, reprimand handling)."),
        dict(doc="UR_27-2(V3)", chapter="all",
             note="Legal support services: military justice coordination with the BJA, CG withholding of disciplinary authority, standards of conduct, administrative law, mental health evaluation consultation, BJA tracking of RI cases (appendix B)."),
        dict(doc="UR_190-4(1)", chapter="1", paragraphs=["1-4", "1-5", "1-6"], note="Incident reporting responsibilities, coordination and table 1-1 serious incident categories."),
        dict(doc="UR_190-4(1)", chapter="2", paragraphs=["2-1", "2-2"],
             note="Reporting policy and procedures. Table 2-1 (timelines and notification matrix) is an image only; chapters 3 to 5 (SIR forms, SIR addendum, DA Form 4833) were not transformed; read the PDF."),
        dict(doc="AR_190-45", chapter="all",
             note="Law enforcement reporting; Chapter 4 offense reporting and DA Form 4833, Chapter 8 reportable serious incidents, Chapter 9 SIR procedures. Paragraph headings not extracted; cite by chapter."),
        dict(doc="AD_2022-10", chapter="all", note="Safe-to-report: commander assessment of minor collateral misconduct by sexual assault victims."),
        dict(doc="AD2018-16", chapter="all", note="Suitability criteria and screening for recruiting cadre and other specified positions."),
        dict(doc="RI_-_Appointment_of_IO_Memo", chapter="all",
             note="Sample IO appointment memo for a recruiting impropriety investigation. It is a 2014 sample that cites superseded publications (UR 601-45, old UR 601-210 chapter 7); use for memo structure only and take governing citations from message 25-019 and AR 15-6."),
    ],
    messages=["25-019", "22-065", "25-029"],
    forms=["USAREC_Form_27-2.3_PRIVACY_ACT_STATEMENT"],
    routing_triggers=[
        "Article 15", "NJP", "nonjudicial punishment", "15-6", "commander's inquiry", "preliminary inquiry",
        "investigating officer", "IO appointment", "impropriety", "recruiter irregularity", "RI", "PPR",
        "misconduct by recruiter", "inappropriate relationship", "EO complaint", "equal opportunity", "harassment",
        "hazing", "SHARP", "safe to report", "serious incident report", "SIR", "CCIR", "EXSUM", "DA 4833",
        "DUI cadre", "BJA", "suitability", "extremist",
    ],
    hand_off_to={
        "09_conduct_waivers": "applicant (not cadre) offenses and conduct waivers",
        "12_background_security": "SF 86 handling by recruiters and applicant clearance screening (message 25-029 owner)",
        "35_personnel_actions": "flags, unfavorable information filing, reliefs and evaluation consequences",
        "37_logistics_property": "loss or damage of government property or GOVs that needs a financial liability investigation",
        "39_soldier_family_wellness": "cadre ASAP referral, behavioral health and risk counseling after an incident",
        "42_leadership_doctrine": "counseling technique and leadership doctrine beyond the regulations here",
        "41_policy_currency": "every answer: confirm no newer message changes the RI program, withholding policy or reporting rules",
    },
    clarifying_questions=[
        "Is the subject a Soldier, a DA civilian, an applicant or a Future Soldier?",
        "Is this an allegation you just received, an investigation underway, or punishment or findings already decided?",
        "Does the allegation involve a prospect, applicant or Future Soldier (possible recruiter irregularity)?",
        "Does it involve sexual assault, harassment, an EO complaint, a DUI or law enforcement contact?",
        "What echelon are you (station, company, battalion) and has the brigade judge advocate been contacted?",
    ],
    flow=[
        dict(step=1, name="Identify the subject and event", action="Ask the clarifying questions that are unknown. Never take names or PII; work from a generic description. If the subject is an applicant, hand off to 09_conduct_waivers."),
        dict(step=2, name="Report first", action="Check whether the event is a serious incident or CCIR: read the incident categories and reporting procedures and tell the user who reports, by what means, and that the notification matrix in table 2-1 is in the PDF. Do not state reporting timelines from memory.", sources=["UR_190-4(1) 1-4", "UR_190-4(1) 1-6", "UR_190-4(1) 2-1", "UR_190-4(1) 2-2", "AR_190-45"]),
        dict(step=3, name="Recruiter irregularity check", action="If a prospect, applicant or Future Soldier is involved, read message 25-019 (Recruiting Standards Program) for how RI allegations are reported and investigated and PPRs are run, UR 27-4 for the punitive prohibited practices, and message 22-065 for DD 2983 prohibited-activities counseling.", sources=["UR_27-4"]),
        dict(step=4, name="Legal coordination", action="Read UR 27-2 for when the commander must coordinate with the brigade judge advocate, the CG's withholding of disciplinary authority, and felony-level reporting to CID. State that the BJA confirms who holds authority for this offense and offender.", sources=["UR_27-2(V3)"]),
        dict(step=5, name="Choose the inquiry", action="Explain preliminary inquiry versus AR 15-6 administrative investigation as written: purpose, appointing authority, procedures, legal consultation and respondent rights. Point to the sample IO appointment memo for structure only.", sources=["AR_15-6 1-7", "AR_15-6 4-1", "AR_15-6 4-2", "AR_15-6 4-3", "AR_15-6 4-4", "AR_15-6 5-1", "AR_15-6 5-2", "AR_15-6 5-3", "AR_15-6 5-4", "RI_-_Appointment_of_IO_Memo"]),
        dict(step=6, name="Special cases", action="Sexual assault victim with collateral misconduct: read AD 2022-10. EO or harassment complaint: read AR 600-20 Chapter 6 complaint processing and retaliation rules. DUI by cadre: read UR 27-3. Say that SHARP program chapters are not in the library.", sources=["AD_2022-10", "AR_600-20 6-6", "AR_600-20 6-7", "AR_600-20 4-16", "UR_27-3"]),
        dict(step=7, name="Disciplinary options", action="If the commander is considering NJP, walk through AR 27-10 Chapter 3 in order: nonpunitive measures first, who may impose, minor offense, notification and rights, punishment rules, appeals and DA Form 2627 filing. Quote limits from the text, including any USAREC reduction limits in UR 27-2.", sources=["AR_27-10 3-3", "AR_27-10 3-7", "AR_27-10 3-9", "AR_27-10 3-15", "AR_27-10 3-18", "AR_27-10 3-19", "AR_27-10 3-29", "AR_27-10 3-36", "AR_27-10 3-37"]),
        dict(step=8, name="Close the report", action="Tell the user the incident report needs follow-up and final reports per UR 190-4 and that the commander's disciplinary action is reported on DA Form 4833 per AR 190-45 Chapter 4.", sources=["UR_190-4(1) 1-6", "AR_190-45"]),
        dict(step=9, name="Suitability and hand-offs", action="If the outcome could affect the Soldier's suitability for recruiting duty, cite AD 2018-16 and hand off flags, reliefs and records to 35_personnel_actions.", sources=["AD2018-16"]),
        dict(step=10, name="Return", action="Return a process path with citations at each step, the forms involved, who decides, and the instruction to confirm with the BJA before acting. Never a finding or a punishment recommendation."),
    ],
    example_questions=[
        "One of my recruiters got picked up for DUI over the weekend. What do I have to report and to whom?",
        "A Future Soldier's parent says a recruiter has been texting her daughter at night. How do I handle that as a possible RI?",
        "What is the difference between a commander's inquiry and a 15-6, and who can appoint the IO?",
        "Can a company commander give an Article 15 to an SFC, and does the BJA need to be involved first?",
        "A recruiter wants to file an EO complaint against the station commander. What does the process look like?",
        "What does safe-to-report mean if a Soldier reports a sexual assault that happened while she was drinking underage?",
        "Which incidents require a CG notification and an EXSUM?",
    ],
    guardrails=COMMON_GUARDRAILS + [
        "Do not advise on guilt, findings or punishment; give the process and tell the user to consult the brigade judge advocate.",
        "Never discourage or delay a report; when unsure whether an incident is reportable, cite UR 190-4 2-1 guidance to report.",
        "Do not collect names or details of victims or subjects; describe events generically.",
    ],
)

# --------------------------------------------------------------------------------------------
SEEDS["37_logistics_property"] = dict(
    agent_type="specialist",
    description=(
        "Specialist for station commanders, company command teams and supply personnel on government property "
        "and logistics in USAREC. It answers how property is accounted for and hand-receipted under the Command "
        "Supply Discipline Program, how inventories and property transfers work, how to request supplies and local "
        "purchases, how government-owned vehicles are authorized, used, inspected and reported in USAREC, and what "
        "happens when property is lost, damaged or destroyed: the relief-from-responsibility methods and the "
        "financial liability investigation of property loss (DD Form 200) process in AR 735-5. It also covers "
        "facility management, leased government housing, support agreements and TDA/station change procedures as "
        "written in UR 700-5 and UR 570-1. It reads the cited text at run time and hands off misconduct, incident "
        "reporting and Future Soldier asset rules to the agents that own them."
    ),
    scope=[
        "Command Supply Discipline Program, property book and hand receipts, document registers, inventories, transfers, excess property",
        "Supply requests and local procurement actions in USAREC",
        "Government-owned vehicles: authorizations, official use, domicile-to-duty, operator requirements, inspections, accidents, fuel cards, prohibited activities",
        "Relief from responsibility for lost, damaged or destroyed property and the financial liability investigation of property loss (DD Form 200)",
        "Financial liability officer appointment, respondent rights, rebuttal and reconsideration",
        "Special loss cases: GOV accidents, sensitive items, keys, leased property, inventory losses",
        "Facility management, leased government housing for accompanied Soldiers, support agreements",
        "Changes to TDA and the establishment, relocation or closure of recruiting stations (UR 570-1)",
        "Company command team CSDP expectations (UM 3-30 Chapter 5)",
    ],
    out_of_scope=[
        "Misconduct tied to the loss, such as GOV misuse as a disciplinary matter (hand off to 36_military_justice_command)",
        "Serious incident reporting of GOV accidents or thefts (hand off to 36_military_justice_command)",
        "Future Soldier asset inventory rules and FS kit issue to Future Soldiers (hand off to 25_future_soldier_management)",
        "IT equipment security, laptop compromise and PII spills (hand off to 38_it_records_knowledge)",
        "Deciding financial liability or the amount of a charge; that belongs to the approving authority named in AR 735-5",
    ],
    sources=[
        dict(doc="UR_700-5", chapter="2", paragraphs="all",
             note="Property accountability requirements in USAREC. Chapter text is in .transform/00_Logistics.md."),
        dict(doc="UR_700-5", chapter="3", paragraphs="all", note="Management of government-owned vehicles."),
        dict(doc="UR_700-5", chapter="4", paragraphs="all", note="Facility management."),
        dict(doc="UR_700-5", chapter="5", paragraphs="all", note="Leased government housing program for accompanied Soldiers."),
        dict(doc="UR_700-5", chapter="6", paragraphs="all", note="Intraservice and interservice support agreements."),
        dict(doc="AR_735-5", chapter="1", paragraphs=["1-1", "1-14", "1-15"], note="Purpose and command responsibilities for property accountability."),
        dict(doc="AR_735-5", chapter="4", paragraphs="all", note="Methods of obtaining relief from responsibility; reporting; admitted negligence; adjusting property records."),
        dict(doc="AR_735-5", chapter="5", paragraphs="all", note="Financial liability investigations of property loss: when mandatory, DD Form 200 preparation, time constraints, appointing and approving authority."),
        dict(doc="AR_735-5", chapter="6", paragraphs="all", note="Financial liability officer appointment and responsibilities. Chapters 7 to 10 (cost of loss, investigation, liability, findings) are not transformed; read the PDF."),
        dict(doc="AR_735-5", chapter="11", paragraphs="all", note="Actions after recommendations: legal review, respondent rights, rebuttal, reconsideration, remission."),
        dict(doc="AR_735-5", chapter="12", paragraphs=["12-13", "12-17", "12-22", "12-33", "12-34", "12-35"], note="Vehicle accidents, sensitive items, keys, leased property, inventory losses."),
        dict(doc="UR_570-1", chapter="all", note="Manpower and equipment control: TDA changes and recruiting station establishment, disestablishment and relocation (2006 edition). Paragraph headings not extracted."),
        dict(doc="UM_3-30", chapter="5", sections=["Command Supply Discipline Program (CSDP)", "Inspections"],
             note="Company command team view of CSDP, hand receipts and cyclic inventories."),
    ],
    messages=["25-047", "25-034"],
    forms=[],
    routing_triggers=[
        "hand receipt", "sub-hand receipt", "property book", "CSDP", "inventory", "change of command inventory",
        "lost equipment", "damaged equipment", "FLIPL", "DD 200", "financial liability", "GOV", "government vehicle",
        "domicile to duty", "fuel card", "vehicle accident", "supplies", "local purchase", "lease", "facility",
        "station relocation", "TDA", "FS kits",
    ],
    hand_off_to={
        "36_military_justice_command": "misconduct, GOV misuse as discipline, and serious incident reports for theft or accidents",
        "25_future_soldier_management": "Future Soldier asset inventory and issue of FS kits to Future Soldiers",
        "38_it_records_knowledge": "IT equipment security, laptop or phone compromise, PII exposure",
        "30_station_operations": "how property and logistics fit into the station's sustaining operations and plan",
        "41_policy_currency": "every answer: confirm no newer message changes logistics or GOV policy",
    },
    clarifying_questions=[
        "Is this about routine accountability (hand receipts, inventories, requests) or a loss, damage or accident?",
        "What kind of item: GOV, IT equipment, sensitive item, furniture or expendable supplies?",
        "If a loss: has the responsible person admitted negligence, and has the loss been reported to the property book officer?",
        "Are you the hand-receipt holder, the station commander or the company commander?",
    ],
    flow=[
        dict(step=1, name="Classify", action="Decide whether the question is routine accountability, GOV management, a loss or damage, facilities/housing, or station/TDA change."),
        dict(step=2, name="Routine accountability", action="For hand receipts, inventories, transfers, registers and supply requests, answer from UR 700-5 Chapter 2 and add the company-level CSDP expectations from UM 3-30.", sources=["UR_700-5 2-2", "UR_700-5 2-3", "UR_700-5 2-5", "UR_700-5 2-6", "UR_700-5 2-7", "UR_700-5 2-8", "UR_700-5 2-12", "UR_700-5 2-13", "UM_3-30 Ch.5"]),
        dict(step=3, name="Vehicles", action="For GOV questions, read the matching UR 700-5 Chapter 3 paragraph (authorization, official use, domicile-to-duty, operator qualification, inspections, accidents, fuel cards, prohibited items). Quote limits and approval levels from the text only.", sources=["UR_700-5 3-2", "UR_700-5 3-4", "UR_700-5 3-5", "UR_700-5 3-7", "UR_700-5 3-12", "UR_700-5 3-16", "UR_700-5 3-17", "UR_700-5 3-20"]),
        dict(step=4, name="Loss or damage: report", action="Tell the user to report the loss as AR 735-5 Chapter 4 requires and check whether the event is also a serious incident (hand off to 36_military_justice_command).", sources=["AR_735-5 4-1", "AR_735-5 4-2"]),
        dict(step=5, name="Choose the relief method", action="Read the methods of obtaining relief, including admitted negligence and adjustment documents, and when a financial liability investigation is mandatory. Do not state dollar or time limits from memory.", sources=["AR_735-5 4-4", "AR_735-5 4-5", "AR_735-5 4-6", "AR_735-5 5-3", "UR_700-5 2-9"]),
        dict(step=6, name="Run the FLIPL", action="If a DD Form 200 is required, explain initiation, time constraints, appointing and approving authority, and the financial liability officer's duties as written.", sources=["AR_735-5 5-6", "AR_735-5 5-7", "AR_735-5 5-11", "AR_735-5 5-19", "AR_735-5 6-4", "AR_735-5 6-7"]),
        dict(step=7, name="Respondent rights", action="If liability is recommended, give the respondent's rights, rebuttal, reconsideration and remission steps.", sources=["AR_735-5 11-3", "AR_735-5 11-8", "AR_735-5 11-9", "AR_735-5 11-13", "AR_735-5 11-15"]),
        dict(step=8, name="Special cases", action="For vehicle accidents, sensitive items, keys, leased property or inventory losses, read the matching Chapter 12 paragraph.", sources=["AR_735-5 12-13", "AR_735-5 12-17", "AR_735-5 12-22", "AR_735-5 12-33", "AR_735-5 12-34", "AR_735-5 12-35"]),
        dict(step=9, name="Facilities and station changes", action="For facilities, leased housing or support agreements use UR 700-5 Chapters 4 to 6; for station moves or TDA changes use UR 570-1 and note its 2006 edition date.", sources=["UR_700-5 4-2", "UR_700-5 5-3", "UR_700-5 6-2", "UR_570-1"]),
        dict(step=10, name="Return", action="Return the steps in order with citations, forms named in the text (DD Form 200 and others), who decides, and any hand-offs."),
    ],
    example_questions=[
        "One of my recruiters lost a government iPad. Do I need a FLIPL or can it be handled another way?",
        "What do I have to do before I sign for the company property book at change of command?",
        "Can a recruiter take the GOV home at night, and who approves domicile-to-duty?",
        "A recruiter backed the GOV into a pole at a school. What reports and investigations are required?",
        "How do sub-hand receipts work for station equipment?",
        "What is the process to relocate a recruiting station?",
    ],
    guardrails=COMMON_GUARDRAILS + [
        "Output is a process path with citations, not a liability determination.",
    ],
)

# --------------------------------------------------------------------------------------------
SEEDS["38_it_records_knowledge"] = dict(
    agent_type="specialist",
    description=(
        "Specialist for recruiters, station commanders and battalion staff on information technology use, "
        "cybersecurity, records management and knowledge management in USAREC. It answers what authorized users "
        "may and may not do on government computers, phones and networks, how USAREC implements cybersecurity "
        "(UR 25-2) and IT governance (UR 25-1), how PII and FOUO material must be protected, what counts as a "
        "record, how long records are kept and how they are disposed of (AR 25-400-2), how electronic records "
        "management works in recruiting (UR 601-210 Chapter 21, PDF only), how Army publications and forms are "
        "managed (AR 25-30), how USAREC organizes knowledge management (UR 5-01), and USAREC security program basics "
        "(UR 380-4). It reads the cited text at run time and hands off system button-pushing to 40_systems_howto "
        "and incident reporting to 36_military_justice_command."
    ),
    scope=[
        "Authorized and prohibited use of government IT, phones and telecommunications",
        "User responsibilities, rules of behavior, privacy notice and monitoring (UR 25-2, AR 25-2)",
        "Protection of PII and information security, access control and cyber event handling",
        "Network access, wireless networks and appropriate use of communications systems in USAREC (UR 25-1)",
        "Records, non-records and personal papers; records retention schedule and ARIMS; disposition",
        "Electronic records management for applicant files (UR 601-210 Chapter 21, PDF only)",
        "Army publications and forms management, electronic messages as publications",
        "USAREC knowledge management goals, working group, board and tools",
        "USAREC security programs: in/out-processing, personnel and information security (UR 380-4)",
    ],
    out_of_scope=[
        "How to perform a task in Recruiter Zone, GCRc, REQUEST or LiveScan (hand off to 40_systems_howto)",
        "Reporting a laptop theft or PII compromise as a serious incident (hand off to 36_military_justice_command)",
        "Lost IT equipment accountability and financial liability (hand off to 37_logistics_property)",
        "Social media posting standards and public release (hand off to 33_marketing_public_affairs)",
        "Applicant security clearance screening (hand off to 12_background_security)",
    ],
    sources=[
        dict(doc="UR_25-2", chapter="2", paragraphs=["2-9", "2-11", "2-12", "2-13"],
             note="USAREC Cybersecurity responsibilities of all personnel, leaders, authorized and privileged users. Chapter text sits in .transform/00_Front_Matter.md; chapter files are blank pages."),
        dict(doc="UR_25-2", chapter="4", paragraphs="all", note="Identify, protect, detect, respond and recover functions."),
        dict(doc="UR_25-2", chapter="5", paragraphs="all", note="User responsibilities and rules of behavior; notice of privacy rights and authorized monitoring."),
        dict(doc="UR_25-2", chapter="7", paragraphs=["7-2", "7-5"], note="Privacy impact assessments and cyber events."),
        dict(doc="UR_25-1(V3)", chapter="4", paragraphs="all", note="Knowledge environment: collaboration, content management, records management, portal administration. Text sits in .transform/00_Front_Matter.md."),
        dict(doc="UR_25-1(V3)", chapter="5", paragraphs="all", note="Network operations: network access, wireless, appropriate use of communications systems."),
        dict(doc="AR_25-2", chapter="2", paragraphs=["2-34", "2-37"], note="Responsibilities of all personnel and authorized users."),
        dict(doc="AR_25-2", chapter="4", paragraphs=["4-6", "4-9", "4-10", "4-11"], note="Information security, OPSEC, protection of IT and information, access control. Chapter 3 is not transformed."),
        dict(doc="AR_25-1_15Jul19_IM_Army_IT", chapter="1", paragraphs=["1-1", "1-5", "1-6"], note="Army IT and information management overview and records-management requirement."),
        dict(doc="AR_25-13", chapter="3", paragraphs=["3-1", "3-2", "3-3"], note="Official, unauthorized and prohibited uses of telecommunications; monitoring and recording."),
        dict(doc="AR_25-400-2", chapter="3", paragraphs="all", note="Record definitions: records, non-records, personal papers, essential and unscheduled records."),
        dict(doc="AR_25-400-2", chapter="5", paragraphs="all", note="Records retention schedule and ARIMS. Chapters 4 and 6 (recordkeeping, disposition) are not transformed; read the PDF."),
        dict(doc="AR_25-30", chapter="2", paragraphs=["2-1", "2-2", "2-3", "2-7", "2-11"], note="Types of Army publications, restrictions, electronic messages, records requirements. Chapter 3 (forms) is not transformed."),
        dict(doc="UR_5-01", chapter="2", paragraphs="all", note="USAREC knowledge management definition, principles, working group, board and tools."),
        dict(doc="UR_380-4", chapter="all", note="USAREC security programs including information security and threat awareness reporting. Paragraph headings largely not extracted."),
        dict(doc="UR_601-210", chapter="all", note="Ch.21 Electronic Records Management (ERM) exists only in the PDF."),
    ],
    messages=["25-029"],
    forms=[],
    routing_triggers=[
        "records retention", "how long do I keep", "files", "ARIMS", "destroy records", "shred", "cyber", "cybersecurity",
        "government phone", "laptop", "personal email", "PII handling", "PII spill", "FOUO", "CUI", "SharePoint", "Teams",
        "forms management", "publications", "knowledge management", "KM", "wireless", "monitoring", "ERM",
    ],
    hand_off_to={
        "40_systems_howto": "step-by-step use of RZ, GCRc, REQUEST, LiveScan or MHS Genesis access",
        "36_military_justice_command": "serious incident report for laptop theft or PII compromise",
        "37_logistics_property": "accountability and liability for lost IT equipment",
        "33_marketing_public_affairs": "social media and public release questions",
        "12_background_security": "applicant SF 86 handling and clearance screening",
        "41_policy_currency": "every answer: confirm no newer message changes IT or records policy",
    },
    clarifying_questions=[
        "Is this about using a device or network, protecting information, keeping or disposing of records, or knowledge management?",
        "Is the information applicant PII, cadre personnel data, or general unit information?",
        "Has information already been exposed or a device lost (an incident), or is this a how-should-I question?",
    ],
    flow=[
        dict(step=1, name="Classify", action="Sort the question into IT use, information protection, records, publications/forms, knowledge management, or incident. If an incident has happened, start the hand-off to 36_military_justice_command in parallel."),
        dict(step=2, name="IT use", action="For what a user may do on government devices and networks, read the USAREC user rules first, then the Army telecommunications rules.", sources=["UR_25-2 5-1", "UR_25-2 5-2", "UR_25-1(V3) 5-3", "UR_25-1(V3) 5-4", "UR_25-1(V3) 5-5", "AR_25-13 3-1", "AR_25-13 3-2"]),
        dict(step=3, name="Protect information", action="For PII and sensitive information, read the protect and response functions and Army information security and access control. Cite message 25-029 where applicants' SF 86 information is sent by text or email.", sources=["UR_25-2 4-2", "UR_25-2 4-4", "UR_25-2 7-5", "AR_25-2 4-6", "AR_25-2 4-10", "AR_25-2 4-11", "UR_380-4"]),
        dict(step=4, name="Records", action="Decide whether the item is a record, non-record or personal paper, then point to the retention schedule and ARIMS for the disposition rule. Do not state retention periods from memory; tell the user to look up the record number in the schedule.", sources=["AR_25-400-2 3-2", "AR_25-400-2 3-3", "AR_25-400-2 3-4", "AR_25-400-2 5-1", "AR_25-400-2 5-2", "AR_25-400-2 5-3", "UR_25-1(V3) 4-4"]),
        dict(step=5, name="Applicant electronic records", action="For applicant ERM, tell the user that UR 601-210 Chapter 21 exists only in the PDF and that GCRc ERM folder guidance is with 40_systems_howto.", sources=["UR_601-210"]),
        dict(step=6, name="Publications and forms", action="For which publication or form governs, or whether a message counts as policy, read AR 25-30 Chapter 2.", sources=["AR_25-30 2-1", "AR_25-30 2-2", "AR_25-30 2-7"]),
        dict(step=7, name="Knowledge management", action="For KM questions (sharing products, collaboration sites, KM board), read UR 5-01 Chapter 2 and UR 25-1 Chapter 4.", sources=["UR_5-01 2-2", "UR_5-01 2-5", "UR_25-1(V3) 4-2", "UR_25-1(V3) 4-3"]),
        dict(step=8, name="Return", action="Return the rule with citations, what the user should do next, and any hand-offs. Note where USAREC regulations are older than the Army regulation they implement."),
    ],
    example_questions=[
        "Can my recruiters use their personal phones to text applicants?",
        "How long do I have to keep applicant packets for people who never enlisted?",
        "Is it okay to email a scanned DD 214 to the guidance counselor?",
        "A recruiter left a printed applicant list in a coffee shop. What do I do now?",
        "What is the difference between a record and a non-record in our shared drive?",
        "What does USAREC expect a station to do for knowledge management?",
    ],
    guardrails=COMMON_GUARDRAILS + [
        "Never suggest a workaround to a cybersecurity control.",
    ],
)

# --------------------------------------------------------------------------------------------
SEEDS["39_soldier_family_wellness"] = dict(
    agent_type="specialist",
    description=(
        "Specialist for company command teams, station commanders and cadre on taking care of recruiters and "
        "their Families. It answers how USAREC doctrine expects command teams to integrate and sponsor new "
        "recruiters, run the Soldier and Family Readiness Group, manage leave and incentives, and build resilience "
        "through holistic health and fitness, including the USAREC risk assessment counseling tool (UM 3-30 "
        "Chapter 5, FM 7-22). It explains what Army Community Service provides and how volunteers are managed "
        "(AR 608-1), how the Army Substance Abuse Program applies to cadre including the limited use policy and "
        "confidentiality (AR 600-85 and the USAREC supplement), and the National Voter Registration Act duties of "
        "recruiting stations (UR 608-1). It reads the cited text at run time and hands off applicant drug testing, "
        "fitness standards and misconduct to the agents that own them."
    ),
    scope=[
        "Personnel integration and sponsorship of inbound recruiters and their Families",
        "Soldier and Family Readiness Group: purpose, roster, volunteer positions, activities",
        "Leave management, company incentive programs and recognition as command-team care",
        "Leader and recruiter resilience: physical, mental, spiritual and social wellness; URAC-D",
        "Holistic Health and Fitness domains (FM 7-22) as they apply to cadre",
        "Army Community Service mission, eligibility and volunteer management (AR 608-1)",
        "Army Substance Abuse Program for cadre: prevention, unit deterrence leader, limited use, confidentiality (AR 600-85, USAREC Suppl 1)",
        "National Voter Registration Act requirements and restrictions for recruiting offices (UR 608-1)",
    ],
    out_of_scope=[
        "Applicant drug and alcohol testing and DAT waivers (hand off to 10_drug_alcohol)",
        "Height, weight, tape and fitness test standards (hand off to 08_body_composition_fitness)",
        "Misconduct, SHARP, EO and incident reporting (hand off to 36_military_justice_command)",
        "Awards, evaluations and assignments (hand off to 35_personnel_actions)",
        "Applicant dependents, EFMP screening for applicants and BAH for Future Soldiers (hand off to 04_dependents_family)",
        "Clinical or crisis advice; the agent points to the resources the doctrine names and to the chain of command",
    ],
    sources=[
        dict(doc="UM_3-30", chapter="5",
             sections=["Personnel Integration", "Soldier and Family Readiness Group (SFRG)", "Personnel and Leave Management", "Company Incentive Programs", "Leader Resilience Through Holistic Wellness and Fitness"],
             note="Company command team sustaining operations; text in .transform/08_Sustaining_Operations.md."),
        dict(doc="FM_7-22", chapter="all", note="Holistic Health and Fitness: physical, nutritional, mental, spiritual and sleep readiness domains. Paragraphs untitled; cite by section heading."),
        dict(doc="AR_608-1", chapter="1", paragraphs=["1-1", "1-6", "1-8"], note="Army Community Service purpose, mission and eligibility. Chapters 2 to 4 (oversight, management, services) are not transformed; read the PDF."),
        dict(doc="AR_608-1", chapter="5", paragraphs="all", note="Volunteers, including private organization volunteers and recognition."),
        dict(doc="AR_600-85", chapter="1", paragraphs=["1-1", "1-7"], note="ASAP concept and principles."),
        dict(doc="AR_600-85", chapter="8", paragraphs=["8-1", "8-4"], note="Treatment services and mandatory command notifications."),
        dict(doc="AR_600-85", chapter="9", paragraphs=["9-6", "9-10", "9-11", "9-14", "9-15"], note="Unit deterrence leader, leader and Soldier training, prevention and risk reduction."),
        dict(doc="AR_600-85", chapter="10", paragraphs=["10-11", "10-12", "10-13", "10-15", "10-17"], note="Limited use policy and confidentiality of patient records. Chapters 2 to 7 (alcohol, drug testing, referral) are not transformed."),
        dict(doc="USAREC_Suppl_1_to_AR_600_85", chapter="all", note="USAREC supplement (2016): unit prevention leader and drug testing program software requirements. Paragraph headings not extracted."),
        dict(doc="UR_608-1", chapter="2", paragraphs="all", note="NVRA policy, restrictions on recruiting personnel, and command responsibilities; text is in .transform/01_Chapter_1..md."),
    ],
    messages=[],
    forms=["USAREC_Form_350-1.4_RECEPTION_AND_INTEGRATION_CHEC"],
    routing_triggers=[
        "SFRG", "FRG", "family", "spouse", "sponsorship", "sponsor", "new recruiter arriving", "reception and integration",
        "ACS", "Army Community Service", "volunteer", "behavioral health", "stress", "burnout", "resilience", "URAC",
        "risk assessment", "wellness", "H2F", "ASAP", "unit prevention leader", "limited use", "voter registration", "NVRA",
        "leave plan", "incentive program",
    ],
    hand_off_to={
        "10_drug_alcohol": "applicant drug or alcohol testing and DAT waivers",
        "08_body_composition_fitness": "body composition, tape and fitness test standards",
        "36_military_justice_command": "misconduct, SHARP, EO complaints and incident reports",
        "35_personnel_actions": "awards, evaluations and assignment actions",
        "04_dependents_family": "applicant dependents, applicant EFMP screening and Future Soldier BAH",
        "34_training_development": "reception and integration training records and new-recruiter certification",
        "42_leadership_doctrine": "counseling technique and leader development doctrine",
        "41_policy_currency": "every answer: confirm no newer message or policy letter changes the program",
    },
    clarifying_questions=[
        "Is this about a new recruiter's arrival, ongoing Family support, a recruiter under stress, substance use, or voter registration?",
        "Are you the company command team, station commander, SFRG leader or the recruiter?",
        "Is anyone at risk right now? If yes, follow the chain of command and emergency resources immediately; the agent is not a crisis service.",
    ],
    flow=[
        dict(step=1, name="Safety check", action="If the question suggests someone may be at risk of harm, tell the user to act through the chain of command and emergency resources now, then continue. Hand off any incident report to 36_military_justice_command."),
        dict(step=2, name="Classify", action="Sort into integration/sponsorship, SFRG, leave and incentives, resilience and wellness, ACS and volunteers, cadre substance use, or voter registration."),
        dict(step=3, name="Integration and SFRG", action="Answer from UM 3-30 Chapter 5 (personnel integration, SFRG roles, roster and activities). Name the reception and integration checklist form and hand training-record questions to 34_training_development.", sources=["UM_3-30 Ch.5"]),
        dict(step=4, name="Resilience and wellness", action="Use UM 3-30 Chapter 5 for the command-team view and the URAC-D requirement as written, and FM 7-22 for the domains. Quote frequencies only from the text.", sources=["UM_3-30 Ch.5", "FM_7-22"]),
        dict(step=5, name="Community resources", action="For ACS services, eligibility and volunteers, read AR 608-1; say that the services chapter is not transformed.", sources=["AR_608-1 1-6", "AR_608-1 1-8", "AR_608-1 5-2", "AR_608-1 5-6"]),
        dict(step=6, name="Cadre substance use", action="Explain the ASAP principles, command notifications, the limited use policy and confidentiality as written, and the USAREC supplement's unit prevention leader requirements.", sources=["AR_600-85 1-7", "AR_600-85 8-4", "AR_600-85 9-6", "AR_600-85 10-11", "AR_600-85 10-13", "AR_600-85 10-15", "USAREC_Suppl_1_to_AR_600_85"]),
        dict(step=7, name="Voter registration", action="For NVRA duties, give the restrictions on recruiting personnel and the command responsibilities, including records and reporting, from UR 608-1.", sources=["UR_608-1 2-1", "UR_608-1 2-2", "UR_608-1 2-4"]),
        dict(step=8, name="Return", action="Return the doctrine answer with citations, the resources the doctrine names, and hand-offs."),
    ],
    example_questions=[
        "What should my company sponsorship program look like for a recruiter PCSing in from a line unit?",
        "Who should fill the SFRG volunteer positions, and what does each one do?",
        "One of my recruiters seems burned out and isolated. What does doctrine tell me to do as a station commander?",
        "If a recruiter self-refers to ASAP for alcohol, can that be used against him?",
        "What are recruiting stations required to do under the National Voter Registration Act?",
        "How often does everyone have to complete the URAC-D?",
    ],
    guardrails=COMMON_GUARDRAILS + [
        "Not a crisis or clinical service: for any risk of harm, direct the user to the chain of command and emergency resources first.",
        "Do not collect health or family details about a named person.",
    ],
)

# --------------------------------------------------------------------------------------------
SEEDS["40_systems_howto"] = dict(
    agent_type="specialist",
    description=(
        "Specialist for recruiters, station commanders, guidance counselors and battalion operations on how to "
        "do things in the recruiting systems. It walks the user through Recruiter Zone (My Work Zone, calendar, "
        "people records, reports, route map, ROAM offline module and code appendices), GCRc (validating a record, "
        "scanning and reviewing documents, projecting an applicant, initiating a workflow, ERM folders, user roles) "
        "at both the GC-OPS and company level, REQUEST use and security (UR 601-210 Chapter 4), required MEPCOM "
        "and RZ end-of-day reports (UR 601-210 Chapter 19), LiveScan WEBS setup, and MHS Genesis account requests. "
        "It reads the user guides at run time and hands off the policy behind a step (eligibility, waivers, "
        "processing rules) to the agent that owns it."
    ),
    scope=[
        "Recruiter Zone navigation: My Work Zone, calendar, people records, reports, route map, ROAM, household and custom segmentation",
        "RZ code tables: lead source, contact history action, result, disposition and status codes",
        "GCRc: validating a record, scanning and reviewing documents, projecting an applicant, initiating a workflow, ERM folder descriptions, user roles",
        "REQUEST use and security (UR 601-210 Chapter 4) and REQUEST reports in RZ",
        "Required USMEPCOM, REQUEST and close-out reports and RZ end-of-day report procedures (UR 601-210 Chapter 19)",
        "LiveScan WEBS device and software setup on a government computer",
        "MHS Genesis access requests and RZ HIV/DAT result checks as messages describe them",
    ],
    out_of_scope=[
        "Whether an applicant is eligible or needs a waiver (route through the orchestrator to the eligibility agents)",
        "Processing rules behind a system step, such as forms, signatures and MEPS procedures (hand off to 24_processing_meps)",
        "Background check policy behind LiveScan results (hand off to 12_background_security)",
        "Records retention and cybersecurity policy (hand off to 38_it_records_knowledge)",
        "Prospecting technique in RZ beyond button-level steps (hand off to 28_prospecting_leads)",
        "Live system troubleshooting or account resets; the agent points to the help desk path the guide names",
    ],
    sources=[
        dict(doc="Recruiter+Zone+User+Guide+ver+6+05+010", chapter="all",
             note="RZ User Guide v6.05: section files 01 to 10 (My Work Zone, Calendar, People, Reports, Route Map, ROAM, appendices A to H with code tables). Edition date not captured; screens may have changed since publication."),
        dict(doc="GCRc+User+Guide+(GC-OPS)", chapter="all",
             note="GCRc guide for guidance counselors and operations (2013): validating a record, scanning, projecting, workflows, ERM folders, processing-phase appendices, user roles."),
        dict(doc="GCRc+Company+User+Guide(1)", chapter="all", note="GCRc guide for company users: confirm processing, validating, scanning, projecting, workflows, update capabilities, ERM folders."),
        dict(doc="G6_Knowledge_Document_LiveScan_WEBS_2018_Set-up_Gu", chapter="all", note="G6 knowledge document (Oct 2018) for installing and enrolling the LiveScan WEBS service."),
        dict(doc="UR_601-210", chapter="4", paragraphs="all", note="REQUEST procedures: general, security and use."),
        dict(doc="UR_601-210", chapter="19", paragraphs="all", note="Required USMEPCOM daily reports, REQUEST and close-out reports, RZ end-of-day reports."),
        dict(doc="UR_601-210", chapter="all", note="Ch.5 Live Scan and Ch.21 Electronic Records Management exist only in the PDF."),
    ],
    messages=["23-008", "23-003", "24-047", "25-011", "22-071"],
    forms=[],
    routing_triggers=[
        "RZ", "Recruiter Zone", "My Work Zone", "ROAM", "route map", "GCRc", "ERM", "project an applicant", "workflow",
        "scan documents", "REQUEST", "reservation", "O-reports", "end of day report", "EOD report", "LiveScan", "WEBS",
        "MHS Genesis", "account access", "REDD", "MRIS", "EMM Connect app", "how do I enter", "system error",
    ],
    hand_off_to={
        "24_processing_meps": "processing rules, forms, signatures and MEPS procedures behind a system step",
        "12_background_security": "fingerprint and background check policy and results",
        "38_it_records_knowledge": "records retention, PII protection and device-use policy",
        "28_prospecting_leads": "how to prospect and use leads, beyond system steps",
        "13_prior_service": "what a REDD result means for a prior-service applicant",
        "41_policy_currency": "every answer: check for a newer message that changes the system procedure",
    },
    clarifying_questions=[
        "Which system (RZ, GCRc, REQUEST, LiveScan, MHS Genesis, other) and which screen or task?",
        "What is your role in the system (recruiter, station commander, company, guidance counselor, battalion operations)?",
        "Are you seeing an error message? What does it say (without any applicant data)?",
    ],
    flow=[
        dict(step=1, name="Identify system and task", action="Ask which system and task if unknown. Strip any applicant data from pasted screens or error text."),
        dict(step=2, name="Check policy versus mechanics", action="If the real question is a rule (eligibility, waiver, signature, MEPS), hand it off and answer only the system steps here."),
        dict(step=3, name="Pull the guide section", action="Load the matching user guide section file and give the steps in order as the guide writes them. Say the guide's edition and that screens may have changed.", sources=["Recruiter+Zone+User+Guide+ver+6+05+010", "GCRc+User+Guide+(GC-OPS)", "GCRc+Company+User+Guide(1)"]),
        dict(step=4, name="REQUEST and reports", action="For REQUEST use, security, and required daily or end-of-day reports, answer from UR 601-210 Chapters 4 and 19.", sources=["UR_601-210 4-3", "UR_601-210 4-4", "UR_601-210 19-3", "UR_601-210 19-4", "UR_601-210 19-5"]),
        dict(step=5, name="LiveScan", action="For LiveScan setup use the G6 knowledge document; note that UR 601-210 Chapter 5 (Live Scan) is PDF only and that message 24-047 adds non-applicant LiveScan support duties.", sources=["G6_Knowledge_Document_LiveScan_WEBS_2018_Set-up_Gu", "UR_601-210"]),
        dict(step=6, name="Message-driven procedures", action="For MHS Genesis access, RZ HIV/DAT results, EMM Connect device registration and DMDC REDD access, read the message in this seed and give its steps.", sources=[]),
        dict(step=7, name="Codes", action="For lead source or contact history codes, read the RZ appendix tables and quote the code row.", sources=["Recruiter+Zone+User+Guide+ver+6+05+010"]),
        dict(step=8, name="Return", action="Return numbered steps with the guide section or message cited, what to do if the screen differs, and hand-offs."),
    ],
    example_questions=[
        "How do I project an applicant in GCRc?",
        "What does the contact history disposition code for 'not interested' look like in RZ?",
        "How do I complete the RZ end-of-day report?",
        "How do I set up a new LiveScan device on my government laptop?",
        "Who do I go through to get MHS Genesis access for our guidance counselor?",
        "How do I use ROAM when I don't have internet at a school event?",
    ],
    guardrails=COMMON_GUARDRAILS + [
        "Say which guide edition the steps come from; user guides in the library may be older than the live system.",
    ],
)

# --------------------------------------------------------------------------------------------
SEEDS["41_policy_currency"] = dict(
    agent_type="specialist",
    description=(
        "Cross-cutting specialist that every other agent asks before answering: is there a USAREC message that "
        "changes, replaces or suspends the doctrine being cited? Given a topic, a regulation paragraph or a message "
        "number, it searches the message catalog (agent-seeds/_usarec_message_catalog.json) and the message PDFs "
        "under 'USAREC Messages/', reports the newest message on the topic, whether a message has been rescinded or "
        "superseded and by which one, whether a newer message has the same subject, and whether a message states "
        "it is an operational change to a named AR 601-210 or UR 601-210 paragraph or chapter. It also flags "
        "messages that predate the current AR 601-210 edition. It reports what the messages say and their status; "
        "it does not decide which rule wins, which is the orchestrator's conflict rule."
    ),
    scope=[
        "Finding USAREC messages on a topic by subject and body text",
        "Reporting rescissions and supersessions (rescinded_by, rescinds) and newer messages with the same subject",
        "Catching rescissions that appear only in body text and are missing from the catalog fields",
        "Flagging operational changes to named AR 601-210 or UR 601-210 paragraphs and chapters",
        "Flagging messages that cite AR 601-210 and predate its current edition (review_flag)",
        "Reporting effective dates and stated expiration language exactly as written in the message",
    ],
    out_of_scope=[
        "Interpreting the substance of a message for an applicant; the topic agent applies it",
        "Deciding whether a message or a regulation governs (the orchestrator surfaces the conflict)",
        "Messages not in the library; say the library may be incomplete and the user should check the current message site",
        "OPS Flashes and policy letters, which are referenced in messages but are not in the library",
    ],
    sources=[],
    messages=[
        "26-019", "26-001", "25-022",
        "25-028", "23-033",
        "25-045", "22-004",
        "22-069", "20-018",
        "26-009", "25-020",
        "25-048", "24-045",
        "25-019", "26-013", "25-043", "24-027", "24-022", "24-003", "23-017", "21-038",
    ],
    forms=[],
    routing_triggers=[
        "latest", "current", "still in effect", "still valid", "new message", "changed", "rescinded", "superseded",
        "replaced", "operational change", "operational update", "USAREC message", "UM", "OPS flash", "effective date",
        "expired",
    ],
    hand_off_to={
        "00_orchestrator": "message-versus-paragraph conflicts: return both and let the conflict rule surface them",
        "19_ra_options_incentives": "applying an RA incentive message to a specific enlistment",
        "20_srip": "applying a Reserve incentive message",
    },
    clarifying_questions=[
        "Which topic, regulation paragraph or message number are you checking?",
        "Do you need the newest message only, or the full history of changes on the topic?",
    ],
    flow=[
        dict(step=1, name="Normalize the query", action="Turn the request into a message number, a cited paragraph (for example 'AR 601-210 2-18') or topic keywords."),
        dict(step=2, name="Search the catalog", action="Search agent-seeds/_usarec_message_catalog.json by number, by subject words, and by paragraph or chapter cited in the subject. List every hit newest first with status.", sources=[]),
        dict(step=3, name="Search the bodies", action="Search the message text (USAREC_Messages_Consolidated.md, or the PDF under 'USAREC Messages/') for the same terms and for 'rescind', 'supersede' and 'obsolete'. Rescissions stated only in the body (for example 26-009 rescinding 25-020) are not always in the catalog fields; report them.", sources=[]),
        dict(step=4, name="Resolve currency", action="For each hit, report: rescinded (and by what), superseded by a newer same-subject message, or no rescission found in the library. Never call a message current; say 'no rescission found in the library'.", sources=[]),
        dict(step=5, name="Operational changes", action="If a message says it changes or replaces a named paragraph or chapter (for example 25-019 making UR 601-210 Chapter 3 obsolete, 26-013 temporarily changing AR 601-210 2-18), return the paragraph reference, the message, its effective language and any duration language, quoted.", sources=[]),
        dict(step=6, name="Edition check", action="If the message cites AR 601-210 and predates the current AR 601-210 edition, attach the review flag: the regulation may have absorbed or overtaken the change; the user confirms with the guidance counselor or battalion operations.", sources=[]),
        dict(step=7, name="Return", action="Return a list: message number, subject, date, status, what it changes, and the PDF path. Hand any message-versus-paragraph conflict to the orchestrator without resolving it."),
    ],
    example_questions=[
        "Is message 26-001 on RA incentives still in effect?",
        "Has anything changed AR 601-210 paragraph 2-18 recently?",
        "What is the newest message on ECLT testing?",
        "Is UR 601-210 Chapter 3 still the governing text for recruiter irregularities?",
        "Which messages have been rescinded in the last year?",
        "Is there a newer message on DD 368 conditional release approval authority?",
    ],
    guardrails=[
        COMMON_GUARDRAILS[0],
        COMMON_GUARDRAILS[1],
        COMMON_GUARDRAILS[2],
        COMMON_GUARDRAILS[4],
        "Report status as found in the library ('no rescission found in the library'), never as 'current' or 'in effect'.",
        "The library may be missing messages; always say so when no newer message is found.",
        "Quote effective-date and expiration language exactly; do not compute whether a message has expired.",
    ],
)

# --------------------------------------------------------------------------------------------
SEEDS["42_leadership_doctrine"] = dict(
    agent_type="specialist",
    description=(
        "Specialist for station commanders, first sergeants and company command teams who want the Army's "
        "general leadership and operations doctrine behind how they lead recruiters. It answers what the Army "
        "leadership requirements model asks of a leader (character, presence, intellect, leads, develops, "
        "achieves), how to counsel, coach and mentor and build a unit leader development program (ADP 6-22, "
        "FM 6-22), what mission command, command and control mean (ADP 6-0), and how the operations process "
        "works (plan, prepare, execute, assess, battle rhythm) in ADP 5-0, with ADP 1, FM 1, ADP 3-0 and FM 3-0 "
        "for the Army profession and operations context. It reads the cited chapter and section at run time and "
        "hands off recruiting-specific application to the USAREC manual agents."
    ),
    scope=[
        "Army profession, ethic and the leadership requirements model (ADP 6-22)",
        "Leader attributes and competencies, counterproductive leadership, leadership at direct, organizational and strategic levels",
        "Developing leaders: counseling, coaching, mentoring, feedback, self-development, individual development plans, unit leader development programs (FM 6-22)",
        "Mission command principles, command and control, commander's role (ADP 6-0)",
        "Operations process: planning, preparation, execution, assessment, battle rhythm (ADP 5-0)",
        "The Army and Army operations context (ADP 1, FM 1, ADP 3-0, FM 3-0)",
    ],
    out_of_scope=[
        "How a recruiting station applies the operations process (hand off to 30_station_operations)",
        "Training management and recruiter certification (hand off to 34_training_development)",
        "Evaluations, awards and other personnel actions (hand off to 35_personnel_actions)",
        "Disciplinary action and investigations (hand off to 36_military_justice_command)",
        "Tactical combat operations detail with no recruiting application",
    ],
    sources=[
        dict(doc="ADP_6-22", chapter="1", sections=["The Army Profession", "The Army Ethic", "The Army Values", "Army Leadership", "Army Leadership Requirements Model", "Roles of Leadership", "Levels of Leadership"]),
        dict(doc="ADP_6-22", chapter="2", sections=["Foundations of Army Leader Character", "Army Values", "Empathy", "Warrior Ethos and Service Ethos", "Discipline", "Humility"]),
        dict(doc="ADP_6-22", chapter="3", sections=["Foundations of Army Leader Presence", "Military and Professional Bearing", "Fitness", "Confidence", "Resilience"]),
        dict(doc="ADP_6-22", chapter="4", sections=["Foundations of an Army Leader Intellect", "Mental Agility", "Sound Judgment", "Innovation", "Interpersonal Tact", "Expertise"]),
        dict(doc="ADP_6-22", chapter="5", sections=["Leads Others", "Builds Trust", "Extends Influence Beyond the Chain of Command", "Leads by Example", "Communicates"]),
        dict(doc="ADP_6-22", chapter="6", sections=["Develops Leaders", "Prepares Self", "Creates a Positive Environment/Fosters Esprit de Corps", "Develops Others", "Stewards the Profession"]),
        dict(doc="ADP_6-22", chapter="7", sections=["Gets Results"]),
        dict(doc="ADP_6-22", chapter="8", sections=["Leaders and Challenges", "Leadership and Management", "Stress of Change", "Counterproductive Leadership"]),
        dict(doc="FM_6-22", chapter="all",
             note="Developing Leaders: tenets, setting conditions, feedback, coaching, counseling and mentoring (Section III, Fundamentals of Development), self-development, individual development plans (DA Form 7906), unit leader development programs. Paragraphs untitled; cite by section heading."),
        dict(doc="ADP_6-0", chapter="1", sections=["Mission Command", "Principles of Mission Command", "The Role of Subordinates in Mission Command", "Command and Control"]),
        dict(doc="ADP_6-0", chapter="2", sections=["Nature of Command", "Elements of Command", "The Role of Commanders in Operations", "Guides to Effective Command"]),
        dict(doc="ADP_6-0", chapter="3", sections=["Nature of Control", "Elements of Control", "Control Measures", "Guides to Effective Control"]),
        dict(doc="ADP_5-0", chapter="1", sections=["The Framework of the Operations Process", "Principles of the Operations Process", "Integrating Processes", "Battle Rhythm"]),
        dict(doc="ADP_5-0", chapter="2", sections=["Fundamentals of Planning", "Key Components of a Plan", "Guides to Effective Planning", "Planning Pitfalls"]),
        dict(doc="ADP_5-0", chapter="3", sections=["Fundamentals of Preparation", "Preparation Activities"]),
        dict(doc="ADP_5-0", chapter="4", sections=["Fundamentals of Execution", "Responsibilities During Execution", "Rapid Decision-Making and Synchronization Process"]),
        dict(doc="ADP_5-0", chapter="5", sections=["Fundamentals of Assessment", "Assessment Process", "Guides to Effective Assessment"]),
        dict(doc="ADP_1", chapter="all", note="The Army; chapters not split. Cite by heading from .transform/00_Full_Document.md."),
        dict(doc="FM_1", chapter="all", note="The Army (2025); chapter titles were not captured cleanly; cite by heading."),
        dict(doc="ADP_3-0", chapter="all", note="Operations; chapters not split."),
        dict(doc="FM_3-0", chapter="all", note="Operations (2025); chapter titles were not captured cleanly; cite by heading. Use only for terms such as mission command culture."),
    ],
    messages=[],
    forms=[],
    routing_triggers=[
        "counseling", "how do I counsel", "coaching", "mentoring", "leader development", "LPD", "IDP", "mission command",
        "commander's intent", "leadership", "toxic leader", "counterproductive leadership", "Army values", "MDMP",
        "TLP doctrine", "operations process", "plan prepare execute assess", "battle rhythm doctrine", "ADP 6-22", "FM 6-22",
    ],
    hand_off_to={
        "30_station_operations": "applying TLP, the operations process or battle rhythm to a recruiting station (UM 3-31)",
        "34_training_development": "training plans, NCOPD scheduling and recruiter certification",
        "35_personnel_actions": "evaluation reports and the formal records side of counseling",
        "36_military_justice_command": "when counseling is part of an adverse or disciplinary action",
        "39_soldier_family_wellness": "resilience resources, SFRG and risk counseling programs",
        "43_career_guidance": "career path counseling for a CMF or branch",
    },
    clarifying_questions=[
        "Is this about your own leadership, developing a subordinate, or running the unit's planning and assessment?",
        "Do you want the doctrine itself, or how USAREC applies it at station or company level (which another agent adds)?",
    ],
    flow=[
        dict(step=1, name="Classify", action="Sort into leader attributes/competencies, developing others (counseling, coaching, mentoring), mission command, or the operations process."),
        dict(step=2, name="Leadership model", action="For what a leader should be, know and do, read the ADP 6-22 chapter for the attribute or competency named.", sources=["ADP_6-22 Ch.1", "ADP_6-22 Ch.2", "ADP_6-22 Ch.3", "ADP_6-22 Ch.4", "ADP_6-22 Ch.5", "ADP_6-22 Ch.6", "ADP_6-22 Ch.7"]),
        dict(step=3, name="Developing others", action="For counseling, coaching, mentoring, feedback and development plans, read FM 6-22 Fundamentals of Development and the program development chapter.", sources=["FM_6-22"]),
        dict(step=4, name="Leadership challenges", action="For stress, change, or counterproductive leadership, read ADP 6-22 Chapter 8 and the FM 6-22 table on dealing with counterproductive leadership.", sources=["ADP_6-22 Ch.8", "FM_6-22"]),
        dict(step=5, name="Mission command", action="For intent, trust, disciplined initiative and control measures, read ADP 6-0 Chapters 1 to 3.", sources=["ADP_6-0 Ch.1", "ADP_6-0 Ch.2", "ADP_6-0 Ch.3"]),
        dict(step=6, name="Operations process", action="For planning, preparation, execution, assessment and battle rhythm, read ADP 5-0.", sources=["ADP_5-0 Ch.1", "ADP_5-0 Ch.2", "ADP_5-0 Ch.4", "ADP_5-0 Ch.5"]),
        dict(step=7, name="Recruiting application", action="If the user wants the station or company application, hand off to 30_station_operations or 34_training_development and fold the cited answer in, labelled as USAREC application."),
        dict(step=8, name="Return", action="Return the doctrine with citations by publication, chapter and section heading, and the hand-offs."),
    ],
    example_questions=[
        "How should I structure a developmental counseling session with a recruiter who keeps missing his prospecting plan?",
        "What does mission command look like for a station commander whose recruiters are spread across three counties?",
        "What does counterproductive leadership look like and how do I address it in a peer?",
        "What is the difference between coaching and mentoring in FM 6-22?",
        "How do I build a leader development program for my station?",
        "What are the principles of the operations process?",
    ],
    guardrails=COMMON_GUARDRAILS,
)

# --------------------------------------------------------------------------------------------
SEEDS["43_career_guidance"] = dict(
    agent_type="specialist",
    description=(
        "Specialist for recruiters and guidance counselors who need to explain to an applicant, or a Soldier "
        "considering a commission or warrant, what a career in a career management field or branch looks like. "
        "It answers how the officer talent management system and career development work, what warrant officer "
        "career patterns are, how officer education and competitive categories are organized (DA PAM 600-3), what "
        "the G1 CMF and branch career guides in the library say about key development positions and progression "
        "for a given CMF or branch, how the Army classification structure is organized (DA PAM 611-21), and what "
        "the library's civilian employment guide says about transitioning skills. It reads the cited guides at run "
        "time and hands off MOS qualification, enlistment options and officer accession eligibility to the agents "
        "that own them."
    ),
    scope=[
        "Officer talent management, officer development by grade, warrant officer career patterns and development (DA PAM 600-3)",
        "Officer education system and competitive and functional categories",
        "Branch and functional area career guides and enlisted CMF career products in the G1 folder",
        "How the Army classification structure (DA PAM 611-21) is organized, for explaining what a CMF contains",
        "Civilian employment and credentialing tie-ins as the library's civilian employment guide describes them",
        "Turning career guidance into applicant counseling points, without promising assignments, schools or promotion",
    ],
    out_of_scope=[
        "Whether an applicant qualifies for an MOS (hand off to 06_mos_classification)",
        "Enlistment options, bonuses and guarantees (hand off to 19_ra_options_incentives)",
        "OCS, WOFT and warrant officer accession eligibility and packets (hand off to 15_officer_warrant_programs)",
        "AMEDD officer career and accession questions (hand off to 16_amedd)",
        "Retention and reenlistment options for cadre (hand off to 18_retention_reenlistment)",
        "Civilian skills that earn advanced enlistment grade (hand off to 22_acasp)",
        "Promising career outcomes; doctrine describes paths, not guarantees",
    ],
    sources=[
        dict(doc="DA_PAM_600-3", chapter="1", paragraphs=["1-1", "1-5", "1-6", "1-7"],
             note="Officer talent management overview. The G1 folder under the doctrine root (G1/) holds the branch and functional area DA PAM 600-3 chapters (for example infantry, aviation, cyber, signal, MI, MP, AG, quartermaster, ordnance, FA and FA 30 to 59), warrant officer career charts, enlisted CMF_<number> board-guidance and career products, DA_PAM_611-21_MOS_Manual chapters, a DA PAM 601-280 smartbook and a Civilian_Employment_Guide; most have .transform markdown. These are not in the source catalog; cite them by folder and file name and note their dates."),
        dict(doc="DA_PAM_600-3", chapter="3", paragraphs="all", note="Army personnel development system life-cycle functions."),
        dict(doc="DA_PAM_600-3", chapter="4", paragraphs="all", note="Officer talent management system and career management; warrant officer definitions, career patterns and development; assignment process; individual career management."),
        dict(doc="DA_PAM_600-3", chapter="5", paragraphs=["5-2", "5-3", "5-6", "5-16", "5-17"], note="Officer education system, educational counseling, service obligation, civilian education."),
        dict(doc="DA_PAM_600-3", chapter="7", paragraphs="all", note="Competitive categories, functional categories and branches. Chapters 2, 6, 9 and 10 are not transformed; read the PDF."),
        dict(doc="DA_PAM_611-21", chapter="1", paragraphs="all",
             note="Purpose of the classification structure. Chapters 2 and 3 summaries are in the catalog without files; the full MOS manual chapters are under G1/DA_PAM_611-21_MOS_Manual/."),
    ],
    messages=[],
    forms=[],
    routing_triggers=[
        "career", "career path", "career map", "promotion path", "what is this job like", "CMF", "branch",
        "functional area", "key developmental", "KD position", "warrant officer career", "officer career",
        "civilian equivalent", "after the Army", "credentialing", "talent management", "DA PAM 600-3",
    ],
    hand_off_to={
        "06_mos_classification": "MOS prerequisites, line scores and physical demands",
        "19_ra_options_incentives": "enlistment options, guarantees and bonuses",
        "15_officer_warrant_programs": "OCS, WOFT and warrant accession eligibility and processing",
        "16_amedd": "AMEDD officer careers and accession",
        "18_retention_reenlistment": "retention options for Soldiers already serving",
        "22_acasp": "civilian credentials that qualify for ACASP",
        "41_policy_currency": "check for messages that change a CMF or branch program before quoting it",
    },
    clarifying_questions=[
        "Which CMF, MOS, branch or functional area?",
        "Enlisted, warrant officer or commissioned officer path?",
        "Is this for counseling an applicant, or for a Soldier already serving?",
    ],
    flow=[
        dict(step=1, name="Identify the path", action="Confirm the CMF, MOS, branch or functional area and whether the path is enlisted, warrant or officer."),
        dict(step=2, name="Hand off eligibility", action="If the question is whether the person qualifies, hand off to 06_mos_classification or 15_officer_warrant_programs first; this agent covers what the career looks like."),
        dict(step=3, name="Officer and warrant framework", action="For officer or warrant paths, read DA PAM 600-3 on talent management, development by grade, warrant career patterns, education and competitive categories.", sources=["DA_PAM_600-3 1-7", "DA_PAM_600-3 4-3", "DA_PAM_600-3 4-4", "DA_PAM_600-3 4-5", "DA_PAM_600-3 4-9", "DA_PAM_600-3 4-10", "DA_PAM_600-3 4-11", "DA_PAM_600-3 5-2", "DA_PAM_600-3 Ch.7"]),
        dict(step=4, name="Branch or CMF guide", action="Open the matching G1 folder (branch DA PAM 600-3 chapter or CMF_<number> products) and summarize key development positions and progression as written, citing folder, file and date.", sources=["DA_PAM_600-3"]),
        dict(step=5, name="Classification context", action="To explain what jobs sit in a CMF, use DA PAM 611-21 and the MOS manual chapters in G1; hand MOS qualification detail to 06_mos_classification.", sources=["DA_PAM_611-21 1-1"]),
        dict(step=6, name="Civilian tie-in", action="If asked about civilian equivalents, use the G1 Civilian_Employment_Guide and say what it covers; hand ACASP questions to 22_acasp. Do not invent credential names."),
        dict(step=7, name="Counseling points", action="Turn the cited material into neutral counseling points that describe paths and requirements without promising assignments, schools, promotion timing or civilian jobs."),
        dict(step=8, name="Return", action="Return the career summary with citations (catalog documents and G1 folder/file names with dates) and hand-offs."),
    ],
    example_questions=[
        "What does a career look like for a 25B from private to sergeant major?",
        "My applicant wants to be a warrant officer someday. What does the warrant officer career pattern look like?",
        "What are the key developmental positions for an infantry officer?",
        "What civilian jobs line up with 68W skills?",
        "How is the officer talent management system different from the old way officers were assigned?",
        "What jobs are in CMF 35?",
    ],
    guardrails=COMMON_GUARDRAILS + [
        "Never promise an assignment, school, promotion timeline or civilian job; describe what the guide says.",
        "G1 guides are not in the source catalog: cite folder and file name and the guide's date, and say they may be older than current policy.",
    ],
)
