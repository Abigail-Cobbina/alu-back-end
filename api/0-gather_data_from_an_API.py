#!/usr/bin/python3
"""Gather data from an API and display TODO list progress."""
import requests
import sys


if __name__ == "__main__":
    user_id = int(sys.argv[1])
    user = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}".format(user_id)
    ).json()
    todos = requests.get(
        "https://jsonplaceholder.typicode.com/todos?userId={}".format(user_id)
    ).json()

    done = [t for t in todos if t.get("completed")]
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(done), len(todos)))
    for task in done:
        print("\t {}".format(task.get("title")))
