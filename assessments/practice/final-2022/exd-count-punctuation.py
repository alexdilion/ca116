#!/usr/bin/env python3

import sys

a = ", . ? !".split()
i = 0
punctuation = {}
while i < len(a):
    punctuation[a[i]] = 1
    i += 1

s = sys.stdin.read()
c = 0
i = 0
while i < len(s):
    if s[i] in punctuation:
        c += 1
    
    i += 1

print(c)