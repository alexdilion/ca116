#!/usr/bin/env python3

import sys

arg = sys.argv[1]
header = input()

# Separate argument into field name and value

i = 0
while i < len(arg) and arg[i] != "=":
    i += 1

name = arg[:i]
value = arg[i + 1:]

# Find the position of the field that we're looking for

i = 0
pos = 0
while i < len(header) and header[i:i + len(name)] != name:
    if header[i] == ",":
        pos += 1

    i += 1

# Read all csv lines into a list

csv = []
csv_line = input()
while csv_line != "end":
    csv.append(csv_line)
    csv_line = input()

# Check every csv line for the value that we're looking for

line_index = 0
while line_index < len(csv):
    line = csv[line_index]

    i = 0
    prev = 0
    count = 0
    while i < len(line) and count <= pos:
        j = i
        while j < len(line) and line[j] != ",":
            j += 1

        count += 1
        prev = i
        i = j + 1

    if line[prev:i - 1] == value:
        print(line)

    line_index += 1
