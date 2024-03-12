#!/usr/bin/env python3

import sys

n = int(sys.stdin.readline().rstrip())
points = sys.stdin.read().split("\n")
plot = [" "] * n

i = 0
while i < len(points):
    point = int(points[i])
    plot[point] = "*"
    i += 1

print("|" + "".join(plot) + "|")