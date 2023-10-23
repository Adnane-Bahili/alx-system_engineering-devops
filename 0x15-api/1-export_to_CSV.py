#!/usr/bin/python3
"""Uses the provided REST API along with an employee's ID,
    returns information about the employee's to do list progress"""
import csv
import requests
import sys


if __name__ == '__main__':

    to_do_url = "https://jsonplaceholder.typicode.com/todos?userId={}"

    users = requests.get("https://jsonplaceholder.typicode.com/users/{}".format
                         (sys.argv[1])).json()
    to_do = requests.get(to_do_url.format(sys.argv[1])).json()

    with open("{}.csv".format(sys.argv[1]), 'w', newline='') as export:
        write_task = csv.writer(export, quoting=csv.QUOTE_ALL)
        for task in to_do:
            write_task.writerow([int(sys.argv[1]), users.get('username'),
                                 task.get('completed'),
                                 task.get('title')])
