import pandas as pd
import numpy as np
import os
from datetime import datetime

try:
    from groq import Groq
    GROQ_AVAILABLE = True
except ImportError:
    GROQ_AVAILABLE = False

class DataAuditor:
    def __init__(self, file_path, api_key=None):
        self.df = pd.read_csv(file_path)
        self.report = []
        # Target schema for Silver layer
        self.expected_schema = ['user_id', 'user_name', 'email', 'status']
        
        self.client = None
        if GROQ_AVAILABLE and api_key:
            try:
                self.client = Groq(api_key=api_key)
            except Exception:
                self.client = None

    def run_llm_sql_audit(self, sql_query):
        """AI-driven SQL compliance check."""
        if self.client:
            try:
                response = self.client.chat.completions.create(
                    messages=[{"role": "user", "content": f"Audit this SQL for security risks: {sql_query}. Be technical and concise."}],
                    model="llama3-8b-8192",
                )
                return [response.choices[0].message.content]
            except Exception:
                pass 

        # Heuristic Fallback
        vulnerabilities = []
        if any(cmd in sql_query.upper() for cmd in ["DROP", "DELETE", "TRUNCATE"]):
            vulnerabilities.append("CRITICAL: Destructive Command Detected (Compliance Violation)")
        if "SELECT *" in sql_query.upper():
            vulnerabilities.append("ADVISORY: Performance issue detected (Schema expansion risk)")
        return vulnerabilities if vulnerabilities else ["Standard validation passed: No high-risk patterns found."]

    def run_audit(self):
        # 1. Schema Evolution Detection
        current_cols = list(self.df.columns)
        if current_cols != self.expected_schema:
            new_cols = set(current_cols) - set(self.expected_schema)
            self.report.append({
                "Check": "Schema Evolution", 
                "Column": "Global", 
                "Issue": f"Drift detected. New columns: {list(new_cols)}", 
                "Severity": "Medium"
            })

        # 2. Automated Null Discovery
        null_counts = self.df.isnull().sum()
        for col, count in null_counts.items():
            if count > 0:
                self.report.append({
                    "Check": "Null discovery", 
                    "Column": col, 
                    "Issue": f"Integrity breach: {count} missing values", 
                    "Severity": "High"
                })

        audit_summary = pd.DataFrame(self.report)
        audit_summary['audit_timestamp'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return audit_summary

def generate_sample_data():
    """Simulates a dirty staging dataset."""
    data = {
        'user_id': [1, 2, 3, 4],
        'user_name': ['Alice', 'Bob', np.nan, 'David'],
        'email': ['alice@test.com', 'invalid_mail', 'char@test.com', np.nan],
        'status': ['Active', 'Active', 'Pending', 'Active'],
        'new_feature_flag': [1, 1, 0, 1] # Extra column to trigger schema evolution
    }
    pd.DataFrame(data).to_csv("source_data.csv", index=False)