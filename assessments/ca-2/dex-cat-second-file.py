#!/usr/bin/env python3

import sys

f1 = sys.argv[1]

with open(f1) as f:
    f2 = f.read().rstrip()

with open(f2) as f:
    print(f.read().rstrip())
