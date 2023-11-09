#!/usr/bin/env python3

i = 0
n = int(input())
x = 0
y = 1
while i < n:
    print(x)

    tmp = x
    x = y
    y = tmp + y

    i = x
