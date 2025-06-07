# scripts/text_preprocessor.py
import spacy
from spacy.lang.en.stop_words import STOP_WORDS

nlp = spacy.load('en_core_web_sm')

def preprocess_text(text):
    doc = nlp(text)
    tokens = [token.lemma_ for token in doc if token.text not in STOP_WORDS and token.is_alpha]
    return ' '.join(tokens)

def preprocess_reviews(df):
    df['processed_review'] = df['review_text'].apply(preprocess_text)
    return df  # Corrected this line to return df