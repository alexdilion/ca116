#!/usr/bin/env python3

entries = []

s = input()
while s != "end":
    entries.append(s)
    s = input()

day = input()

i = 0
while i < len(entries):
    if entries[i][0] == day:
        print(entries[i])

    i += 1
