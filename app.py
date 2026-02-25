import streamlit as st
import pandas as pd
from audit_engine import DataAuditor, generate_sample_data

st.set_page_config(page_title="AI Governance Auditor", layout="wide")

st.title(":material/security: AI Data Governance & Audit Portal")
st.sidebar.info("Lead Engineer: Srishti Goenka | 9.18 CGPA")

if st.sidebar.button("Generate & Load Sample Data"):
    generate_sample_data()
    st.sidebar.success("Source Data Loaded!")

if st.button("Run AI Audit Engine"):
    try:
        auditor = DataAuditor("source_data.csv")
        report_df = auditor.run_audit()
        
        st.subheader("Raw Data Audit")
        st.dataframe(pd.read_csv("source_data.csv"), use_container_width=True)
        
        st.subheader("Audit Findings")
        if not report_df.empty:
            # Highlighting High Severity issues
            st.table(report_df)
        else:
            st.success("Data Governance Passed! No issues found.")
            
    except FileNotFoundError:
        st.error("Please load data first from the sidebar.")

st.markdown("---")
st.caption("AI Auditor v1.0 | Data Governance Framework")