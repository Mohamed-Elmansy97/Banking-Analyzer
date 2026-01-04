import pandas as pd

class FeatureBuilder:
    def build(self, df):
        features_df = df.copy()
        features_df["balance_change_origin"] = features_df["newbalanceOrig"] - features_df["oldbalanceOrg"]
        
        customer_agg = features_df.groupby("nameOrig").agg(
            tx_count=("step", "count"),
            total_amount=("amount", "sum"),
            avg_amount=("amount", "mean"),
            max_amount=("amount", "max"),
            avg_bal_change=("balance_change_origin", "mean")
        ).reset_index()
        return customer_agg