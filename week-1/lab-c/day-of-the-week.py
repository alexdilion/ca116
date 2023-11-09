#!/usr/bin/env python3

month = int(input())
date = int(input())
day_of_year = (month - 1) * 30 + date
day = ((day_of_year - 1) % 7) + 1

print(day)
