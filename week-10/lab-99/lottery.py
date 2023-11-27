#!/usr/bin/env python3

import sys

args = sys.argv[1:]
draw = {}
i = 0
while i < len(args):
    if args[i] not in draw:
        draw[args[i]] = 0

    draw[args[i]] += 1
    i += 1

ticket = sys.stdin.readline().strip()
while ticket != "":
    balls = ticket.split()
    matching = 0
    i = 0
    while i < len(balls):
        if balls[i] in draw:
            matching += 1
        i += 1

    if matching == 3:
        print(100)
    elif matching == 2:
        print(5)
    elif matching == 1:
        print(1)
    else:
        print(0)

    ticket = sys.stdin.readline().strip()
