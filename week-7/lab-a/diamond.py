#!/usr/bin/env python3

import sys

size = int(sys.argv[1])

i = 0
while i < size:
    c = i - size // 2

    if c < 0:
        c = -c

    print(" " * c + "*" * (size - c * 2))
    i += 1
