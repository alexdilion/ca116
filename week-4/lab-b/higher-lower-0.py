#!/usr/bin/env python3

prev = int(input())
while prev != 0:
    curr = int(input())

    if curr != 0:
        if curr == prev:
            print("equal")
        elif curr < prev:
            print("lower")
        else:
            print("higher")

    prev = curr
