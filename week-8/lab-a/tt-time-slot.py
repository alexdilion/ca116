#!/usr/bin/env python3

s = input()
while s != "end":
    tokens = s.split()
    new_start = tokens[1].lstrip("0") + ":00"
    end = str((int(tokens[1]) + int(tokens[2]) - 1) % 24) + ":50"

    new_line = " ".join([tokens[0], new_start, end] + tokens[3:])
    print(new_line)

    s = input()
