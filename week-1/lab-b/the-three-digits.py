#!/usr/bin/env python3

n = int(input())
ones = n % 10
tens = n // 10 % 10
hundreds = n // 100

print(hundreds)
print(tens)
print(ones)
