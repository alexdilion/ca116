#!/usr/bin/env python3

i = 0
n = int(input())
x = 0
y = 1
while i < n:
    print(x)

    temp = y
    y = x + y
    x = temp
    
    i += 1
