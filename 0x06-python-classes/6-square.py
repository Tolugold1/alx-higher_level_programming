#!/usr/bin/python3
"""class Square that defines a square by: (based on 5-square.py)"""


class Square:
    """class Square that defines a square"""
    def __init__(self, size=0, position=(0, 0)):
        """Initialize size and position"""
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """retrieve size"""
        return self.__size

    @size.setter
    def size(self, value):
        """check for size requirements"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """retrieve position"""
        return self.__position

    @position.setter
    def position(self, value):
        """test for position requirement"""
        if (value[0] < 0 or value[1] < 0 or type(value) != tuple
                or type(value[0]) != int or type(value[1]) != int
                or len(value) != 2):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """compute square"""
        return self.__size ** 2

    def my_print(self):
        """prints in stdout the square with the character #"""
        if self.__size == 0:
            print()
        else:
            print('\n' * self.__position[1], end='')
            for i in range(self.__size):
                print(' ' * self.__position[0], end='')
                print('#' * self.__size)
