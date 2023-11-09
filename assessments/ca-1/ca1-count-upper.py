#!/usr/bin/env python3

s = input()
c = 0
i = 0
while i < len(s):
    if s[i] >= "A" and s[i] <= "Z":
        c += 1

    i += 1

print(c)
