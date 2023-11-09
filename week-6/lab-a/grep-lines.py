#!/usr/bin/env python3

import sys

p = sys.argv[1]
matches = []

s = input()
while s != "end":
    i = 0
    while i <= len(s) - len(p) and p != s[i:i + len(p)]:
        i += 1

    if i <= len(s) - len(p):
        matches.append(s)

    s = input()

i = 0
while i < len(matches):
    print(matches[i])
    i += 1
