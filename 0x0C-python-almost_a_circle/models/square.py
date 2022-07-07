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
        return ("[Square] {} {}/{} - {}".format(self.id, self._Rectangle__x,
                                                self._Rectangle__y,
                                                self._Rectangle__height))
