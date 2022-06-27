#!/usr/bin/python3
"""class Rectangle that defines a rectangle by: (based on 1-rectangle.py)"""


class Rectangle:
    """class Rectangle that compute perimeter and area of a rectangle"""

    def __init__(self, width=0, height=0):
        """Initialize class"""
        self.height = height
        self.width = width

    def __str__(self):
        """print rectangle according to the width and height"""
        string = ""
        if self.__height == 0 or self.__width == 0:
            return string
        string += ("#" * self.__width + "\n") * self.__height
        return string[:-1]

    def __repr__(self):
        """return a string representation of the rectangle"""
        return "Rectangle({}, {})".format(str(self.__width),
                                          str(self.__height))

    def __del__(self):
        """print the message Bye rectangle..."""
        print("Bye rectangle...")

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

    def area(self):
        """area of a rectangle"""
        return self.__height * self.__width

    def perimeter(self):
        """perimeter of a rectangle"""
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.__width + self.__height)
