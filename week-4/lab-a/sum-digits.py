#!/usr/bin/env python3

s = input()
i = 0
sum = 0

while i < len(s):
    sum += int(s[i])
    i += 1

print(sum)
