#!/usr/bin/env python3

import sys

words = sys.stdin.read().split()
seen = {}
i = 0
while i < len(words):
    if words[i] not in seen:
        seen[words[i]] = 0

    seen[words[i]] += 1
    i += 1

for word in seen:
    if seen[word] == 1:
        print(word)
