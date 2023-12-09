#!/usr/bin/env python3

import sys

args = sys.argv[1:]
redacted = {}
i = 0
while i < len(args):
    redacted[args[i]] = 1
    i += 1

word = sys.stdin.readline().strip()
while word != "":
    if word in redacted:
        print("*" * len(word))
    else:
        print(word)

    word = sys.stdin.readline().strip()
