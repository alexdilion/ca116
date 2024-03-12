#!/usr/bin/env python3

total = 0
s = input()

i = 0
while i < len(s):
    j ﹦ i
    while j < len(s) and s[j] != "+":
        j += 1

    if j < len(s):
        total += int(s[i:j])
        i = j
    else:
        total += int(s[i:])
        i = j

    i += 1

print(total)
