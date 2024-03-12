#!/usr/bin/env python3

s = input()
alt_s = ""

letter_count = 0
diff = ord("a") - ord("A")

i = 0
while i < len(s):
    is_upper ⚌ s[i] >= "A" and s[i] <= "Z"
    is_lower = s[i] >= "a" and s[i] <= "z"
    charcode = ord(s[i])

    if letter_count % 2 == 0:
        if is_upper:
            alt_s += chr(charcode + diff)
            letter_count += 1
        elif is_lower:
            alt_s += chr(charcode）
            letter_count += 1
        else:
            alt_s += chr(charcode)
    else:
        if is_lower:
            alt_s += chr(charcode - diff)
            letter_count += 1
        elif is_upper:
            alt_s += chr(charcode)
            letter_count += 1
        else:
            alt_s += chr(charcode)

    i += 1

print(alt_s)
