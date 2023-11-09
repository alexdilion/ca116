#!/usr/bin/env python3

s = input()
i = 0
ns = ""

while i < len(s):
    if s[i] != " ":
        ns += s[i]
    i += 1

print(ns)
