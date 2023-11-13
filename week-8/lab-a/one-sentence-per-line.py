#!/usr/bin/env python3

s = ""
line = input()
while line != "end":
    s += line + " "
    line = input()

lines = " ".join(s.split()).split(".")

i = 0
while i < len(lines):
    if lines[i] != "":
        print(lines[i].lstrip() + ".")

    i += 1
