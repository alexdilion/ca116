#!/usr/bin/env python3

s = input()
i = 0

while i < len(s) and not (s[i] >= "0" and s[i] <= "9"):
    i += 1

if i < len(s):
    j = i

    while j < len(s) and (s[j] >= "0" and s[j] <= "9"):
        j += 1

    print(s[i:j], i)
