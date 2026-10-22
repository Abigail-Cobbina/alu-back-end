#!/usr/bin/python3
"""Export all employees TODO data to JSON."""
import json
import requests


if __name__ == "__main__":
    users = requests.get(
        "https://jsonplaceholder.typicode.com/users"
    ).json()
    todos = requests.get(
        "https://jsonplaceholder.typicode.com/todos"
    ).json()

    data = {}
    for user in users:
        user_id = user.get("id")
        username = user.get("username")
        data[str(user_id)] = [
            {
                "username": username,
                "task": t.get("title"),
                "completed": t.get("completed")
            } for t in todos if t.get("userId") == user_id
        ]

    with open("todo_all_employees.json", "w") as f:
        json.dump(data, f)
