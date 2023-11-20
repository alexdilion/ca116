#!/usr/bin/env python3

import sys

line = sys.stdin.readline().strip()
while line != "":
    tokens = line.split()

    if int(tokens[2]) >= 40:
        print(" ".join(tokens[:2]))

    line = sys.stdin.readline().strip()
