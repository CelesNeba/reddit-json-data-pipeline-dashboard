# Reddit JSON streaming data pipeline & dashboard

## Project overview

This project demonstrates a **real-time data pipeline** that collects **JSON data from the Reddit API**, processes it, and visualizes insights using an interactive **Streamlit dashboard**.

The system continuously ingests live Reddit posts, transforms the JSON data into a structured dataset, and provides real-time analytics on trending posts and subreddits.

This project simulates a **real-world data engineering workflow**, where streaming data is ingested, processed, and visualized for decision-making.

---

## Project architecture

Reddit API → JSON Data Collection → Data Processing → CSV Storage → Streamlit Dashboard

1. **Reddit API** provides live JSON data.
2. **Python data collector** retrieves and processes the data.
3. JSON fields are transformed into structured tabular data.
4. Data is stored in a continuously updated dataset.
5. **Streamlit dashboard** visualizes insights in real time.

---

## Key Features

- Real-time Reddit data ingestion
- JSON API data processing
- Automated data collection pipeline
- Streaming dataset updates
- Interactive Streamlit dashboard
- Auto-refresh analytics every 30 seconds
- Visualization of trending subreddits and posts

---

## Dashboard analytics

The Streamlit dashboard provides:

- **Top subreddits**  
  Bar chart showing the most frequent subreddits in collected posts.

- **Top Posts by score**  
  Ranking of the highest-scoring Reddit posts.

- **Live dataset view**  
  Real-time display of collected Reddit data.

- **Total posts collected metric**  
  Live counter of ingested posts.

---

## Tech stack / Tools

Python  
Pandas  
Requests  
Streamlit  
Altair  
JSON API  

---

## Project structure



reddit-json-data-pipeline-dashboard/
│
├── reddit_collector.py # Collects Reddit JSON data

├── dashboard.py # Streamlit dashboard

├── run_all.bat # Runs collector + dashboard

├── README.md # Project documentation

└── .gitignore



---

## Installation

- Clone the repository:


git clone https://github.com/CelesNeba/reddit-json-data-pipeline-dashboard.git
cd reddit-json-data-pipeline-dashboard


1. Create a virtual environment:
 
- python -m venv env

2. Activate the environment:

   Windows:

   env\Scripts\activate

3. Install dependencies:

    - pip install requests pandas streamlit altair streamlit-autorefresh
  
### Running the project

1. Start the Reddit data collector:

- python reddit_collector.py

2. Open a new terminal and run the dashboard:

- streamlit run dashboard.py

3. The dashboard will open automatically in your browser:

- http://localhost:8501

## Example data fields (JSON → structured data)

- The Reddit API returns JSON objects containing fields such as:

1. title
2. subreddit
3. score
4. author
5. created_utc

These are transformed into structured tabular data for analysis.


### Purpose of this project

This project was built to demonstrate skills in:

- API data ingestion

- JSON data transformation

- Data pipeline development

- Real-time data processing

- Data visualization dashboards

- Python-based analytics workflows

### Potential improvements

Future enhancements could include:

- Kafka streaming pipeline

- Database storage (PostgreSQL)

- Docker containerization

- Cloud deployment (AWS / Azure)

- Sentiment analysis on Reddit posts

- Time-series analytics


##  Reddit trending posts dashboard

The main analytics dashboard provides a live overview of collected Reddit data, including trending subreddits, post rankings, and dataset updates.

![Reddit Trending Posts Dashboard](https://raw.githubusercontent.com/CelesNeba/reddit-json-data-pipeline-dashboard/main/json%20main%20board%20screenshot.PNG)

### Collected Reddit Data

The dashboard also displays the structured dataset generated from the Reddit JSON API, allowing users to view the processed data in real time.

Key fields include:

- **title** – Reddit post title  
- **subreddit** – Source subreddit  
- **score** – Post popularity score  

This table represents the transformation of raw JSON API responses into structured data suitable for analytics and visualization.









##  Dashboard preview

Below is a snapshot of the real-time Streamlit dashboard used to visualize the Reddit JSON data pipeline.

![Reddit JSON Dashboard](https://github.com/CelesNeba/reddit-json-data-pipeline-dashboard/blob/main/json%20dashboard%20screenshot.PNG)

The dashboard provides live insights including:

- Top subreddits based on collected posts
- Ranking of the highest scoring Reddit posts
- Real-time dataset updates
- Total posts collected metric
- Automatic refresh every 30 seconds

This visualization demonstrates how raw JSON API data can be transformed into meaningful analytics using Python and Streamlit.





# 👤 Author

**Celestine Neba**  
ETL | Data Engineering | Data Analytics  
BSc Computer Science

## About the Author

Celestine Neba is a data professional with a background in Computer Science and a strong interest in data engineering, ETL pipelines, and analytics. I focus on building practical data solutions that transform raw data into meaningful insights.

My work includes developing data pipelines, processing API-based JSON data, and building interactive dashboards to support data-driven decision-making.

This project is part of my growing portfolio, demonstrating skills in data ingestion, transformation, and visualization using modern Python data tools.
