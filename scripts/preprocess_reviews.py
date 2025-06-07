import pandas as pd

def preprocess_reviews(file_path):
    df = pd.read_csv(file_path)

    # Remove duplicates
    df = df.drop_duplicates(subset=['review_text'])

    # Handle missing data
    df = df.dropna()

    # Normalize dates
    df['date'] = pd.to_datetime(df['date']).dt.strftime('%Y-%m-%d')

    return df

if __name__ == "__main__":
    # Load and preprocess each bank's reviews
    banks = ['CBE', 'BOA', 'Dashen']
    for bank in banks:
        cleaned_data = preprocess_reviews(f'{bank}_reviews.csv')
        cleaned_data.to_csv(f'cleaned_{bank}_reviews.csv', index=False)
        print(f"✅ Cleaned data saved for {bank}")