import streamlit as st
import pandas as pd
import os
import time
from audit_engine import DataAuditor, generate_sample_data

# Enterprise Configuration
st.set_page_config(page_title="AI Governance Portal", layout="wide")

# Advanced CSS for Landing Page & Animations
st.markdown("""
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/animate.css/4.1.1/animate.min.css"/>
    <style>
    .stApp { background-color: #f4f7f6; }
    .auth-card {
        background: white; padding: 40px; border-radius: 15px;
        box-shadow: 0 10px 25px rgba(0,0,0,0.05); border: 1px solid #eef2f6;
        margin-top: 50px;
    }
    .landing-title {
        font-size: 42px; font-weight: 800; text-align: center;
        color: #1a202c; letter-spacing: -1px;
    }
    .stButton>button {
        background-color: #2d3748; color: white; border-radius: 8px;
        height: 48px; transition: 0.3s;
    }
    .stButton>button:hover { background-color: #4a5568; transform: translateY(-1px); }
    </style>
    """, unsafe_allow_html=True)

# Session Management
if 'auth' not in st.session_state:
    st.session_state['auth'] = False
if 'users' not in st.session_state:
    st.session_state['users'] = {"admin": "srishti918"}

# ==========================================
# AUTHENTICATION LAYER
# ==========================================
if not st.session_state['auth']:
    st.markdown('<div class="animate__animated animate__fadeIn">', unsafe_allow_html=True)
    st.markdown('<p class="landing-title">AI Data Governance Portal</p>', unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #718096;'>Enterprise Audit Environment | Principal Access Only</p>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 1.3, 1])
    with col2:
        st.markdown('<div class="auth-card">', unsafe_allow_html=True)
        mode = st.tabs([":material/login: Sign In", ":material/person_add: Create Account"])
        
        with mode[0]:
            user = st.text_input("Username", key="login_user")
            pwd = st.text_input("Password", type="password", key="login_pwd")
            if st.button("Authenticate"):
                if user in st.session_state['users'] and st.session_state['users'][user] == pwd:
                    st.session_state['auth'] = True
                    st.balloons()
                    time.sleep(0.5)
                    st.rerun()
                else:
                    st.error("Access Denied: Invalid Credentials")
        
        with mode[1]:
            nu = st.text_input("New Username")
            np = st.text_input("New Password", type="password")
            if st.button("Register System User"):
                if nu and np:
                    st.session_state['users'][nu] = np
                    st.success("Account Provisioned. Proceed to Sign In.")
        st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# ==========================================
# GOVERNANCE DASHBOARD
# ==========================================
else:
    with st.sidebar:
        st.title(":material/shield: Control Center")
        st.info(f"Lead: Srishti Goenka\nCredential Score: 9.18 CGPA")
        if st.button(":material/logout: Sign Out"):
            st.session_state['auth'] = False
            st.rerun()
        
        st.markdown("---")
        key = st.text_input("Groq API Key (Optional)", type="password")
        if st.button(":material/database: Ingest Pipeline Data"):
            generate_sample_data()
            st.toast("Staging data refreshed")

    st.title(":material/analytics: Governance & Audit Workspace")

    if os.path.exists("source_data.csv"):
        auditor = DataAuditor("source_data.csv", api_key=key)
        results = auditor.run_audit()

        # KPIs
        k1, k2, k3 = st.columns(3)
        with k1: st.metric("Governance Health", "78%", delta="-14% (Drift)")
        with k2: st.metric("Active Alerts", len(results))
        with k3: st.metric("Audit Mode", "AI Enabled" if key else "Heuristic")

        st.subheader("Data Integrity Audit Log")
        st.dataframe(results, use_container_width=True)

        st.markdown("---")
        st.subheader("AI-Powered SQL Compliance Lab")
        query = st.text_area("SQL Script Audit:", "DROP TABLE users;")
        if st.button(":material/security: Scan Script"):
            with st.spinner("LLM Heuristics running..."):
                analysis = auditor.run_llm_sql_audit(query)
                for item in analysis:
                    st.warning(f":material/history_edu: {item}")
    else:
        st.info("No data detected. Please trigger 'Ingest Pipeline Data' from the control center.")

st.markdown("---")
st.caption("AI Auditor v2.4 | Engine: Llama-3-8b | Engineer: Srishti Goenka")