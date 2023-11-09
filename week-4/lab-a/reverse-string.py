#!/usr/bin/env python3

s = input()
rs = ""
i = 0

while i < len(s):
    rs += s[-(i + 1)]
    i += 1

print(rs)
