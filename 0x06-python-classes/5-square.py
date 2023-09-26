#!/usr/bin/python3
"""class Square definition"""


class Square:
    """representing a square"""

    def __init__(self, size):
        """initializing a new square

        Args:
            size (int): new square size
        """
        self.size = size

    @property
    def size(self):
        """current size of the square setting/getting"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Func returning current area of a square"""
        return (self.__size * self.__size)

    def my_print(self):
        """Func printing a square with the # char"""
        for i in range(0, self.__size):
            [print("#", end="") for j in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
