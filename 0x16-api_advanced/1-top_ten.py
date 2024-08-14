#!/usr/bin/python3
"""
Queries the Reddit API to print the titles of the first 10 Hot posts.
"""

import requests


def top_ten(subreddit):
    """
    Function querying the API.
    Prints "None", if the subreddit is not valid.
    """
    r = requests.get(
        "https://www.reddit.com/r/{}/hot.json".format(subreddit),
        headers={"User-Agent": "Custom"},
        params={"limit": 10},
    )

    if r.status_code == 200:
        for get_data in r.json().get("data").get("children"):
            d = get_data.get("data")
            t = d.get("title")
            print(t)
    else:
        print(None)
