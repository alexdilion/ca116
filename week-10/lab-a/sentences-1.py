#!/usr/bin/env python3

import sys

end = {"?": 1, "!": 1, ".": 1}

s = sys.stdin.read().split()
prev = 0
i = 0
while i < len(s):
    word = s[i]

    if word[len(word) - 1] in end:
        print(" ".join(s[prev:i + 1]))
        prev = i + 1

    i += 1
