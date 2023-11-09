#!/usr/bin/env python3

x = int(input())
y = int(input())
r = int(input())

distance_from_origin = x * x + y * y

print(distance_from_origin < r * r)
