#!/usr/bin/env python3

import sys

tasks = sys.stdin.read().split()
i = 0
while i < len(tasks) // 2:
    tmp = tasks[i]
    tasks[i] = tasks[len(tasks) - i - 1]
    tasks[len(tasks) - i - 1] = tmp

    i += 1

user_data = {}
i = 0
while i < len(tasks):
    user = tasks[i].split("/")[0]
    task = tasks[i].split("/")[1].split(".")[0] + ".py"
    correct = tasks[i].split(".")[2] == "correct"

    if user not in user_data:
        user_data[user] = {"correct": {}, "incorrect": {}}

    if task not in user_data[user]["incorrect"] and correct:
        user_data[user]["correct"][task] = 1
    elif task not in user_data[user]["correct"] and not correct:
        user_data[user]["incorrect"][task] = 1

    i += 1

for user in user_data:
    print(user, len(user_data[user]["correct"]))
