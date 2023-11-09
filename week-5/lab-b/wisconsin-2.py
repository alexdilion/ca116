#!/usr/bin/env python3

header = input()
s = input()
c = 0

while s != "end":
    i = 0

    while s[i] != ",":
        i += 1

    if s[i + 1:i + 3] == "WI":
        c += 1

    s = input()

print(c)
