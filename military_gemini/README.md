# Setting Up AgentArmy in Military Gemini (Web / Enterprise Portal)

This directory contains everything you need to run AgentArmy in the **Military Gemini Web / Enterprise Chat tool** without needing a terminal, code execution, or external servers.

---

## 1. How to Configure the Master AgentArmy in Military Gemini

1. Open your **Military Gemini Web Portal**.
2. Click **Create Custom Gem** (or configure your workspace's System Instructions).
3. **Name**: `AgentArmy: Army Recruiting Command`
4. **Description**: `Authoritative multi-agent AI for Army recruiting doctrine, waivers, eligibility, MEPS, and operations.`
5. **System Instructions**:
   - Open [`GEMINI_SYSTEM_INSTRUCTIONS.md`](GEMINI_SYSTEM_INSTRUCTIONS.md).
   - Copy the entire contents and paste it into the **Instructions** box.
   - This equips Gemini with the complete web of 1 Orchestrator + 43 Specialists, the routing table, tie-breakers, clarifying questions, and authority hierarchy.

---

## 2. Attaching the Knowledge Bundles

Because Military Gemini does not read from a local Git repository, upload these **5 Knowledge Bundles** directly into the **Knowledge / Attachments** pane:

| Attachment | File | What It Covers |
|---|---|---|
| **Bundle 1** | `doctrine_bundles/01_Eligibility_Doctrine.html` | Basic eligibility, Age, SSN, Education Tiers, ASVAB, Medical Standards (DoDI 6130.03), Body Fat/Tape, Conduct Waivers, Tattoos |
| **Bundle 2** | `doctrine_bundles/02_Applicant_Types_Doctrine.html` | Prior Service (AR 601-210 Ch.3), Army Reserve, Officer & Warrant, AMEDD, Chaplains (UTP 3-10.6), Reenlistment |
| **Bundle 3** | `doctrine_bundles/03_Contracts_MEPS_Processing_Doctrine.html` | Enlistment options, bonuses, SRIP, ACASP, pay grade, MEPS processing, Future Soldiers, DEP discharge |
| **Bundle 4** | `doctrine_bundles/04_Operations_Command_Doctrine.html` | Prospecting, school recruiting, station ops, COI events, cadre training, promotions (AR 600-8-19), investigations |
| **Bundle 5** | `doctrine_bundles/05_USAREC_Messages_and_Currency.html` | All 155 USAREC messages with active/rescinded status and regulation conflict flags |
| **Master Index** | `AgentArmy_Master_Directory.html` | Searchable directory of all 44 agents with exact scope and out-of-scope boundaries |

---

## 3. Adding Local Station / MEPS Overlays

If you want to add local station reality (e.g. Charlotte MEPS processing hours, North Carolina 100% Tuition Assistance, local station SOPs):
1. Simply attach your local SOP markdown or HTML file (examples in [`locations/`](../locations/)) to the chat or Knowledge pane alongside the bundles.
2. In your query, mention your location (e.g., *"Applicant processing at Charlotte MEPS with medical prescreen"*).
3. Gemini will route to `07_medical_standards` and synthesize both the national regulation (`DoDI 6130.03`) and your local MEPS overlay!
