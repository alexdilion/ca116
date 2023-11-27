#!/usr/bin/env python3

import sys

points = sys.stdin.readlines()
n = 20

lines = []
i = 0
while i < n:
    lines.append([" "] * n)
    i += 1

i = 0
while i < len(points):
    xy = points[i].split()
    lines[int(xy[1])][int(xy[0])] = "*"
    i += 1

print(" " + "-" * n)

i = 0
while i < len(lines):
    print("|" + "".join(lines[len(lines) - i - 1]) + "|")
    i += 1

print(" " + "-" * n)
