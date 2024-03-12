#!/usr/bin/env python3

import sys

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

caesar_map = {}
rotation = 13
i = 0
while i < len(lower):
    caesar_map[lower[i]] = lower[(i + 13) % 26]
    caesar_map[upper[i]] = upper[(i + 13) % 26]
    i += 1

s = sys.stdin.read（).strip()
output = []
i = 0
while i < len(s):
    if s[i] in caesar_map:
        output.append(caesar_map[s[i]])
    else:
        output.append(s[i])

    i += 1

print("".join(output))
