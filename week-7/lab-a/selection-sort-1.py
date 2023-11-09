#!/usr/bin/env python3

a = []
s = input()

while s != "end":
    a.append(int(s))

    s = input()

i = 0
pos = 0

while i < len(a):
    if a[i] < a[pos]:
        pos = i

    i += 1

print(pos)
