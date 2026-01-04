import pandas as pd
import os

class DataManager:
    def load_csv(self, path):
        try:
            if not os.path.exists(path):
                print(f"Error: File not found at {path}")
                return None
            return pd.read_csv(path)
        except Exception as e:
            print(f"Error loading CSV: {e}")
            return None