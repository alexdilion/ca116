#!/usr/bin/env python3

import sys

name_map = {"boys": {}, "girls": {}}

with open("boys.txt") as f:
    s = f.read().split()
    i = 0
    while i < len(s):
        name_map["boys"][s[i]] = 1
        i += 1

with open("girls.txt") as f:
    s = f.read().split()
    i = 0
    while i < len(s):
        name_map["girls"][s[i]] = 1
        i += 1

names = sys.stdin.read().split()
i = 0
while i < len(names):
    boy_name = names[i] in name_map["boys"]
    girl_name = names[i] in name_map["girls"]

    if boy_name and girl_name:
        print(names[i], "either")
    elif boy_name:
        print(names[i], "boy")
    elif girl_name:
        print(names[i], "girl")

    i += 1
