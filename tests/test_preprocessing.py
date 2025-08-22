# tests/test_preprocessing.py

import pandas as pd
import pytest
import sys
import os

# Add the parent directory to the system path to allow imports from scripts
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from scripts.preprocess_reviews import drop_duplicates_and_nan, normalize_dates
from scripts.text_preprocessor import preprocess_text

# --- Test Data ---
@pytest.fixture
def sample_dataframe():
    """Provides a sample DataFrame for testing."""
    data = {
        'review_text': ['great app', 'great app', 'bugs and errors', 'works well', 'another review', None],
        'rating': [5, 5, 1, 4, 3, 2],
        'date': ['2025-01-01', '2025-01-01', '2025-01-02', '2025-01-03', '2025-01-04', '2025-01-05'],
        'bank_name': ['A', 'A', 'B', 'B', 'C', 'C']
    }
    return pd.DataFrame(data)

# --- Unit Tests for Preprocessing Functions ---

def test_drop_duplicates_and_nan(sample_dataframe):
    """Test if duplicates and rows with NaN values are correctly dropped."""
    df = drop_duplicates_and_nan(sample_dataframe)

    # Check for correct number of rows after dropping duplicates and NaNs
    # Original: 6 rows
    # Duplicates: 1 (row 1 is same as row 0)
    # NaNs: 1 (row 5 has NaN in review_text)
    # Expected final rows: 4
    assert len(df) == 4

    # Check if the duplicate 'great app' is removed
    assert df['review_text'].duplicated().sum() == 0

    # Check if the row with a NaN value is removed
    assert df['review_text'].isnull().sum() == 0

def test_normalize_dates(sample_dataframe):
    """Test if the date column is correctly normalized to YYYY-MM-DD format."""
    df = normalize_dates(sample_dataframe)

    # Get the format of the first non-null date
    first_date = df['date'].iloc[0]

    # The expected format should be YYYY-MM-DD
    expected_format = '%Y-%m-%d'

    # Check if the date can be parsed to the expected format
    try:
        pd.to_datetime(first_date).strftime(expected_format)
        date_format_is_correct = True
    except ValueError:
        date_format_is_correct = False

    assert date_format_is_correct

def test_preprocess_text():
    """Test if text is correctly cleaned (lowercase, lemmatized, stopwords removed)."""
    text = "The app is working GREAT, but the login process is a pain."
    processed_text = preprocess_text(text)

    # We expect 'The', 'is', 'a' to be removed, and 'working', 'pain' to be lemmatized.
    expected_output = "app work great login process pain"

    assert processed_text == expected_output