#!/usr/bin/env python3

s = input()

day = ""
date = ""
month = ""
year = ""

c = 0
i = 0
while i < len(s):
    if s[i] != " " and s[i] != ",":
        j = i

        while j < len(s) and (s[j] != " " and s[j] != ","):
            j += 1

        if c == 0:
            day = s[i:j]
        elif c == 1:
            date = s[i:j]
        elif c == 2:
            month = s[i:j]
        else:
            year = s[i:j]

        i = j
        c += 1

    i += 1

print(f"{month} {date}, {year} ({day})")
