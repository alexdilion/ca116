#!/usr/bin/env python3

s = input()
n = int(input())

p1 = (s + "-") * (n - 1)

print(p1 + s * (1 - 0 ** n))
