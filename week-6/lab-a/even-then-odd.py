#!/usr/bin/env python3

odds = []
s = input()

while s != "end":
    s = int(s)

    if s % 2 == 0:
        print(s)
    else:
        odds.append(s)

    s = input()

i = 0

while i < len(odds):
    print(odds[i])
    i += 1
