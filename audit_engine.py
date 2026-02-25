import pandas as pd
import numpy as np
from datetime import datetime

class DataAuditor:
    def __init__(self, file_path):
        self.df = pd.read_csv(file_path)
        self.report = []

    def run_audit(self):
        # 1. Null Value Audit
        null_counts = self.df.isnull().sum()
        for col, count in null_counts.items():
            if count > 0:
                self.report.append({"Check": "Null Discovery", "Column": col, "Issue": f"Found {count} missing values", "Severity": "High"})

        # 2. Schema Integrity (AI Logic Simulation)
        # Checking if emails are valid
        if 'email' in self.df.columns:
            invalid_emails = self.df[~self.df['email'].str.contains("@", na=False)]
            if not invalid_emails.empty:
                self.report.append({"Check": "Format Validation", "Column": "email", "Issue": f"{len(invalid_emails)} rows have invalid email formats", "Severity": "Medium"})

        # 3. Governance Metadata
        audit_summary = pd.DataFrame(self.report)
        audit_summary['audit_timestamp'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return audit_summary

def generate_sample_data():
    # Creating a dirty dataset to test the auditor
    data = {
        'user_id': [1, 2, 3, 4],
        'user_name': ['Alice', 'Bob', np.nan, 'David'],
        'email': ['alice@test.com', 'bob_at_test.com', 'char@test.com', np.nan],
        'status': ['Active', 'Active', 'Pending', 'Active']
    }
    df = pd.DataFrame(data)
    df.to_csv("source_data.csv", index=False)
    return "source_data.csv"

if __name__ == "__main__":
    file = generate_sample_data()
    auditor = DataAuditor(file)
    print(auditor.run_audit())