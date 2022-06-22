#!/usr/bin/python3
"""class Square that defines a square by: (based on 3-square.py)"""


class Square:
    """class Square that defines a square"""
    def __init__(self, size=0):
        """initialize size"""
        self.__size = size

    @property
    def size(self):
        """return size"""
        return self.__size

    @size.setter
    def size(self, value):
        """test size if it meet some requirement"""
        if type(value) is int:
            self.__size = value
        else:
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """compute square of size"""
        return self.__size ** 2
