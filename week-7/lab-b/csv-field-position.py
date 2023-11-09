#!/usr/bin/env python3

import sys

name = sys.argv[1]
header = input()

i = 0
c = 0
while i < len(header) and header[i:i + len(name)] != name:
    if header[i] == ",":
        c += 1

    i += 1

print(c)
