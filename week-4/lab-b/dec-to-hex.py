#!/usr/bin/env python3

digits = "0123456789abcdef"
h = ""

n = int(input())
while n > 0:
    h = digits[n % 16] + h
    n //= 16

print(h)
