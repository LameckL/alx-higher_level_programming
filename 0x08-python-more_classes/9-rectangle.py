#!/usr/bin/python3
"""Module 9 definition of a Rectangle class
"""


class Rectangle:
    """definition of Rectangle class by width and height

    Attributes:
        number_of_instances: number of Rectangle instances
    """

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """initializing Rectangle instance

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
                rec_str += str(self.print_symbol)
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
        """func etrieving the width of a Rectangle instance"""
        return self.__width

    @width.setter
    def width(self, value):
        """func setting width of a Rectangle instance

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
        """func retrieving height"""
        return self.__height

    @height.setter
    def height(self, value):
        """func setting height

        Args:
            value: height value must be a positive int
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """func calculating area of a Rectangle instance

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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """func dertimining the largest Rectangle based on the area

        Args:
            rect_1: Rectangle instance
            rect_2: different Rectangle instance

        Returns:
            instance with largest area,
            or rect_1 if both areas are equal
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() == rect_2.area() or rect_1.area() > rect_2.area():
            return rect_1
        if rect_1.area() < rect_2.area():
            return rect_2

    @classmethod
    def square(cls, size=0):
        """func creating a new Rectangle instance with width == height == size

        Args:
            size: size to set new rectangle to

        Returns:
            new rectangle instance
        """
        return cls(size, size)
