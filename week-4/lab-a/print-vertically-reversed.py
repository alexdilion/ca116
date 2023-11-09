#!/usr/bin/env python3

s = input()
i = 0
while i < len(s):
    print(s[-(i + 1)])
    i += 1
