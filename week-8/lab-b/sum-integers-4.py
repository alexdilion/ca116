#!/usr/bin/env python3

import sys

files = sys.argv[1:]
total = 0
s = ""

i = 0
while i < len(files):
    with open(files[i]) as f:
        s += " " + f.read()

    i += 1

s = s.split()
i = 0
while i < len(s):
    total += int(s[i])
    i += 1

print(total)
