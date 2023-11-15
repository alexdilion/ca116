#!/usr/bin/env python3

import os

files = os.listdir(".")

i = 0
while i < len(files):
    with open(files[i]) as f:
        if f.read(1) != "" and files[i][len(files[i]) - 3:] == ".py":
            print(files[i])

    i += 1
