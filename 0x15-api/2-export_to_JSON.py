#!/usr/bin/python3
"""Uses the provided REST API along with an employee's ID,
    returns information about the employee's to do list progress"""
import json
import requests
import sys


if __name__ == '__main__':

    to_do_url = "https://jsonplaceholder.typicode.com/todos?userId={}"

    users = requests.get("https://jsonplaceholder.typicode.com/users/{}".format
                         (sys.argv[1])).json()
    to_do = requests.get(to_do_url.format(sys.argv[1])).json()
    user_name = users.get('username')

    tasks = []
    for task in to_do:
        task_dict = {}
        task_dict["task"] = task.get('title')
        task_dict["completed"] = task.get('completed')
        task_dict["username"] = user_name
        tasks.append(task_dict)

    json_obj = {}
    json_obj[sys.argv[1]] = tasks
    with open("{}.json".format(sys.argv[1]), 'w') as file_json:
        json.dump(json_obj, file_json)
