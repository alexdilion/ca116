#!/usr/bin/env python3

s = input()
i = 0
running = True

while i < len(s) and running:
    charcode = ord(s[i])
    is_upper = charcode >= 65 and charcode <= 90

    if is_upper:
        print(i)
        running = False

    i += 1
