# scripts/preprocess_reviews.py
import pandas as pd
import numpy as np

def drop_duplicates_and_nan(df):
    """
    Removes duplicate reviews and drops rows with any missing data.
    
    Args:
        df (pd.DataFrame): The DataFrame containing review data.
    
    Returns:
        pd.DataFrame: The cleaned DataFrame.
    """
    original_rows = len(df)
    
    # Drop duplicates based on review_text
    df = df.drop_duplicates(subset=['review_text'])
    duplicates_removed = original_rows - len(df)
    
    # Drop rows with any missing data
    df = df.dropna()
    nan_removed = original_rows - duplicates_removed - len(df)
    
    print(f"  - Removed {duplicates_removed} duplicates.")
    print(f"  - Removed {nan_removed} rows with missing data.")
    
    return df

def normalize_dates(df):
    """
    Normalizes the 'date' column to YYYY-MM-DD format.
    
    Args:
        df (pd.DataFrame): The DataFrame with a 'date' column.
    
    Returns:
        pd.DataFrame: The DataFrame with normalized dates.
    """
    df['date'] = pd.to_datetime(df['date']).dt.strftime('%Y-%m-%d')
    return df

# This is the main function that will be called from the notebook
def preprocess_reviews(df):
    """
    Orchestrates the full preprocessing pipeline on a DataFrame.
    
    Args:
        df (pd.DataFrame): The raw DataFrame to preprocess.
    
    Returns:
        pd.DataFrame: The fully cleaned DataFrame.
    """
    df = drop_duplicates_and_nan(df)
    df = normalize_dates(df)
    return df