#!/usr/bin/python3
"""class Rectangle that defines a rectangle by: (based on 0-rectangle.py)"""


class Rectangle:
    """class Rectangle that defines a rectangle by: height and width"""
    def __init__(self, width=0, height=0):
        """Initialize class"""
        self.height = height
        self.width = width

    @property
    def width(self):
        """retrieve width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setting width and it's requirements"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """retrieve height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setting height and it's requirements"""
        if isinstance(value, int) == 0:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
