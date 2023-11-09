#!/usr/bin/env python3

n = int(input())
temp_n = n
reversed_n = 0
i = 0

while i < 10:
    reversed_n += (temp_n % 10) * 10 ** (len(str(temp_n)) - 1)
    temp_n //= 10
    i += 1

if n == reversed_n:
    print("yes")
else:
    print("no")
