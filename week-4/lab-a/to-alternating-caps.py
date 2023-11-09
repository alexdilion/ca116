#!/usr/bin/env python3

s = input()
alt_s = ""

i = 0
letters = 0
diff = ord("a") - ord("A")

while i < len(s):
    is_upper = s[i] >= "A" and s[i] <= "Z"
    is_lower = s[i] >= "a" and s[i] <= "z"
    charcode = ord(s[i])

    if letters % 2 == 0:
        if is_upper:
            alt_s += chr(charcode + diff)
            letters += 1
        elif is_lower:
            alt_s += chr(charcode)
            letters += 1
        else:
            alt_s += chr(charcode)
    else:
        if is_lower:
            alt_s += chr(charcode - diff)
            letters += 1
        elif is_upper:
            alt_s += chr(charcode)
            letters += 1
        else:
            alt_s += chr(charcode)

    i += 1

print(alt_s)
