#!/usr/bin/python3
"""Function that returns True if the object is exactly an
instance of the specified class, otherwise false
"""


def inherits_from(obj, a_class):
    """test for class of obj"""
    return issubclass(type(obj), a_class) and type(obj) != a_class
