#!/usr/bin/python3
"""class dfinition"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """class representation a rectangle using BaseGeometry"""

    def __init__(self, width, height):
        """intialization of a new Rectangle

        Args:
            width (int): new width of the Rectangle
            height (int): new height of the Rectangle
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
