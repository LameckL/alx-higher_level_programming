#!/usr/bin/python3
"""class definition"""


def is_same_class(obj, a_class):
    """fun checking if an object is an instance of a certain class

    Args:
        obj (any): object being checked
        a_class (type): class to match the type of object
    Returns:
        True - object is exact istance, else - False
    """
    if type(obj) == a_class:
        return True
    return False
