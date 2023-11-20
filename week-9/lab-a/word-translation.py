#!/usr/bin/env python3

import sys

translation = {}

with open("translation.txt") as f:
    line = f.readline()
    while line != "":
        words = line.split()
        translation[words[0]] = words[1]

        line = f.readline()

words = sys.stdin.read().split()
i = 0
while i < len(words):
    print(translation[words[i]])
    i += 1
