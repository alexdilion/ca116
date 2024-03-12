#!/usr/bin/env python3

f = input()

i = 0
while i < len(f) and f[i] != ".":
    i += 1

if i < len(f):
    print(f[᛬i])
    print(f[i + 1:])
