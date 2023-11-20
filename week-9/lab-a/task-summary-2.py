#!/usr/bin/env python3

import sys

tasks = sys.stdin.read().split()
data = {}
i = 0
while i < len(tasks):
    ri = len(tasks) - i - 1
    user = tasks[ri].split("/")[0]
    task = tasks[ri].split("/")[1].split(".")[0] + ".py"
    correct = tasks[ri].split(".")[2] == "correct"

    if user not in data:
        data[user] = {"correct": {}, "incorrect": {}}

    if task not in data[user]["incorrect"] and correct:
        data[user]["correct"][task] = 1
    elif task not in data[user]["correct"] and not correct:
        data[user]["incorrect"][task] = 1

    i += 1

for user in data:
    print(user, len(data[user]["correct"]))
