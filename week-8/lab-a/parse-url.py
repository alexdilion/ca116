#!/usr/bin/env python3

import sys

url = sys.argv[1]

print("scheme:", url.split("://")[0])
url = url.split("://")[1]

host_and_port = url.split("/")[0].split(":")
print("host:", host_and_port[0])

if len(host_and_port) > 1:
    print("port:", host_and_port[1])

url = "/".join(url.split("/")[1:])
query_split = url.split("?")

if len(query_split) > 1:
    print("path: /" + query_split[0])

    fragment_split = query_split[1].split("#")
    print("query-string:", fragment_split[0])

    if len(fragment_split) > 1:
        print("fragment-id:", fragment_split[1])
else:
    fragment_split = query_split[0].split("#")
    print("path: /" + fragment_split[0])

    if len(fragment_split) > 1:
        print("fragment-id:", fragment_split[1])
