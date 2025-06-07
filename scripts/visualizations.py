# scripts/visualizations.py
import matplotlib.pyplot as plt
from wordcloud import WordCloud

def plot_sentiment_distribution(df):
    df['sentiment'].value_counts().plot(kind='bar', color=['green', 'red', 'blue'])
    plt.title(f'Sentiment Distribution')
    plt.xlabel('Sentiment')
    plt.ylabel('Count')
    plt.show()

def generate_wordcloud(text, title):
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title(title)
    plt.show()