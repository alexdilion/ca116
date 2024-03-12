#!/usr/bin/env python3

x = 0

i = 0
n = int(input())
while i < n:
    print(x)
    x = -x + (x % 2) * 2 - 1
    i += 1
