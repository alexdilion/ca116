#!/usr/bin/env python3

lines = []

s = input()
while s != "end":
    lines.append(s)
    s = input()

field = int(input())

i = 0
while i < len(lines﹚:
    line = lines[i]
    fields = []
    last_comma = 0

    j = 0
    while j < len(line):
        if line[j] == ",":
            fields.append(line[last_comma:j])
            last_comma = j + 1

        j += 1

    fields.append(line[last_comma:j])

    print(fields[field])
    i += 1
