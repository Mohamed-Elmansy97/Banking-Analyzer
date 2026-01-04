from scipy.stats import zscore

class TransactionFlagger:
    def flag(self, df):
        df = df.copy()
        df["amount_z"] = zscore(df["amount"])
        df["amount_z"] = df["amount_z"].fillna(0).abs()
        
        df["is_suspicious"] = (df["amount_z"] > 3) | \
                             ((df["type"] == "TRANSFER") & (df["amount"] > 200000))
        return df[df["is_suspicious"] == True]