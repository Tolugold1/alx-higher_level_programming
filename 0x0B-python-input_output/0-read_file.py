#!/usr/bin/python3
"""function that reads a text file"""


def read_file(filename=""):
    """function that reads a text file(UTF8)"""
    with open(filename, 'r') as f:
        print(f.read(), end='')
