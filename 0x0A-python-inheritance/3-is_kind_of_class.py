#!/usr/bin/python3
"""class definition"""


def is_kind_of_class(obj, a_class):
    """func checking if an object is an instance or inherited instance of a class

    Args:
        obj (any): object being checked
        a_class (type): class being matched object type to
    Returns:
        True - object is a class instance or inherited instance, else False
    """
    if isinstance(obj, a_class):
        return True
    return False
    
