#!/usr/bin/env python3

n = int(input())
a = 0
b = 1
while a < n:
    tmp = a
    a = b
    b += tmp

if a == n:
    print("yes")
else:
    print("no")