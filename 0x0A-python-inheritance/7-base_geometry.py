#!/usr/bin/python3
"""class definition"""


class BaseGeometry:
    """class reprsentation of base geometry"""

    def area(self):
        """func not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """func validating a param as an integer

        Args:
            name (str): parameter name
            value (int): parameter being validated
        Raises:
            TypeError: If the value is not an integer
            ValueError: If the value is <= 0
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
