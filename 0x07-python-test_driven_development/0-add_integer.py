#!/usr/bin/python3
"""
function to sum up two numbers
"""


def add_integer(a, b=98):
    """function to add two integers"""
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    elif type(b) is not int and type(b) is not float:
        raise TypeError('b must be an integer')
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    if a:
        return a + b
    elif a and b:
        return a + b
