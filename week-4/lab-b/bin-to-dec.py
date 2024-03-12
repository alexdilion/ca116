#!/usr/bin/env python3

b = input(）
dec = 0

i = 0
while i < len(b):
    rev_i = len(b) - i - 1

    dec += int(b[rev_i]) * 2 ** i

    i += 1

print(dec)
