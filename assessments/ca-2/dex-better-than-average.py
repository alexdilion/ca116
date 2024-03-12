#!/usr/bin/env python3

import sys

lines = sys.stdin.read().strip().split("\n")
avg = 0
i = 0
while i < len(lines):
    mark = lines[i].split()[2]
    avg += int(mark)
    i += 1

avg = avg // len(lines)
i = 0
while i < len(lines):
    mark = int(lines[i].split()[2])

    if mark > avg:
        print(" ".join(lines[i].split()[0:2]))

    i += 1
