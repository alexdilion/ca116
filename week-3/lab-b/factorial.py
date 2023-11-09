#!/usr/bin/env python3

i = 0
n = int(input())
output = 1

while i < n:
    output *= i + 1
    i += 1

print(output)
