#!/usr/bin/env python3

import sys

lines = sys.stdin.read().split()

task_states = {}
i = 0
while i < len(lines):
    line = lines[i].split(".")
    name = ".".join(line[:2])
    task_states[name] = line[2]

    i += 1

for task in task_states:
    if task_states[task] == "correct":
        print(task)
