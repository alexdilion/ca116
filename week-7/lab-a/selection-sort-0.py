#!/usr/bin/env python3

a = []
s = input()

while s != "end":
    a.append(int(s))

    s = input()

i = 0
smallest = a[0]

while i < len(a):
    if a[i] < smallest:
        smallest = a[i]

    i += 1

print(smallest)
