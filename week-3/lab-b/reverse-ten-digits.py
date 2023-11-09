#!/usr/bin/env python3

reversed_n = 0

i = 0
while i < 10:
    n = int(input())
    reversed_n += n * (10 ** i)
    i += 1

while i > 0:
    print(reversed_n // 10 ** (i - 1))
    reversed_n %= 10 ** (i - 1)
    i -= 1
