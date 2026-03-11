import os
import pandas as pd
import streamlit as st
import altair as alt
from streamlit_autorefresh import st_autorefresh

# ------------------------------
# Auto-refresh every 30 seconds
# ------------------------------
st_autorefresh(interval=30*1000, key="data_refresh")

# ------------------------------
# Page title
# ------------------------------
st.title("Reddit Trending Posts Dashboard")

# ------------------------------
# Load CSV safely
# ------------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(BASE_DIR, "reddit_posts.csv")

if os.path.exists(csv_path):
    df = pd.read_csv(csv_path)
    df["subreddit"] = df["subreddit"].astype(str).str.strip().str.lower()
else:
    st.warning("reddit_posts.csv not found. Run reddit_collector.py first.")
    st.stop()

# ------------------------------
# Show raw collected data
# ------------------------------
st.subheader("Collected Reddit Data")
st.dataframe(df)

# ------------------------------
# Top Subreddits Bar Chart (all dark blue)
# ------------------------------
st.subheader("Top Subreddits")

# Count top 20 subreddits
subreddit_counts = df["subreddit"].value_counts().head(20).reset_index()
subreddit_counts.columns = ["subreddit", "count"]

# Use a single dark-blue color for all bars
bars = alt.Chart(subreddit_counts).mark_bar(color="#1F3B73").encode(
    x=alt.X("subreddit", sort="-y"),
    y="count",
    tooltip=["subreddit", "count"]
)

# Add data labels
text = bars.mark_text(
    align='center',
    baseline='bottom',
    dy=-5,
    color='black'
).encode(
    text='count:Q'
)

chart = bars + text
st.altair_chart(chart, use_container_width=True)

# ------------------------------
# Top Posts by Score
# ------------------------------
st.subheader("Top Posts by Score")

top_posts = df.sort_values(by="score", ascending=False).head(10)
# No highlight on top post, just uniform table
st.dataframe(top_posts)

# ------------------------------
# Live Metric
# ------------------------------
st.metric("Total Posts Collected", len(df))