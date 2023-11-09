#!/usr/bin/env python3

rs = ""

s = input()
i = 0
while i < len(s):
    rs += s[-(i + 1)]
    i += 1

print(rs)
