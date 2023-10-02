#!/usr/bin/python3
"""Module 6 defining a Rectangle class
"""


class Rectangle:
    """Rectangle class definition

    Attributes:
        number_of_instances: number of Rectangle instances
    """

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """initializing a Rectangle instances

        Args:
            width: width of the rectangle
            height: height of the rectangle
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
        Rectangle.number_of_instances -= 1

    @property
    def width(self):
        """finc retrieving the width"""
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
        """this func retrieves the height."""
        return self.__height

    @height.setter
    def height(self, value):
        """sets the height

        Args:
            value: height must be a positive int
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """func calculatig the area of a Rectangle instance

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
