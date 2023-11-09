#!/usr/bin/env python3

a = int(input())

b = input()
length_b = len(b)
b = int(b)

c = int(input())

num = a * (10 ** length_b) + b
p1 = ((num // 10 ** length_b) * (1 - (c % 2)))
p2 = ((num % 10 ** length_b) * (c % 2))

print(p1 + p2)
