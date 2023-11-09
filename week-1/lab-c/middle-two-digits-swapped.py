#!/usr/bin/env python3

n = (int(input()) % 10000) // 100
tens = n // 10
ones = n % 10

print(ones * 10 + tens)
