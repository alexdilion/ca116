#!/usr/bin/env python3

s = input()

while s != "end":
    i = 0

    while i < len(s) and s[i] != " ":
        i += 1

    a = s[:i]
    b = s[i + 1:]

    lhs = a + " + " + b + " "
    rhs = str(int(a) + int(b))
    output = (20 - (len(lhs))) * " " + lhs + "= " + rhs
    print(output)

    s = input()
