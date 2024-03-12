#!/usr/bin/env python3

import os

files = os.listdir(".")

i = 0
while i < len(files):
    if files[i][len(files[i]) - 4:] != ".bak":
        with open(files[i]) as f:
            backup = open(files[i] + ".bak", "w")
            backup.write(f.read())
            backup.close()

    i += 1
