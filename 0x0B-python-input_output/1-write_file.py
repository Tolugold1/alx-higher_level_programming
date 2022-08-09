#!/usr/bin/python3
"""function that writes a text file"""


def write_file(filename="", text=""):
    """function that write a text file(UTF8)"""
    with open(filename, 'w') as f:
        no_of_char = f.write(text)
    return no_of_char
