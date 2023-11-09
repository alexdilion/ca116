#!/usr/bin/env python3

pos = 0
neg = 0

n = 5
i = 0
while i < n:
    m = int(input())

    if m < 0:
        neg += m
    else:
        pos += m

    i += 1

print(neg, pos)
