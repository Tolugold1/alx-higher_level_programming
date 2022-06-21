#!/usr/bin/python3
"""class Square that defines a square by: (based on 2-square.py)"""


class Square:
    """class Square that defines a square"""
    
    def __init__(self, size=0):
        """test if size meet some requirement"""
        if isinstance(size, int) == 0:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """compute square of size"""
        return self.__size ** 2
