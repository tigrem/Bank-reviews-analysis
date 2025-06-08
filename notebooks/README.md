# Mobile Banking App Review Analysis for Omega Consultancy

## Project Overview

This project, undertaken for Omega Consultancy, focuses on enhancing customer retention and satisfaction for mobile banking applications. As a Data Analyst, the core objective was to extract, analyze, and interpret user feedback from Google Play Store reviews for three prominent banks: **Commercial Bank of Ethiopia (CBE)**, **Bank of Abyssinia (BOA)**, and **Dashen Bank**. The insights derived are intended to guide strategic improvements for product, marketing, and engineering teams, addressing key areas such as user retention, feature enhancement, and efficient complaint management.

## Project Objectives

The project aimed to achieve the following:
* **Scrape user reviews** from the Google Play Store.
* Perform **sentiment analysis** (positive/negative/neutral) and **extract themes** (e.g., "bugs", "UI").
* Identify crucial **satisfaction drivers** (e.g., "speed") and **pain points** (e.g., "crashes").
* **Store cleaned and analyzed review data** in an Oracle relational database.
* Deliver a comprehensive **report with visualizations** and **actionable recommendations**.

## Scenarios Addressed

This analysis directly supports banking teams in the following simulated real-world scenarios:

1.  **Retaining Users:** Analyze complaints (e.g., "slow loading during transfers") to determine broader issues and suggest app investigation areas (e.g., comparing CBE 4.4-star, BOA 2.8-star, Dashen 4.0-star ratings).
2.  **Enhancing Features:** Extract desired features (e.g., "transfer", "fingerprint login", "faster loading times") through keyword and theme extraction, recommending competitive strategies for each bank.
3.  **Managing Complaints:** Cluster and track common complaints (e.g., "login error") to inform AI chatbot integration and strategies for faster support resolution.

## Technologies and Libraries Used

* **Python:** Primary programming language for data processing, analysis, and database interaction.
* **`google-play-scraper`:** For web scraping mobile app reviews from Google Play Store.
* **`pandas`:** For efficient data manipulation, cleaning, and analysis.
* **`spaCy`:** For natural language processing (tokenization, lemmatization, stop-word removal).
* **`TfidfVectorizer` (from `sklearn.feature_extraction.text`):** For keyword and n-gram extraction.
* **`vaderSentiment`:** For sentiment analysis (as per initial Task 2 description for alternative methods).
* **`matplotlib` & `seaborn`:** For data visualization and plotting.
* **`WordCloud`:** For generating visual representations of prominent keywords.
* **Oracle Database (Oracle XE - `LOCALCR` instance):** For persistent storage of cleaned and processed review data.
* **`cx_Oracle`:** Python driver for connecting to and interacting with Oracle Database.
* **SQL Developer / SQL*Plus:** For database schema management and verification.
* **Git / GitHub:** For version control and collaborative development.

## Project Structure & Tasks Completed

The project was structured into four key tasks, each building upon the previous one:

### Task 1: Data Collection and Preprocessing
* **Objective:** Scrape user reviews and prepare them for analysis.
* **Methodology:**
    * **Git Setup:** Established a GitHub repository (`Bank-reviews-analysis`) with `.gitignore` and `requirements.txt`. Maintained frequent, meaningful commits on the `task-1` branch.
    * **Web Scraping:** Used `google-play-scraper` to collect over 400 reviews per bank (1,200+ total) for CBE, BOA, and Dashen.
    * **Preprocessing:** Implemented Python scripts to remove duplicate reviews, handle missing data, and normalize dates to `YYYY-MM-DD` format.
* **Output:** Cleaned review data saved as CSV files (`cleaned_CBE_reviews.csv`, `cleaned_BOA_reviews.csv`, `cleaned_Dashen_reviews.csv`) with columns: `review_text`, `rating`, `date`, `bank_name`, `source`.

### Task 2: Sentiment and Thematic Analysis
* **Objective:** Quantify review sentiment and identify recurring themes.
* **Methodology:**
    * **Sentiment Analysis:** Applied `vaderSentiment` (as initially specified) or `distilbert-base-uncased-finetuned-sst-2-english` (as per code implementation) to assign sentiment scores and labels (positive, negative, neutral) to reviews.
    * **Thematic Analysis:** Utilized `spaCy` for text cleaning (tokenization, lemmatization, stop-word removal) and `TfidfVectorizer` for keyword extraction. Grouped keywords into 5 overarching themes: 'Account Access Issues', 'Transaction Performance', 'User Interface & Experience', 'Customer Support', and 'Feature Requests'.
* **Output:** Processed dataframes including `processed_review`, `sentiment_score`, and `sentiment` (or `sentiment_label`), saved to CSV files (`processed_reviews_CBE.csv`, etc.).

### Task 3: Store Cleaned Data in Oracle
* **Objective:** Design and implement a relational database in Oracle to store the cleaned and processed review data persistently.
* **Methodology:**
    * **Oracle Database Setup:** Used an existing Oracle XE instance (`LOCALCR` - identified as a Non-CDB).
    * **Schema Definition:** Created a dedicated user (schema) named `BANK_REVIEWS` within the `LOCALCR` database. Defined `Banks` and `Reviews` tables with appropriate data types (`VARCHAR2`, `NUMBER`, `DATE`, `CLOB`) and constraints (`PRIMARY KEY`, `FOREIGN KEY`, `NOT NULL`). A sequence and trigger were implemented to auto-populate `review_id`.
    * **Data Insertion:** Developed a Python script using `cx_Oracle` to connect to the `BANK_REVIEWS` schema in `LOCALCR` and batch insert the combined processed review data from CSVs into the `reviews` table.
