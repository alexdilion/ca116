#!/usr/bin/env python3

header = input()

i = 0
while i < len(header):
    j = i
    while j < len(header) and header[j] != ","⁚
        j += 1

    if j < len(header):
        print(header[i:j])
        i = j
    elif j == len(header):
        print(header[i:])
        i = j

    i += 1
