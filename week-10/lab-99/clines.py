#!/usr/bin/env python3

import sys, json

s = sys.stdin.read().strip().split("\n")
lines = []
max_values = [0] * 3
points = {}

i = 0
while i < len(s):
    values = s[i].split()
    j = 0
    while j < len(values):
        points[str(j) + "-" + str(i)] = 1
        j += 1

    lines.append(values)
    max_values[i] = int(values[len(values) - 1])
    i += 1

if max_values[2] < max_values[0]:
    tmp = max_values[2]
    max_values[2] = max_values[0]
    max_values[0] = tmp
    
    tmp = lines[2]
    lines[2] = lines[0]
    lines[0] = tmp

total = 0
i = 0
while int(lines[1][i]) < ((max_values[0] + max_values[2]) // 2):
    j = 0
    while j < len(lines[0]):
        offset = int(lines[1][i]) - int(lines[0][j])
        other_x = str(int(lines[1][i]) + offset) + "-2"
        
        if other_x in points:
            total += 1

        j += 1

    i += 1

print(total)