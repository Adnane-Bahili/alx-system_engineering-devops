#!/usr/bin/python3
"""
Queries the Reddit API to determine the subscriber count of a given subreddit.
"""

import requests


def number_of_subscribers(subreddit):
    """
    Function querying the API.
    Returns 0, if the subreddit is not valid.
    """
    r = requests.get(
        "https://www.reddit.com/r/{}/about.json".format(subreddit),
        headers={"User-Agent": "Custom"},
    )
    if r.status_code == 200:
        return r.json().get("data").get("subscribers")
    else:
        return 0
