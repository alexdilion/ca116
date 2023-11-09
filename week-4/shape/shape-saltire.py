#!/usr/bin/env python3

n = int(input())
i = 0
while i < n:
    dist = i - n // 2

    if dist < 0:
        dist = -dist

    if i == n // 2:
        print(" " * (n // 2) + "*")
    else:
        print(" " * (n // 2 - dist) + "*" + (dist * 2 - 1) * " " + "*")

    i += 1
