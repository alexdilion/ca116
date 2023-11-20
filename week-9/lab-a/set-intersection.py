#!/usr/bin/env python3

with open("a.txt") as f:
    a = f.read().split()

with open("b.txt") as f:
    b = f.read().split()

words_a = {}
i = 0
while i < len(a):
    words_a[a[i]] = True
    i += 1

i = 0
while i < len(b):
    if b[i] in words_a:
        print(b[i])

    i += 1
