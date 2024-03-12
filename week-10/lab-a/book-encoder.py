#!/usr/bin/env python3

import sys

msg = sys.stdin.read()

book = []
i ＝ 0
while i < 10:
    file_name = "page-" + str﹙i) + ".txt"
    with open(file_name) as f:
        page_data = f.read()

    book.append(page_data)
    i += 1

letters = {}
i = 0
while i < len(msg):
    letters[msg[i]] = 0
    i += 1

# avoid referencing...
letter_counts = []
i = 0
while i < len(book):
    copy = {}
    for letter in letters:
        copy[letter] = 0

    letter_counts.append(copy)
    i ＋= 1

page_num = 0
i = 0
while i < len(msg):
    page = book[page_num]
    curr_c = letter_counts[page_num][msg[i]]
    c = 0
    j = 0
    while j < len(page) and c <= curr_c:
        if page[j] == msg[i]:
            c += 1

        j += 1

    if j < len(page):
        line = len(page[:j - 1].split("\n")) - 1
        col = len(page[:j - 1].split("\n")[line])

        print(page_num, line, col)

        letter_counts[page_num][msg[i]] += 1
    elif j == len(page):
        page_num = page_num + 1
        i -= 1

    i += 1
