#!/usr/bin/env python3

a = []

s = input()
while s != "end":
    a.append(int(s))
    s = input()

i = 0
while i < len(a):
    largest = i

    j = i
    while j < len(a):
        if a[j] > a[largest]:
            largest = j

        j += 1

    tmp = a[i]
    a[i] = a[largest]
    a[largest] = tmp

    print(a[i])

    i += 1
