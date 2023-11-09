#!/usr/bin/env python3

n = input()
i = 0
prefix = ""

if n[0] == "-":
    prefix = n[0]
    n = n[1:]

while i < len(n) and n[i] != ".":
    i += 1

if i < len(n):
    if i == 0:
        print(prefix + "0" + n)
    elif i == len(n) - 1:
        print(prefix + n + "0")
    else:
        print(prefix + n)
else:
    print(prefix + n + ".0")
