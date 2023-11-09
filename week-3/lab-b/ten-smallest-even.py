#!/usr/bin/env python3

i = 0
smallest_even = 219830921382148

while i < 10:
    n = int(input())

    if n % 2 == 0 and n < smallest_even:
        smallest_even = n

    i += 1

print(smallest_even)
