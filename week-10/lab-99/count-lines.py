#!/usr/bin/env python3

import sys

s = sys.stdin.read().strip().split("\n")
lines = []
points = {}
i = 0
while i < len(s):
    x_coords = s[i].split()
    lines.append(x_coords)
    j = 0
    while j < len(x_coords):
        points[x_coords[j] + "-" + str(i)] = 1
        j += 1

    i += 1

total = 0
i = 0
while i < len(lines[1]):
    j = 0
    while j < len(lines[0]):
        offset = int(lines[1][i]) - int(lines[0][j])
        other_x = str(int(lines[1][i]) + offset) + "-2"
        if other_x in points:
            total += 1
        j += 1

    i += 1

print(total)
