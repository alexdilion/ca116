#!/usr/bin/env python3

import sys

opb = {"{": "}", "[": "]", "(": ")"}
clb = {"}": "{", "]": "[", ")": "("}

lines = sys.stdin.readlines()
i = 0
while i < len(lines):
    line = lines[i]
    opening = [] # index of each opening bracket
    closing = [] # index of each closing bracket

    j = 0
    while j < len(line):
        if line[j] in opb:
            opening.append(j)
        elif line[j] in clb:
            closing.append(j)

        j += 1

    n_op = len(opening)
    n_cl = len(closing)
    
    # if n_op > n_cl:
        # start from inner-most open bracket
        # loop from current bracket to next closing bracket
        # if closing bracket matches the current bracket then it is valid, move on
        # if closing bracket does not match, then closing bracket is error col
        # if we fall off the end of the line then current bracket is the error col
    for j, br in enumerate(closing):
        print(j, br)

    i += 1