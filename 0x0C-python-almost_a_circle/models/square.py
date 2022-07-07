#!/usr/bin/python3
"""class Square that inherits from Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Initialize class square"""

    def __init__(self, size, x=0, y=0, id=None):
        """Class constructor"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """return [Square] (<id>) <x>/<y> - <size>"""
        return ("[Square] ({}) {}/{} - {}".format(self.id, self._Rectangle__x,
                                                  self._Rectangle__y,
                                                  self._Rectangle__height))

    def to_dictionary(self):
        """returns the dictionary representation of a Rectangle"""
        return ({'id': self.id, 'size': self.size, 'x': self._Rectangle__x,
                 'y': self._Rectangle__y})

    @property
    def size(self):
        """retrieve size"""
        return self._Rectangle__height

    @size.setter
    def size(self, value):
        """set size requirements"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        if value <= 0:
            raise ValueError("height must be > 0")
        self._Rectangle__width = value
        self._Rectangle__height = value

    def update(self, *args, **kwargs):
        """playing with args and kwargs"""
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self._Rectangle__x = args[2]
            if len(args) >= 4:
                self._Rectangle__y = args[3]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)
