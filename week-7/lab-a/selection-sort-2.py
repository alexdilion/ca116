#!/usr/bin/env python3

a = []

s = input()
while s != "end":
    a.append(int(s))
    s = input()


i = int(input())
pos = i
while i < len(a):
    if a[i] < a[pos]:
        pos = i

    i += 1

print(pos)
