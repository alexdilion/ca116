#!/usr/bin/env python3

a = []
s = input()

while s != "end":
    a.append(int(s))
    s = input()

i = 0

while i < len(a):
    smallest = i
    j = i

    while j < len(a):
        if a[j] < a[smallest]:
            smallest = j

        j += 1

    tmp = a[i]
    a[i] = a[smallest]
    a[smallest] = tmp

    i += 1

mid = len(a) // 2

if len(a) % 2 == 0:
    if a[mid] < a[mid - 1]:
        print(a[mid - 1])
    else:
        print(a[mid])
else:
    print(a[mid])
