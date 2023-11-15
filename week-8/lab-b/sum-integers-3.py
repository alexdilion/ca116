#!/usr/bin/env python3

import sys

total = 0
files = sys.argv[1:]

i = 0
while i < len(files):
    with open(files[i]) as f:
        a = f.readlines()

        j = 0
        while j < len(a):
            total += int(a[j].strip())
            j += 1

    i += 1

print(total)
