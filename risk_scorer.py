import pandas as pd
from scipy.stats import zscore

class RiskScorer:
    def score(self, customer_df):
        df = customer_df.copy()
        df["amount_zscore"] = zscore(df["total_amount"])
        df["amount_zscore"] = df["amount_zscore"].fillna(0).abs()

        def assign_band(score):
            if score < 1: return "Low"
            elif score < 2: return "Medium"
            elif score < 3: return "High"
            else: return "Critical"

        df["risk_level"] = df["amount_zscore"].apply(assign_band)
        return df