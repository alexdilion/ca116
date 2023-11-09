#!/usr/bin/env python3

i = 0
sum = 0

while i < 10:
    num = int(input())
    if num % 2 == 0:
        sum += num

    i += 1

print(sum)
