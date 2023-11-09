#!/usr/bin/env python3

s1 = int(input())
s2 = int(input())
s3 = int(input())

p1 = (s1 == s2 and s1 != s3) or (s1 == s3 and s1 != s2)
p2 = (s2 == s3 and s1 != s3) or (s1 == s2 == s3)

print(p1 or p2)
