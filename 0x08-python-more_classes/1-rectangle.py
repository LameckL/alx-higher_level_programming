#!/usr/bin/python3
"""module definition of a class Rectangle
"""


class Rectangle:
    """defining class Rectangle"""

    def __init__(self, width=0, height=0):
        """initialixing class instances

        Args:
            width: rectangle's width
            height: rectangle's height
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """func retrieving width"""
        return self.__width

    @width.setter
    def width(self, value):
        """func setting width

        Args:
            value: width value should be a positive int
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """func retrieving height"""
        return self.__height

    @height.setter
    def height(self, value):
        """func setting height

        Args:
            value: must be positive int
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
