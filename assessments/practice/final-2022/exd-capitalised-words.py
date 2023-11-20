#!/usr/bin/env python3

import sys

a = sys.stdin.read().split()
i = 0
while i < len(a):
    if a[i][0] >= "A" and a[i][0] <= "Z":
        print(a[i])

    i += 1
