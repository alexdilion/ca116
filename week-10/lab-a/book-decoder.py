#!/usr/bin/env python3

import sys

book = []
i = 0
while i < 10:
    file_name = "page-" + str(i) + ".txt"
    with open(file_name) as f:
        page_data = f.readlines()

    book.append(page_data)
    i += 1

msg = []
encoding = sys.stdin.readline()
while encoding != "":
    data = encoding.split()
    page = int(data[0])
    line = int(data[1])
    col = int(data[2])

    msg.append(book[page][line][col])
    encoding = sys.stdin.readline()

print("".join(msg).rstrip())
