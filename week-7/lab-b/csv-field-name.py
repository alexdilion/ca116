#!/usr/bin/env python3

import sys

pos = int(sys.argv[1])
header = input()

i = 0
c = 0
p = 0
while i < len(header) and c <= pos:
    j = i
    while j < len(header) and header[j] != ",":
        j += 1

    c += 1
    p = i
    i = j + 1

print(header[p:i - 1])
