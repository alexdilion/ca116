#!/usr/bin/env python3

n = int(input())

pos = 0
neg = 0

while n != 0:
    if n < 0:
        neg += n
    else:
        pos += n

    n = int(input())

print(neg, pos)
