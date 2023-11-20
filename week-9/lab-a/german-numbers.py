#!/usr/bin/env python3

import sys

english = "one two three four five six seven eight nine ten".split()
german = "eins zwei drei vier funf sechs sieben acht neun zehn".split()

translation = {}
i = 0
while i < len(english):
    translation[english[i]] = german[i]
    i += 1

words = sys.stdin.read().split()
i = 0
while i < len(words):
    print(translation[words[i]])
    i += 1
