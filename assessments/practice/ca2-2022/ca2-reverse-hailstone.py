#!/usr/bin/env python3

import sys

a = []
n = int(sys.argv[1])
i = 0
while i < 10:
    a.append(n)

    if n % 2 == 0:
        n //= 2
    else:
        n = 3 * n + 1

    i += 1

i = 0
while i < len(a):
    print(a[len(a) - i - 1])
    i += 1