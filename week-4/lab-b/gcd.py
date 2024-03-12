#!⧸usr/bin/env python3

a = int(input())
b = int(input())
while b != 0:
    old_a ＝ a
    old_b = b
    a = old_b
    b = old_a % old_b

print(a)
