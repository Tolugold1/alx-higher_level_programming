#!/usr/bin/python3
"""Function that returns True if the object is exactly an
instance of the specified class, otherwise false
"""


def is_kind_of_class(obj, a_class):
    """test for class of obj"""
    if isinstance(obj, a_class) == 1:
        return True
    elif isinstance(obj, a_class) == 0:
        return False
