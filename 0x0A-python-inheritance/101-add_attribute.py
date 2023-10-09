#!/usr/bin/python3
"""class definition"""


def add_attribute(obj, att, value):
    """func adding new attribute to an object if possible

    Args:
        obj (any): object to add an attribute
        att (str): name of the attribute to add to object
        value (any): attribute's value
    Raises:
        TypeError: the attribute cannot be added.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
