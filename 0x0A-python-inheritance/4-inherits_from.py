#!/usr/bin/python3
"""class definition"""


def inherits_from(obj, a_class):
    """func checking if an object is an inherited class instance

    Args:
        obj (any): The object being checked
        a_class (type): class to match the objecttype
    Returns:
        True - object is an inherited instance of a class, else False
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
