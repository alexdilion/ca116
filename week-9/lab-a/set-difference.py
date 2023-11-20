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

words_b = {}
i = 0
while i < len(b):
    words_b[b[i]] = True
    i += 1

for word in words_a:
    if word not in words_b:
        print(word)
