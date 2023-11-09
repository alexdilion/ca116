#!/usr/bin/env python3

s = input()
cap_s = ""

i = 0
while i < len(s):
    charcode = ord(s[i])
    if s[i] >= "a" and s[i] <= "z":
        cap_s += chr(charcode - (ord("a") - ord("A")))
    else:
        cap_s += s[i]

    i += 1

print(cap_s)
