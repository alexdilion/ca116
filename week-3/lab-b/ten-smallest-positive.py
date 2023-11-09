#!/usr/bin/env python3

smallest = int(input())

i = 1
while i < 10:
    n = int(input())

    if n > 0 and n < smallest:
        smallest = n

    i += 1

print(smallest)
