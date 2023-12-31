#!/usr/bin/python3
"""Module 5-rectangle clas Rectangle
"""


class Rectangle:
    """Rectangle class defining with width and height"""

    def __init__(self, width=0, height=0):
        """initializing instance

        Args:
            width: width
            height: height
        """
        self.width = width
        self.height = height

    def __str__(self):
        """Returns an informal and nicely printable string representation
        of a Rectangle instance, filled with the '#' char"""
        if self.__height == 0 or self.__width == 0:
            return ''
        rec_str = ''
        for i in range(self.__height):
            for j in range(self.__width):
                rec_str += '#'
            rec_str += '\n'
        return rec_str[:-1]

    def __repr__(self):
        """Return a string representation of a Rectangle instance
        that is able to recreate a new instance by using eval()
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Deletes a Rectangle instance"""
        print("Bye rectangle...")

    @property
    def width(self):
        """Retrieves the width of a Rectangle instance."""
        return self.__width

    @width.setter
    def width(self, value):
        """func setting the width

        Args:
            value: width must be a positive int
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """this retrieves the height"""
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
        """fuunc calculating area of a Rectangle

        Returns:
            area
        """
        return self.__width * self.__height

    def perimeter(self):
        """func calculating the perimeter

        Returns:
            perimeter
        """
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.__width + self.__height)
