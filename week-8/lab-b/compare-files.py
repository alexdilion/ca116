#!/usr/bin/env python3

import sys

name_a = sys.argv[1]
name_b = sys.argv[2]

with open(name_a) as fa:
    sa = fa.read()
    with open(name_b) as fb:
        sb = fb.read()

        if len(sa) > len(sb):
            tmp = sa
            sa = sb
            sb = tmp

        i = 0
        while i < len(sa) and sa[i] == sb[i]:
            i += 1

        s = sa[:i]
        line = len(s.split("\n")) - 1
        col = i - len("\n".join(s.split("\n")[:line])) - 1

        if i < len(sb):
            print(line, col)
