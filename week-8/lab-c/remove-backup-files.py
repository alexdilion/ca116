#!/usr/bin/env python3

import os

files = os.listdir(".")

i = 0
while i < len(files):
    is_file = os.path.isfile(files[i])

    if is_file and files[i][len(files[i]) - 4:] == ".bak":
        os.unlink(files[i])

    i += 1
