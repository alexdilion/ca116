#!/usr/bin/env python3

f = [0] * 10
s = input()

while s != "end":
    f[int(s)] += 1
    s = input()

i = 0

while i < len(f):
    print(i, "*" * f[i])
    i += 1
