#!/usr/bin/python3
"""
add-integer module,
sums two integers

"""


def add_integer(a, b=98):
    """a func returning sum of a and b,
    or an error if a and b arenot integers or floats
    """

    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")

    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)

    return a + b
