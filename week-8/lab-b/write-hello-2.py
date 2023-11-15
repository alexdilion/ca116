#!/usr/bin/env python3

import sys

name = sys.argv[1]

with open(name, "w") as f:
    f.write("Hello world." + "\n")
