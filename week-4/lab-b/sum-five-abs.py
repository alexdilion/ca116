#!/usr/bin/env python3

total = 0

n = 5
i = 0
while i < n:
    m = int(input())

    if m < 0:
        m *= -1

    total += m
    i += 1

print(total)
