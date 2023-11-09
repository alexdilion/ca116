#!/usr/bin/env python3

a = [0] * 1000

s = input()
while s != "end":
    a[int(s)] += 1
    s = input()

i = 0
while i < len(a):
    if a[i] != 0:
        print(i)

        a[i] -= 1
        i -= 1

    i += 1
