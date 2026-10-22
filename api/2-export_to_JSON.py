#!/usr/bin/python3
"""Export employee TODO data to JSON."""
import json
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

    username = user.get("username")
    data = {str(user_id): [
        {
            "task": t.get("title"),
            "completed": t.get("completed"),
            "username": username
        } for t in todos
    ]}

    with open("{}.json".format(user_id), "w") as f:
        json.dump(data, f)
