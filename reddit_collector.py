import requests
import pandas as pd
import os
import time

# My Reddit API setup
url = "https://www.reddit.com/r/all/top.json?limit=10"
headers = {"User-Agent": "python:reddit.stream:v1.0 (by /u/yourusername)"}

file = "reddit_posts.csv"

while True:
    response = requests.get(url, headers=headers)
    data = response.json()

    posts = data['data']['children']
    df = pd.json_normalize(posts)
    df = df[['data.title','data.subreddit','data.score']]
    df.columns = ['title','subreddit','score']

    if not os.path.exists(file):
        df.to_csv(file, index=False)
    else:
        df.to_csv(file, mode='a', header=False, index=False)

    print("Batch saved")
    time.sleep(60)  # wait 60 seconds before next batch