# scripts/keyword_extraction.py
from sklearn.feature_extraction.text import TfidfVectorizer

def extract_keywords(df):
    vectorizer = TfidfVectorizer(max_features=100)
    X = vectorizer.fit_transform(df['processed_review'])
    return vectorizer.get_feature_names_out()

def cluster_keywords(keywords):
    themes = {
        "Account Access Issues": ["login", "access", "error"],
        "Transaction Performance": ["transfer", "delay", "slow"],
        "User Interface & Experience": ["UI", "design", "easy"],
        "Customer Support": ["support", "help", "service"],
        "Feature Requests": ["feature", "request", "add"]
    }
    return themes