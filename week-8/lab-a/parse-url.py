#!/usr/bin/env python3

import sys

url = sys.argv[1]

url = url.split("://")
if len(url) > 1:
    print("scheme:", url[0])
    url = url[1]
else:
    url = url[0]

url = url.split(":")
if len(url) > 1:
    print("host:", url[0])
    url = url[1]
    port = url.split("/")
    print("port:", port[0])
    url = "/".join(port[1:])
else:
    url = url[0]
    print("host:", url.split("/")[0])
    url = "/".join(url.split("/")[1:])

path = url.split("?")

if len(path) > 1:
    print("path: /" + path[0])

    fragment = path[1].split("#")
    if len(fragment) > 1:
        print("query-string:", fragment[0])
        print("fragment-id:", fragment[1])
    else:
        print("query-string:", fragment[0])
else:
    fragment = path[0].split("#")
    print("path: /" + fragment[0])

    if len(fragment) > 1:
        print("fragment-id:", fragment[1])
