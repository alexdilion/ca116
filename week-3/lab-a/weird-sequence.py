#!/usr/bin/env python3

i = 0
n = int(input())
x = 0

while i < n:
    print(x)
    x = -x + (x % 2) * 2 - 1
    i += 1
