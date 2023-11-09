#!/usr/bin/env python3

i = 1
smallest = int(input())

while i < 10:
    n = int(input())

    if n < smallest:
        smallest = n

    i += 1

print(smallest)
