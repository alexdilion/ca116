#!/usr/bin/env python3

n = int(input())
h = ""
digits = "0123456789abcdef"

while n > 0:
    h = digits[n % 16] + h
    n //= 16

print(h)
