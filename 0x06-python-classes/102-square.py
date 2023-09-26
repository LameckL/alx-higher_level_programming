#!/usr/bin/python3
"""definition of class Square"""


class Square:
    """Representation of a square"""

    def __init__(self, size=0):
        """initialization a new square

        Args:
            size (int): new square size
        """
        self.size = size

    @property
    def size(self):
        """current square size setting or getting"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current area of the square."""
        return (self.__size * self.__size)

    def __eq__(self, other):
        """defining comparison to Square"""
        return self.area() == other.area()

    def __ne__(self, other):
        """defining comparison to Square"""
        return self.area() != other.area()

    def __lt__(self, other):
        """defining comparison to Square"""
        return self.area() < other.area()

    def __le__(self, other):
        """defining comparison to Square"""
        return self.area() <= other.area()

    def __gt__(self, other):
        """defining comparison to Square"""
        return self.area() > other.area()

    def __ge__(self, other):
        """defining comparison to Square"""
        return self.area() >= other.area()
