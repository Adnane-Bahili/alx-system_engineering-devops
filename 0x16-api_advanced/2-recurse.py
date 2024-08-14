#!/usr/bin/python3
"""
Queries the Reddit API to return a list of all the hot articles of a subreddit
"""

import requests


def recurse(subreddit, hot_list=[], after=""):
    """
    Queries the Reddit API and gives a list of the titles
    of all hot articles of a given subreddit.
    Returns "None" If no valid subreddit is found.
    """
    r = requests.get(
        "https://www.reddit.com/r/{}/hot.json".format(subreddit),
        headers={"User-Agent": "Custom"},
        params={"after": after},
    )
    if r.status_code == 200:
        for get_data in r.json().get("data").get("children"):
            dat = get_data.get("data")
            t = d.get("title")
            hot_list.append(t)
        after = r.json().get("data").get("after")

        if after is None:
            return hot_list
        else:
            return recurse(subreddit, hot_list, after)
    else:
        return None
