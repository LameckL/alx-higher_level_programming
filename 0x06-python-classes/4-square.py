#!/usr/bin/python3
"""class Square definition"""


class Square:
    """Representation of a square."""

    def __init__(self, size=0):
        """initialization of new square

        Args:
            size (int): new square size
        """
        self.size = size

    @property
    def size(self):
        """Current square size set or getting"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return current square area"""
        return (self.__size * self.__size)
