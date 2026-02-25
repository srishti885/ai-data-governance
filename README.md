# AI Data Governance & Audit Portal
**Enterprise-grade Compliance Framework for Modern Data Pipelines (Medallion Architecture)**

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge.svg)](https://ai-data-governance-dfmkrkrmhgf2yrmibdjxas.streamlit.app)

---

## Live Demo
Access the production portal here: [AI Data Governance Portal](https://ai-data-governance-dfmkrkrmhgf2yrmibdjxas.streamlit.app)

**Authorized Access Credentials:**
* **Username:** admin
* **Password:** srishti918

---

## Project Overview
In modern data engineering, ensuring data quality and security during the transition from Bronze to Silver layers is critical. This project implements an automated governance layer that audits incoming data for schema drift, integrity breaches, and security vulnerabilities using Generative AI.



### Core Modules
* **AI SQL Security Auditor:** Leverages Groq (Llama-3-8b) to parse and validate SQL scripts for destructive commands (DROP, TRUNCATE) and performance bottlenecks.
* **Schema Evolution Tracker:** Automatically detects metadata drift and unauthorized column additions in staging environments.
* **Data Quality Gates:** Real-time discovery of null values and data format inconsistencies to maintain Silver layer integrity.
* **Secure Session Management:** Enterprise-style authentication with persistent session states and custom-styled Landing Interface.

---

## Architecture & Workflow
1.  **Landing Interface:** Professional entry point with Glassmorphism UI and animated transitions.
2.  **Authentication Layer:** Secure Sign-up/Sign-in to manage authorized access sessions.
3.  **Control Center:** Sidebar-driven data ingestion and Groq Cloud API configuration.
4.  **Audit Workspace:** Real-time visualization of Governance Scores, Critical Alerts, and AI-generated security traces.



---

## Technical Stack
* **Language:** Python 3.x
* **Frontend:** Streamlit (Custom CSS & Material Design System)
* **AI Engine:** Groq Cloud API (Llama-3-8b-8192)
* **Data Processing:** Pandas, NumPy
* **Security:** Session-state based Authentication

---

## Developer Profile
**Srishti Goenka** *Lead Data Engineer & AI Auditor* * **Academic Excellence:** 9.18 CGPA  
* **Focus:** Building secure, scalable data architectures with AI-driven governance and automated compliance.

---

## Local Installation
1.  Clone the repository:
    ```bash
    git clone [https://github.com/YOUR_USERNAME/ai-data-governance.git](https://github.com/YOUR_USERNAME/ai-data-governance.git)
    ```
2.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3.  Run the application:
    ```bash
    streamlit run app.py
    ```

---
*Developed for robust compliance in Modern Data Stacks.*
