#!/usr/bin/python3
"""class BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


"""class Rectangle that inherits from BaseGeometry 7-base_geometry.py"""


class Rectangle(BaseGeometry):
    """rectangular class with width and height"""
    def __init__(self, width, height):
        """Initializer"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.width = width
        self.height = height
