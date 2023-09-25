#!/usr/bin/python3
def safe_print_integer(value):
    """func printing an integer with "{:d}".format()
    Args:
    integer value to print.
    Returns:
    if value has been correctly printed - True
    Otherwise - False
    """
try:
    print("{:d}".format(value))
    return (True)
except (TypeError, ValueError):
    return (False)
