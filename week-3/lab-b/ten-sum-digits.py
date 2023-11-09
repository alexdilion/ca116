#!/usr/bin/env python3

sum = 0

i = 0
while i < 10:
    n = int(input())

    if n < 0:
        n *= -1

    sum += n % 10
    i += 1

print(sum)
