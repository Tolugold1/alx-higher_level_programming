#!/usr/bin/python3
"""This is rectangle class that has a super class BaseGeometry"""


Rectangle = __import__("9-rectangle").Rectangle


"""class Square that inherits from Rectangle"""


class Square(Rectangle):
    """inherit from rectangle"""
    def __init__(self, size):
        """Using class Rectangle and BaseGeometry methods"""
        self.integer_validator("size", size)
        self.__size = size
        Rectangle.__init__(self, size, size)

    def __str__(self):
        """Return [Square] <width>/<height>"""
        return "[Square] {}/{}".format(self.__size, self.__size)

    def area(self):
        """return the square area"""
        return self.__size ** 2
