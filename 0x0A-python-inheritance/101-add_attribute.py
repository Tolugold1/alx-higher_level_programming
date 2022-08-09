#!/usr/bin/python3
"""
This is the add attribute module.
The add attribute module has one function, add_attribute().
"""


def add_attribute(self, attribute, value):
    """Add attribute if it's possible."""
    if hasattr(self, '__dict__'):
        setattr(self, attribute, value)
    else:
        raise TypeError("can't add new attribute")
