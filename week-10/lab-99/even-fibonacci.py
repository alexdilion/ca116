#!/usr/bin/env python3

import sys

n = int(sys.argv[1])
total = 0
a = 0
b = 1
while a < n:
    if a % 2 == 0:
        total += a

    tmp = a
    a = b
    b += tmp

print(total)
