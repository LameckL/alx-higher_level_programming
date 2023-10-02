#!/usr/bin/python3
"""second module for defining class Rectangle
"""


class Rectangle:
    """defining class Rectangle"""

    def __init__(self, width=0, height=0):
        """instance initialization

        Args:
            width: width
            height: height
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """retrieving class instances"""
        return self.__width

    @width.setter
    def width(self, value):
        """func setting width

        Args:
            value: width value must be positive int
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """retrieving the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """func setting height

        Args:
            value: value of the height, must be a positive integer
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """func finding area

        Returns:
            area
        """
        return self.__width * self.__height

    def perimeter(self):
        """func calculting perimeter

        Returns:
            perimeter
        """
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.__width + self.__height)
