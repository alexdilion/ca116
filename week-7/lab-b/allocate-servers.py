#!/usr/bin/env python3

minimum = 0
jobs = []

s = input()
while s != "end":
    jobs.append(int(s))
    s = input()

i = 0
while i < len(jobs) - 1:
    c = 1

    j = i + 1
    while j < len(jobs) and jobs[j] - jobs[i] <= 1000:
        c += 1
        j += 1

    if c > minimum:
        minimum = c

    i += 1

print(minimum)
