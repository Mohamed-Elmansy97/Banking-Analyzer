import pandas as pd

class TransactionCleaner:
    def clean(self, df):
        df = df.copy()
        df = df.drop_duplicates().dropna()
        if 'step' in df.columns:
            df['step'] = df['step'].astype(int)
        df["origin_is_merchant"] = df["nameOrig"].str.startswith("M")
        df["dest_is_merchant"] = df["nameDest"].str.startswith("M")
        return df