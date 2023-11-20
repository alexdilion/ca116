#!/usr/bin/env python3

import sys

args = sys.argv[1:]

with open(args[0]) as f:
    f1 = f.read()

with open(args[1]) as f:
    f2 = f.read()

tmp = f1
with open(args[0], "w") as f:
    f.write(f2)

with open(args[1], "w") as f:
    f.write(tmp)
