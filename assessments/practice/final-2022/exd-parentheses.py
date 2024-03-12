#!/usr/bin/env python3

import sys

line = sys.stdin.readline().strip()
while line != "":
    i = 0
    while i < len(line) and line[i] != "(":
        i += 1

    if i < len(line):
        j = i + 1
        while j < len(line) and line[j] != ")":
            j += 1

        if j < len(line):
            print(line[i + 1:j])

    line = sys.stdin.readline().strip()
