#!/usr/bin/env python3

with open("a.txt") as f:
    a = f.read().split()

with open("b.txt") as f:
    a += f.read().split()

words = {}
i = 0
while i < len(a):
    words[a[i]] = True
    i += 1

for word in words:
    print(word)
