#!/usr/bin/env python3

home_score = int(input())
away_score = int(input())

if home_score > away_score:
    print("Home win.")
elif home_score < away_score:
    print("Away win.")
else:
    print("Draw.")
