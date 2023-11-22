#!/usr/bin/env python3

import sys

points = sys.stdin.readlines()

lines = []
i = 0
while i < 20:
    lines.append([" "] * 20)
    i += 1

i = 0
while i < len(points):
    xy = points[i].split()
    lines[int(xy[1])][int(xy[0])] = "*"

    i += 1

print(" " + "-" * 20)
i = 0
while i < len(lines):
    print("|" + "".join(lines[len(lines) - i - 1]) + "|")
    i += 1

print(" " + "-" * 20)
