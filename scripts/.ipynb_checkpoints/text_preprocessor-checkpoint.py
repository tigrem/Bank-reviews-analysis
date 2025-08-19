# scripts/text_preprocessor.py
import spacy
from spacy.lang.en.stop_words import STOP_WORDS

# Load spaCy model once
try:
    nlp = spacy.load('en_core_web_sm')
except OSError:
    print("Downloading spaCy model 'en_core_web_sm'. This will only happen once.")
    from spacy.cli import download
    download('en_core_web_sm')
    nlp = spacy.load('en_core_web_sm')

def preprocess_text(text):
    """
    Performs text preprocessing: tokenization, stop-word removal, and lemmatization.
    
    Args:
        text (str): The raw review text.
        
    Returns:
        str: The preprocessed text string.
    """
    doc = nlp(text)
    tokens = [
        token.lemma_ for token in doc 
        if token.text.lower() not in STOP_WORDS and token.is_alpha
    ]
    return ' '.join(tokens)

def preprocess_reviews_with_text(df):
    """
    Applies text preprocessing to a DataFrame's 'review_text' column.
    
    Args:
        df (pd.DataFrame): The DataFrame to process.
    
    Returns:
        pd.DataFrame: The DataFrame with a new 'processed_review' column.
    """
    df['processed_review'] = df['review_text'].apply(preprocess_text)
    return df