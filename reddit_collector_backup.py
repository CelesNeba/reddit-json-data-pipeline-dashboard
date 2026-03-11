import requests
import pandas as pd

url = "https://www.reddit.com/r/all/top.json?limit=10"

headers = {
    "User-Agent": "reddit-data-project"
}

response = requests.get(url, headers=headers)
data = response.json()

posts = []

for post in data["data"]["children"]:
    posts.append({
        "title": post["data"]["title"],
        "subreddit": post["data"]["subreddit"],
        "score": post["data"]["score"]
    })

df = pd.DataFrame(posts)

print(df)
import os
import os

file = "reddit_posts.csv"

if not os.path.exists(file):
    df.to_csv(file, index=False)
else:
    df.to_csv(file, mode='a', header=False, index=False)

print("Data saved to reddit_posts.csv")