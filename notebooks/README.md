Mobile Banking App Review Analysis for Omega Consultancy

Project Overview

This project, developed for Omega Consultancy, focuses on enhancing customer retention and satisfaction for mobile banking applications. As a Data Analyst, the core objective was to build an end-to-end data pipeline to automatically extract, analyze, and interpret user feedback from Google Play Store reviews for five prominent Ethiopian banks: Commercial Bank of Ethiopia (CBE), Bank of Abyssinia (BOA), Dashen Bank, Awash Bank, and Zemen Bank.

The final output is an interactive dashboard that provides actionable insights to guide strategic improvements for product, marketing, and engineering teams. This analysis addresses key areas such as user retention, feature enhancement, and efficient complaint management.

Project Objectives

The project successfully achieved the following objectives:

    Scrape over 2,800 user reviews from the Google Play Store using a robust pipeline.

    Clean and preprocess raw review data, handling missing values and duplicates.

    Perform sentiment analysis to quantify user opinions (positive/negative/neutral).

    Extract recurring themes and keywords (e.g., "bugs", "UI", "speed") from user comments.

    Store all cleaned and analyzed data in a persistent Oracle relational database.

    Deliver an interactive dashboard with key metrics and visualizations for a clear and immediate understanding of customer sentiment and pain points.

Scenarios Addressed

This analysis directly supports banking teams in the following simulated real-world scenarios:

    Retaining Users: By analyzing common complaints (e.g., "slow loading during transfers"), the analysis determines broader issues and suggests areas for app investigation and optimization.

    Enhancing Features: By extracting desired features (e.g., "fingerprint login", "faster loading times") through keyword and theme extraction, the project provides competitive strategies for each bank.

    Managing Complaints: By clustering and tracking common complaints (e.g., "login error"), the insights can inform strategies for faster support resolution, potentially via in-app chatbots.

Technologies and Libraries Used

    Python: Primary programming language for the entire data pipeline.

    google-play-scraper: For web scraping mobile app reviews.

    pandas: For efficient data manipulation, cleaning, and analysis.

    spacy: For natural language processing (tokenization, lemmatization, stop-word removal).

    scikit-learn: For keyword and n-gram extraction using TfidfVectorizer.

    vaderSentiment: For sentiment analysis, providing sentiment scores and labels.

    tqdm: For displaying progress bars, enhancing user experience for long-running tasks.

    oracledb: Python driver for connecting to and interacting with Oracle Database.

    SQL Developer / SQL*Plus: For database schema management.

    streamlit: For building the interactive, web-based dashboard.

    plotly: For creating professional and interactive data visualizations.

    Git / GitHub: For version control.

Project Structure & Tasks Completed

The project was structured into a complete data pipeline, ensuring each stage is verifiable and robust.

    Task 1: Data Collection and Preprocessing (Completed)

        Objective: Scrape user reviews and prepare them for analysis.

        Methodology: A robust Python script was used to scrape over 2,800 reviews from five different banks. The script includes error handling to gracefully manage empty or malformed data. Data was then cleaned to remove duplicates, handle missing values, and normalize dates.

        Output: Raw and cleaned review data for each bank were saved as CSV files in the notebooks/data directory, with a final combined file named all_processed_reviews.csv.

    Task 2: Sentiment and Thematic Analysis (Completed)

        Objective: Quantify review sentiment and identify recurring themes.

        Methodology: The vaderSentiment library was used to assign a sentiment score and a corresponding label (positive, negative, or neutral) to each review. spaCy and TfidfVectorizer were utilized to identify the most frequent and important keywords in both positive and negative reviews.

        Output: The combined DataFrame was enriched with new sentiment_score and sentiment columns and saved as final_analyzed_reviews.csv.

    Task 3: Data Persistence (Completed)

        Objective: Design and implement a relational database to store the processed data.

        Methodology: A schema with Banks and Reviews tables was defined in an Oracle Database. A Python script using the oracledb library was developed to connect to the database and insert the combined, analyzed data. This ensures the data is permanently stored for future use or reporting.

        KPIs Achieved: Successfully established a connection, created the schema, and populated the tables with over 2,800 entries.

    Task 4: Interactive Dashboard & Final Presentation (In Progress)

        Objective: Visualize key insights and present actionable recommendations via an interactive dashboard.

        Methodology: An interactive dashboard is being built using Streamlit and Plotly. The dashboard will display key metrics and visualizations, including overall sentiment distribution, sentiment by bank, and top themes in negative reviews.

        Output: A live, interactive web application (app.py) that presents project findings in a clear and compelling format.

Key Insights & Recommendations (Summary)

    Overall Sentiment: The analysis provides a clear overview of customer sentiment, allowing banks to be benchmarked against each other.

    Common Pain Points: App stability (crashes), transaction performance (slow transfers), and customer support responsiveness are recurring themes.

    Key Drivers: User-friendly interfaces, efficient core banking functionalities, and comprehensive digital experiences are strong drivers of satisfaction.

Setup and Usage

To set up and run this project, follow these steps:

    Clone the Repository:
    Bash

git clone [https://github.com/tigrem/Bank-reviews-analysis.git]
cd Bank-reviews-analysis

Create a Virtual Environment (Recommended):
Bash

python -m venv venv
# On Windows:
.\venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

Install Dependencies:
Bash

pip install pandas google-play-scraper spacy scikit-learn vaderSentiment tqdm oracledb streamlit plotly

Oracle Database Setup:

    Ensure an Oracle Database instance is running and accessible.

    Create a .env file in the root directory with your database credentials:
    Ini, TOML

    ORACLE_DB_USER=your_username
    ORACLE_DB_PASSWORD=your_password
    ORACLE_DB_DSN=your_dsn_string

Run the Data Pipeline:

    Open the main Jupyter notebook and run all the cells to scrape, clean, analyze, and save the data to a CSV and your database.

Run the Interactive Dashboard:

    From your terminal, in the project's root directory, run:

Bash

streamlit run app.py