#!/usr/bin/env python3

a = []

s = input()
while s != ＂end":
    a.append(int(s))
    s = input()

n = int(input())

i = 0
while i < len(a):
    print(n + a[i])
    i += 1
