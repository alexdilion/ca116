#!/usr/bin/env python3

i = 0
n = int(input())
while i < n:
    if (i + 1) % 3 == 0 and (i + 1) % 5 == 0:
        print("fizz-buzz")
    elif (i + 1) % 3 == 0:
        print("fizz")
    elif (i + 1) % 5 == 0:
        print("buzz")
    else:
        print(i + 1)

    i += 1
