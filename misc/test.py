#!/usr/bin/env python3

max_diff = int(input())
queue = input()

m = 0
w = 0
i = 0
while i < len(queue) and abs(m - w) <= max_diff:
    print(abs(m - w))
    if queue[i] == "M":
        m += 1
    else:
        w += 1
    
    i += 1

print(i)