#!/usr/bin/python3
"""class BaseGeometry"""


class BaseGeometry:
    """Raise an exception"""
    def area(self):
        """raise an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validator"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


"""class Rectangle that inherits from BaseGeometry 7-base_geometry.py"""


class Rectangle(BaseGeometry):
    """rectangular class with width and height"""
    def __init__(self, width, height):
        """Initializer"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """return printed rectangle"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    def area(self):
        """area of a rectangle"""
        return self.__width * self.__height
