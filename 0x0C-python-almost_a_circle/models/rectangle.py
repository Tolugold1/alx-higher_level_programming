#!/usr/bin/python3
"""Rectangle class that inherit from Base class"""
from models.base import Base


class Rectangle(Base):
    """Initialising Rectangle class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Class constructor"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)
