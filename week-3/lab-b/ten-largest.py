#!/usr/bin/env python3

i = 1
largest = int(input())

while i < 10:
    n = int(input())

    if n > largest:
        largest = n

    i += 1

print(largest)
