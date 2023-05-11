#!/usr/bin/python3
"""A func. that queries Reddit API and returns num. of Subs"""

import json
import requests
import sys

def number_of_subscribers(subreddit):
    """This func. takes one parameter"""

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "Custom"}

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()['data']['subscribers']
        return data
    else:
        return 0
