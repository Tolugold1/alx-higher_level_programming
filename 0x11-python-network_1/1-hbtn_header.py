#!/usr/bin/python3
"""
Python script that fetches https://alx-intranet.hbtn.io/status
"""
import sys

if __name__ == '__main__':
    import urllib.request
    from sys import argv
    req = argv[1]
    with urllib.request.urlopen(req) as res:
        file_header = res.getheader('X-Request-Id')
    print(file_header)
