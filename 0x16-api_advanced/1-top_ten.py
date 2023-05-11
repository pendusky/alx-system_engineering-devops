#!/usr/bin/python3
"""A function that queries Reddit API and returns top ten hot post"""

import json
import requests

def top_ten(subreddit):
    """This func. takes one parameter"""

    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {"User-Agent": "Custom User Agent"}

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()['data']['children']
        for post in data:
            print(post['data']['title'])
        else:
            print(None)
