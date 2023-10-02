#!/usr/bin/python3
"""module 4-rectangle definng class
"""


class Rectangle:
    """Rectangle class defininition with width and height."""

    def __init__(self, width=0, height=0):
        """initializes instances

        Args:
            width: width of the rectangle
            height: height of the rectangle
        """
        self.width = width
        self.height = height

    def __str__(self):
        """returns an informal and nicely printable string representation
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

    @property
    def width(self):
        """func retrieving width of the instance"""
        return self.__width

    @width.setter
    def width(self, value):
        """func setting width

        Args:
            value: must be positive int
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieves the height of a Rectangle instance."""
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

    def area(self):
        """func calculating area

        Returns:
            area
        """
        return self.__width * self.__height

    def perimeter(self):
        """func calculating perimeter

        Returns:
            perimeter
        """
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.__width + self.__height)
