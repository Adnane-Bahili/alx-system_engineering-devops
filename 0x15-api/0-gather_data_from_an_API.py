#!/usr/bin/python3
"""Uses the provided REST API along with an employee's ID,
    returns information about the employee's to do list progress"""
import requests
import sys


if __name__ == '__main__':

    to_do_url = "https://jsonplaceholder.typicode.com/todos?userId={}"

    users = requests.get("https://jsonplaceholder.typicode.com/users/{}".format
                         (sys.argv[1])).json()
    to_do = requests.get(to_do_url.format(sys.argv[1])).json()

    completed_tasks = []
    for tasks in to_do:
        if tasks.get('completed') is True:
            completed_tasks.append(tasks.get('title'))
    print("Employee {} is done with tasks({}/{}):".
          format(users.get('name'), len(completed_tasks), len(to_do)))
    print("\n".join("\t {}".format(tasks) for tasks in completed_tasks))
