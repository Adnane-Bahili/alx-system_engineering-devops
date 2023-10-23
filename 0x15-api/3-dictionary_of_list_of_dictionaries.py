#!/usr/bin/python3
"""Uses the provided REST API along with an employee's ID,
    returns information about the employee's to do list progress"""
import json
import requests


if __name__ == '__main__':
    users = requests.get("https://jsonplaceholder.typicode.com/users").json()
    user_dic = {}
    user_name_dic = {}
    for user in users:
        user_id = user.get("id")
        user_dic[user_id] = []
        user_name_dic[user_id] = user.get("username")
    to_do = requests.get("https://jsonplaceholder.typicode.com/todos").json()
    for tasks in to_do:
        task_dic = {}
        user_id = tasks.get("userId")
        task_dic["task"] = tasks.get('title')
        task_dic["completed"] = tasks.get('completed')
        task_dic["username"] = user_name_dic.get(user_id)
        user_dic.get(user_id).append(task_dic)
    with open("todo_all_employees.json", 'w') as file_json:
        json.dump(user_dic, file_json)
