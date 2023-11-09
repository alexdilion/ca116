#!/usr/bin/env python3

i = 0
n = int(input())
m = int(input())

while i < n:
    print(m)

    if m % 2 == 0:
        m //= 2
    else:
        m = 3 * m + 1

    i += 1
