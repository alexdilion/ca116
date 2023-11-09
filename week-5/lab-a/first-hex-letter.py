#!/usr/bin/env python3

hex_digits = "0123456789abcdef"
h = ""

n = int(input())
while n > 0:
    h = hex_digits[n % 16] + h
    n //= 16

i = 0
while i < len(h) and not (h[i] >= "a" and h[i] <= "f"):
    i += 1

if i < len(h):
    print(h[i])
