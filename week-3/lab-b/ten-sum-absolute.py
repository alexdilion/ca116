#!/usr/bin/env python3

sum = 0

i = 0
while i < 10:
    n = int(input())

    if n < 0:
        sum += -n
    else:
        sum += n

    i += 1

print(sum)
