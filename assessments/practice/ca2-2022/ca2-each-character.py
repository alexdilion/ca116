#!/usr/bin/env python3

import sys

s = sys.stdin.read()
i = 0
while i < len(s):
    if s[i] == "\n":
        print()
    else:
        print(s[i])

    i += 1