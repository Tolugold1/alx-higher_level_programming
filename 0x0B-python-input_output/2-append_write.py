#!/usr/bin/python3
"""function that appends a text file"""


def append_write(filename="", text=""):
    """function that append a text file(UTF8)"""
    with open(filename, 'a') as f:
        no_of_char = f.write(text)
    return no_of_char
