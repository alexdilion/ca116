#!/usr/bin/env python3

# move input to lists a and b
a, b = [], []
s = input()
while s != "end":
    a.append(int(s))
    s = input()

s = input()
while s != "end":
    b.append(int(s))
    s = input()

i, j = 0, 0
while i < len(a) and j < len(b):
    if a[i] < b[j]:
        print(a[i])
        i += 1
    else:
        print(b[j])
        j += 1

if i < len(a):
    t = i
    while t < len(a):
        print(a[t])
        t += 1
elif j < len(b):
    t = j
    while t < len(b):
        print(b[t])
        t += 1
