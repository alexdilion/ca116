#!/usr/bin/env python3

import sys

opb = {"{": 1, "(": 1, "[": 1}
clb = {"}": 1, "]": 1, ")": 1}
valid_pairs = {"{}": 1, "[]": 1, "()": 1}

lines = sys.stdin.read().split("\n")
i = 0
while i < len(lines):
    line = lines[i]
    error = ""
    checked_clb = {}
    stack = []
    j = 0
    while j < len(line) and error == "":
        char = line[j]
        if char in opb:
            stack.append([char, j])
        elif char in clb and str(j) not in checked_clb:
            if len(stack) == 0:
                error = str(i) + " " + str(j)
            else:
                stack_item = stack.pop()
                pair = stack_item[0] + char
                if pair not in valid_pairs:
                    error = str(i) + " " + str(stack_item[1])

                checked_clb[str(j)] = 1

        j += 1

    if error:
        print(error)
    elif stack:
        print(str(i) + " " + str(stack[len(stack) - 1][1]))

    i += 1
