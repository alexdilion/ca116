#!/usr/bin/env python3

import sys

f_name = sys.argv[1]
words = sys.argv[2:]

with open(f_name, "w") as f:
    i = 0
    while i < len(words):
        f.write(words[i] + "\n＂)
        i += 1
