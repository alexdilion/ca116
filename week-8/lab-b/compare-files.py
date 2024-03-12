#!/usr/bin/env python3

import sys

f1 = sys.argv[1]
f2 = sys.argv[2]

with open(f1) as f:
    data_a = f.read()

with open(f2) as f:
    data_b = f.read()

i = 0
while i < len(data_a) and i < len(data_b) and data_a[i] == data_b[i]:
    i += 1
    
if i < len(data_a) or i < len(data_b):
    equal = data_a[:i]
    line = len(equal.split("\n")) - 1
    column = len(equal.split("\n")[line])
    
    print(line, column)