* **KPIs Achieved:**
    * Successfully established connection and insert script.
    * `reviews` table populated with over 1,200 entries.
    * SQL DDL for schema committed to GitHub.

### Task 4: Insights and Recommendations
* **Objective:** Derive actionable insights, visualize results, and recommend app improvements.
* **Methodology:**
    * **Data Loading:** Loaded processed review data directly from the Oracle `reviews` table into a Pandas DataFrame.
    * **Insights:** Identified 2+ drivers (e.g., efficient UI/UX, high performance) and 2+ pain points (e.g., app stability issues, slow operations) by analyzing positive/negative sentiment trends and top keywords per bank. Performed bank comparisons based on average ratings and sentiment distributions.
    * **Visualizations:** Generated the following plots using `matplotlib` and `seaborn`:
        * Overall Rating Distribution.
        * Overall Sentiment Distribution (Pie Chart).
        * Average Rating per Bank (Bar Plot).
        * Monthly Average Sentiment Score Trend by Bank (Line Plot).
        * Word Cloud for Top Positive Keywords (Drivers).
        * Word Cloud for Top Negative Keywords (Pain Points).
    * **Ethical Considerations:** Acknowledged potential review biases (e.g., negative skew), language nuances, and representativeness limitations in the analysis.
* **KPIs Achieved:**
    * Identified multiple drivers and pain points with supporting evidence.
    * Produced clear, labeled visualizations.
    * Provided practical, actionable recommendations for app improvements.

## Key Insights & Recommendations (Summary)

* **Sentiment Overview:** Dashen Bank demonstrates the highest positive sentiment, followed by CBE, with BOA having a more mixed to negative sentiment distribution, indicating significant areas for improvement.
* **Common Pain Points:** App stability (crashes), transaction performance (slow loading, transfer issues), and customer support responsiveness are recurring themes, particularly prominent for BOA.
* **Key Drivers:** User-friendly interfaces, efficient core banking functionalities (fast transfers, easy payments), and comprehensive digital experiences (e.g., Dashen's "superapp" features) are strong drivers of satisfaction.
* **Recommendations include:**
    * **Prioritizing app stability and bug fixes, especially for BOA.**
    * **Enhancing money transfer and transaction features** with clear feedback and addressing specific limitations.
    * **Improving customer support accessibility and responsiveness**, potentially via in-app chatbots for common queries.
    * **Focusing on UI/UX for speed and ease of use**, capitalizing on positive feedback for quick and simple interactions.
    * **Exploring value-added features** like budgeting tools or biometric authentication to increase engagement.

## Ethical Considerations

The analysis was conducted with awareness of potential biases inherent in user-generated content, such as a possible negative skew in reviews. The limitations of automated sentiment analysis (e.g., inability to perfectly capture sarcasm or context) and the representativeness of Google Play reviews (not encompassing all user demographics) were considered. All data handling respected user privacy by focusing on aggregated, anonymized insights.

## Setup and Usage

To set up and run this project:

1.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/tigrem/Bank-reviews-analysis.git)
    cd Bank-reviews-analysis
    ```
    (Replace `your-username` with your actual GitHub username if this is a public repo).

2.  **Create a Virtual Environment (Recommended):**
    ```bash
    python -m venv venv
    # On Windows:
    .\venv\Scripts\activate
    # On macOS/Linux:
    source venv/bin/activate
    ```

3.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
    (Ensure `requirements.txt` contains all listed libraries: `cx_Oracle`, `pandas`, `matplotlib`, `seaborn`, `wordcloud`, `scikit-learn`, `google-play-scraper`, `spacy`, `vaderSentiment`)

4.  **Oracle Database Setup:**
    * Ensure Oracle Database Express Edition (XE) is installed and running (`LOCALCR` service).
    * Connect as `SYS` or `SYSTEM` to `LOCALCR`.
    * Create the `BANK_REVIEWS` user (schema) and grant necessary privileges as described in Task 3.
    * Create the `Banks` and `Reviews` tables (and the `reviews_seq` sequence and `trg_reviews_id` trigger for `review_id` auto-population) within the `BANK_REVIEWS` schema. Refer to the SQL DDL in the repository.

5.  **Run Data Collection and Preprocessing (Task 1):**
    * Execute the script for Task 1 to scrape and clean data. This will generate `cleaned_BANK_reviews.csv` files.

6.  **Run Sentiment and Thematic Analysis (Task 2):**
    * Execute the script for Task 2. This will generate `processed_reviews_BANK.csv` files.

7.  **Run Data Insertion into Oracle (Task 3):**
    * Update the `username` and `password` variables in the Oracle insertion script (`oracle_db_insert.py` or similar) to match your `BANK_REVIEWS` user credentials.
    * Run the script to insert data into your Oracle database.

8.  **Run Insights and Recommendations (Task 4):**
    * Update the `username