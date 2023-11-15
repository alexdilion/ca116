#!/usr/bin/env python3

import os

with open("start.txt") as start:
    content = start.read().rstrip()
    while os.path.isfile(content):
        f = open(content)
        content = f.read().rstrip()
        f.close()

    print(content.rstrip())
