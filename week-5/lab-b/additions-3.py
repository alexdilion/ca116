#!/usr/bin/env python3

output = 0

i = 0
while output != 1000:
    s = input()

    j = 0
    while j < len(s) and s[j] != "+":
        j += 1

    output = int(s[:j]) + int(s[j + 1:])
    print(output)

    i += 1
