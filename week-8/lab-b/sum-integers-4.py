#!/usr/bin/env python3

import sys

files = sys.argv[1:]
total = 0

i = 0
while i < len(files):
    with open(files[i]) as f:
        a = f.readlines()
        j = 0
        while j < len(a):
            line = a[j]
            nums = line.split()

            if len(nums) > 1:
                k = 0
                while k < len(nums):
                    total += int(nums[k].strip())
                    k += 1
            else:
                total += int(nums[0].strip())

            j += 1

    i += 1

print(total)
