#!/usr/bin/env python3

import sys

opb = {"{": "}", "(": ")", "[": "]"}
clb = {"}": "{", "]": "[", ")": "("}
valid_pairs = {"{}": 1, "[]": 1, "()": 1}

lines = sys.stdin.read().split("\n")
i = 0
while i < len(lines):
    line = lines[i]
    errors = []
    stack = []
    j = 0
    while j < len(line):
        char = line[j]
        if char in opb:
            stack.append([char, j])
        elif char in clb:
            if len(stack) == 0:
                errors.append(str(i) + " " + str(j))
            else:
                stack_item = stack.pop()
                pair = stack_item[0] + char
                if pair not in valid_pairs:
                    errors.append(str(i) + " " + str(stack_item[1]))
                else:
                    line = line[:j] + "*" + line[j + 1:]

        j += 1

    if len(errors) > 0:
        print(errors[0])
    elif len(stack) > 0:
        print(str(i) + " " + str(stack[len(stack) - 1][1]))

    i += 1
