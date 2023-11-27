#!/usr/bin/env python3

with open("characters.txt") as f:
    s = f.read()

i = 0
while i < len(s):
    if s[i] == "\n":
        print()
    else:
        print(s[i])

    i += 1
