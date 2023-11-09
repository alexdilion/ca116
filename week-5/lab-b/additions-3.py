#!/usr/bin/env python3

i = 0
output = 0

while output != 1000:
    j = 0
    s = input()

    while j < len(s) and s[j] != "+":
        j += 1

    output = int(s[:j]) + int(s[j + 1:])
    print(output)

    i += 1
