#!/usr/bin/python3
class Square:
    """class Square that defines a square by: (based on 1-square.py)"""
    def __init__(self, size=0):
        """Private instance attribute: size"""
        if isinstance(size, int) == 0:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
