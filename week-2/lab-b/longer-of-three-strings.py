#!/usr/bin/env python3

s1 = input()
s2 = input()
s3 = input()

if len(s1) > len(s2) and len(s1) > len(s3):
    print(s1)
elif len(s2) > len(s3):
    print(s2)
else:
    print(s3)
