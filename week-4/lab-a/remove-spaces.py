#!/usr/bin/env python3

ns = ""

s = input()
i = 0
while i < len(s):
    if s[i] != " ":
        ns += s[i]
    i += 1

print(ns)
