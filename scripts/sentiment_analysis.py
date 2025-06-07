# scripts/sentiment_analysis.py
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()

def analyze_sentiment(review):
    sentiment = analyzer.polarity_scores(review)
    return sentiment['compound']

def classify_sentiment(score):
    if score >= 0.05:
        return 'positive'
    elif score <= -0.05:
        return 'negative'
    else:
        return 'neutral'

def perform_sentiment_analysis(df):
    df['sentiment_score'] = df['processed_review'].apply(analyze_sentiment)
    df['sentiment'] = df['sentiment_score'].apply(classify_sentiment)
    return df