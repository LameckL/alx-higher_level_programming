#!/usr/bin/python3
"""
print_square module
prints a square with the char #
"""


def print_square(size):
    """func printing a square, size is the length and width of the square
    """

    if type(size) is not int:
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        for j in range(size):
            print('#', end='')
        print()
