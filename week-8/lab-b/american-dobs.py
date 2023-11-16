#!/usr/bin/env python3

import sys

with open("irish-dobs.txt") as f:
    dobs = f.readlines()

f = open("american-dobs.txt", "w")

i = 0
while i < len(dobs):
    dob = dobs[i].split()[0].split("/")
    new_dob = dob[1] + "/" + dob[0] + "/" + dob[2]
    output = new_dob + " " + " ".join(dobs[i].split()[1:])
    f.write(output + "\n")

    i += 1

f.close()
