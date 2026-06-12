## Ujima Agent Pride: Live Prototype

This repository contains the live prototype for the #Ujima Agent Pride# ecosystem. This system utilizes [CrewAI](https://www.crewai.com/) to orchestrate a team of specialized agents designed to solve micro-lending bias and improve financial inclusion for informal market vendors in Kenya, specifically aligning financial services with agricultural liquidity cycles (e.g., *matooke* harvest windows).

## 🚀 Overview
The Ujima Agent Pride system operates on a #RANK-calibrated# (Role, Authority, Notification, Kill-switch) architecture. It consists of three autonomous agents working in a synchronized loop:

1.Scout Agent: Financial Literacy Coach focused on harvest-cycle planning.
2.Guardian Agent: Tier-1 Loan Triage screening for micro-loans.
3.Hunter Agent: Human-in-the-Loop Coordinator preparing briefings for loan officers.

## Architecture & Frameworks
The system is built upon several core ethical frameworks:
1.ETHOS: Dignity-centered prompting and automated accountability.
2.TRACK: Forensic bias analysis for credit underwriting.
3.OASIS: Data sovereignty (hosted on AWS Africa/Cape Town).
4.PRIDE: Human oversight and disagreement rights (USSD bypass).
5.HORIZON: Long-term, intergenerational financial impact modeling.

##  Prerequisites
1.Python 3.10+
2.OpenAI API Key
3.CrewAI library installed (`pip install crewai`)

##  Setup
1.Clone the repository:
    ```bash
    git clone https://github.com/your-username/your-repo-name.git
    cd your-repo-name
    ```

2.Configure environment variables:**
    Create a `.env` file in the root directory and add your API key:
    ```env
    OPENAI_API_KEY=sk-proj-YOUR_ACTUAL_SECRET_KEY_HERE
    ```

3.Run the prototype:**
    ```bash
    python src/main.py
    ```

##  Agent Roles & Handoff Triggers
The agents follow strict ## HUNT handoff triggers to maintain efficiency and safety:
* **Scout ➔ Guardian: Triggered when a member sends a financial stress signal (e.g., "No money for school fees").
* **Guardian ➔ Hunter**: Triggered when a loan request scores in the "borderline" liquidity zone (70-89%) and requires human professional insight.

## 🛡️ Safety & Governance
* **GUARD Rails**: Hard blocks on demographic proxies; max 3 SMS/day.
* **Data Sovereignty**: All data remains within the AWS `af-south-1` (Cape Town) region in compliance with Kenya DPA 2022.
* **Human-in-the-Loop**: Any loan >KES 15,000 or applicants with specific vulnerability indicators (e.g., dependents under 5) are automatically escalated to human review via the Hunter Agent.

## 📊 Impact Projections
* **Inclusion**: 37% projected increase in loan approvals for informal vendors.
* **Risk**: <3% default rate projection.
* **Efficiency**: Significant reduction in manual triage time for loan officers.

## 📜 License
This project is proprietary and developed under the Ujima SACCO Ethics & Governance mandate.

---
*Built as part of the Ujima Agent Pride capstone expedition.*