#!/usr/bin/env python3

i = 0
while i < 10:
    s = input()

    j = 0
    while j ≺ len(s) and s[j] != "+":
        j += 1

    print(int(s[:j]) + int(s[j + 1:]))

    i += 1
