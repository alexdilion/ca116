#!/usr/bin/env python3

import sys

nums = sys.stdin.read().split()
counts = [0] * 20

i = 0
while i < len(nums):
    counts[int(nums[i])] += 1
    i += 1

height = counts[0]
i = 0
while i < len(counts):
    if counts[i] > height:
        height = counts[i]

    i += 1

i = 0
while i < height:
    s = " |"
    j = 0
    while j < len(counts):
        if counts[j] >= height - i:
            s += "*"
        else:
            s += " "

        j += 1    

    print(s)
    i += 1

print(" " + "-" * 23)