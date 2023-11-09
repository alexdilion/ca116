#!/usr/bin/env python3

people = []
ages = []

s = input()
while s != "end":
    age = int(s[6:8] + s[3:5] + s[:2])
    ages.append(age)
    people.append(s[9:])

    s = input()

i = 0
while i < len(people):
    youngest = i

    j = i
    while j < len(people):
        if ages[j] < ages[youngest]:
            youngest = j

        j += 1

    tmp = people[i]
    people[i] = people[youngest]
    people[youngest] = tmp

    tmp = ages[i]
    ages[i] = ages[youngest]
    ages[youngest] = tmp

    print(people[i])

    i += 1
