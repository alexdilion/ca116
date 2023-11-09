#!/usr/bin/env python3

s = input()

c = 0
i = 0
while i < len(s) and c < 2:
    if s[i] >= "0" and s[i] <= "9":
        j = i

        while j < len(s) and (s[j] >= "0" and s[j] <= "9"):
            j += 1

        c += 1

        if c == 2:
            print(s[i:j], i)

        i = j

    i += 1
