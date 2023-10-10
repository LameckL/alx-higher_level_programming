#!/usr/bin/python3
"""class definition"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class representation of a square"""

    def __init__(self, size):
        """initialization a new square

        Args:
            size (int): size of a new square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
