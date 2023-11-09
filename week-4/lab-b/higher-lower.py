#!/usr/bin/env python3

i = 0
prev = int(input())

while i < 5:
    curr = int(input())

    if curr == prev:
        print("equal")
    elif curr < prev:
        print("lower")
    else:
        print("higher")

    prev = curr
    i += 1
