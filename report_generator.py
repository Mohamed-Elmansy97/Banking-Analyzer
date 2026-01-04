import os

import os

class ReportGenerator:
    def export(self, flagged_df, scored_df):
        if not os.path.exists("reports"):
            os.makedirs("reports")

        flagged_df.to_csv("reports/flagged_transactions.csv", index=False)
        scored_df.to_csv("reports/customer_risk_summary.csv", index=False)

        with open("reports/report.txt", "w") as f:
            f.write("PaySim Fraud Detection Report\n")
            f.write("="*30 + "\n")
            f.write(f"Total Unique Customers Scored: {len(scored_df)}\n")
            f.write("Risk level distribution:\n")
            f.write(scored_df["risk_level"].value_counts().to_string() + "\n")
            f.write("\nTop 5 Flagged Transactions:\n")
            f.write(flagged_df.head().to_string() + "\n")