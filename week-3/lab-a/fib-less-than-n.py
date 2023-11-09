#!/usr/bin/env python3

i = 0
n = int(input())
x, y = 0, 1

while i < n:
    print(x)
    x, y = y, x + y
    i = x
