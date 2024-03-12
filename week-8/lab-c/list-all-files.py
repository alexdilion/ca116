#!/usr/bin/env python3

import os

dirs = ["."]
while len(dirs) > 0:
    curr_dir = dirs[0]
    files = os.listdir(curr_dir)

    i = 0
    while i < len(files):
        f_path = curr_dir + "/" + files[i]

        if os.path.isfile(f_path):
            print(f_path)
        else:
            dirs.append(f_path)

        i += 1

    dirs = dirs[1:]
