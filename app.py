# app.py
import streamlit as st
import pandas as pd
import plotly.express as px
import os

# --- Load Data ---
# We assume the analysis notebook has been run and the file is saved.
DATA_DIR = 'notebooks/data'
try:
    df = pd.read_csv(os.path.join(DATA_DIR, 'final_analyzed_reviews.csv'))
except FileNotFoundError:
    st.error("Data file not found. Please run the analysis notebook to generate 'final_analyzed_reviews.csv'.")
    st.stop()

# Convert date column to datetime for proper sorting
df['date'] = pd.to_datetime(df['date'])

# --- Streamlit App Configuration ---
st.set_page_config(layout="wide", page_title="Bank Reviews Analysis")
st.title("🏦 Ethiopian Bank Reviews Dashboard")
st.markdown("### A Look at Customer Feedback Across Top Ethiopian Banks")

# --- Key Metrics ---
st.header("Overall Performance Metrics")
col1, col2, col3 = st.columns(3)
total_reviews = len(df)
avg_rating = df['rating'].mean()
positive_percent = (df[df['sentiment'] == 'positive'].shape[0] / total_reviews) * 100

col1.metric("Total Reviews Analyzed", total_reviews)
col2.metric("Average Rating", f"{avg_rating:.2f} / 5")
col3.metric("Positive Sentiment", f"{positive_percent:.2f}%")

# --- Visualizations ---
st.header("Sentiment & Thematic Insights")

# Overall Sentiment Distribution
st.markdown("#### Overall Sentiment Distribution")
sentiment_counts = df['sentiment'].value_counts().reset_index()
sentiment_counts.columns = ['Sentiment', 'Count']
fig_pie = px.pie(sentiment_counts, values='Count', names='Sentiment', title='Overall Sentiment Distribution', hole=0.3)
st.plotly_chart(fig_pie, use_container_width=True)

# Sentiment Distribution by Bank
st.markdown("#### Sentiment Distribution by Bank")
sentiment_by_bank = df.groupby('bank_name')['sentiment'].value_counts(normalize=True).mul(100).rename('Percentage').reset_index()
fig_bar = px.bar(sentiment_by_bank, x='bank_name', y='Percentage', color='sentiment',
                 title='Sentiment Distribution by Bank', barmode='group')
st.plotly_chart(fig_bar, use_container_width=True)

# Top Negative Themes
st.markdown("#### Top Negative Review Themes")
negative_reviews_text = ' '.join(df[df['sentiment'] == 'negative']['processed_review'].dropna())
if negative_reviews_text:
    from collections import Counter
    words = negative_reviews_text.split()
    word_counts = Counter(words)
    common_words = pd.DataFrame(word_counts.most_common(10), columns=['Word', 'Count'])
    fig_themes = px.bar(common_words, x='Word', y='Count', title='Top 10 Most Frequent Words in Negative Reviews')
    st.plotly_chart(fig_themes, use_container_width=True)
else:
    st.info("Not enough negative reviews to analyze themes.")

# --- Raw Data Table ---
st.header("Review Data")
st.dataframe(df[['review_text', 'bank_name', 'rating', 'sentiment', 'sentiment_score', 'date']].head(50))