#!/usr/bin/python3
"""third module of Rectangle class
"""


class Rectangle:
    """class Rectangle definition by width and height"""

    def __init__(self, width=0, height=0):
        """initializing Rectangle instance

        Args:
            width: width
            height: height
        """
        self.width = width
        self.height = height

    def __str__(self):
        """Returns an informal and nicely printable string representation
        of a Rectangle instance, filled with the '#' character."""
        if self.__height == 0 or self.__width == 0:
            return ''
        rec_str = ''
        for i in range(self.__height):
            for j in range(self.__width):
                rec_str += '#'
            rec_str += '\n'
        return rec_str[:-1]

    @property
    def width(self):
        """retrieving width"""
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
        """retrieving height"""
        return self.__height

    @height.setter
    def height(self, value):
        """func setting the height

        Args:
            value: height must be a positive int
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """func calculationg are

        Returns:
            area
        """
        return self.__width * self.__height

    def perimeter(self):
        """this func finds perimeter

        Returns:
            perimeter
        """
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.__width + self.__height)
