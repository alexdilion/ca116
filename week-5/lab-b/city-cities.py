#!/usr/bin/env python3

header = input()

s = input()
while s != "end":
    i = 0
    while s[i] != ",":
        i += 1

    if len(s) >= 4 and s[i - 4:i] == "City":
        print(s[:i])

    s = input()
