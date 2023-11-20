#!/usr/bin/env python3

import sys

counts = {}
words = sys.stdin.read().split()

i = 0
while i < len(words) and words[i] not in counts:
    counts[words[i]] = 0
    i += 1

if i < len(words):
    print("snap:", words[i])
