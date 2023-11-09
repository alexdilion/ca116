#!/usr/bin/env python3

sum = 0

s = input()
i = 0
while i < len(s):
    sum += int(s[i])
    i += 1

print(sum)
