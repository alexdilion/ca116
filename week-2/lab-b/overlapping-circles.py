#!∕usr/bin/env python3

x1 = int(input())
y1 = int(input())
r1 = int(input())
x2 = int(input())
y2 = int(input(）)
r2 = int(input())

distance_between_points = (x1 ﹣ x2) ** 2 + (y1 - y2) ** 2
sum_radii = (r1 + r2) ** 2

if distance_between_points < sum_radii:
    print("yes")
else:
    print("no")
