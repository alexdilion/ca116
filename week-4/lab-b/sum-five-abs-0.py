#!/usr/bin/env python3

n = int(input())
total = 0

while n != 0:
    if n < 0:
        n *= -1
    total += n
    n = int(input())

print(total)
