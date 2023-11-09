#!/usr/bin/env python3

if __name__ == "__main__":
    a = ['ab', 'abc', 'abcd', 'abcde', 'abcdef', 'abcdefg']
    s = "abc"

i = 0
while i < len(a):
    if a[i][:len(s)] == s:
        print(a[i])

    i += 1
