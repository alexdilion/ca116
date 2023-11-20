#!/usr/bin/env python3

import sys

f = "apple pear orange banana cherry".split()
fruits = {}

i = 0
while i < len(f):
    fruits[f[i]] = True
    i += 1

a = sys.stdin.read().split()

i = 0
while i < len(a):
    if a[i] in fruits:
        print(a[i])

    i += 1
