#!/usr/bin/env python3

if __name__ == "__main__":
    a = ["", "", "dog", "", "", "cat", "", "", "", "mouse"]
    a = []

i = 0
while i < len(a) and a[i] == "":
    i += 1

if i < len(a):
    print(a[i])
