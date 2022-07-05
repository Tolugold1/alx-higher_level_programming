#!/usr/bin/python3
def read_file(filename=""):
    """function that reads a text file(UTF8)"""
    with open(filename, 'r') as f:
        print(f.read(), end='')
