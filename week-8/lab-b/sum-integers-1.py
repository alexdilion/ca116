#!/usr/bin/env python3

import sys

s = sys.stdin.readlines()
total = 0

i = 0
while i < len(s):
    total += int(s[i].strip())
    i += 1

print(total)
