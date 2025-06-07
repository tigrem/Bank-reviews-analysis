# scripts/data_loader.py
import pandas as pd

def load_data(file_paths):
    bank_dataframes = {}
    for bank_name, path in file_paths.items():
        df = pd.read_csv(path)
        df['bank_name'] = bank_name
        bank_dataframes[bank_name] = df
        print(f"Loaded data for {bank_name}:")
        print(df.head(), "\n")
    return bank_dataframes