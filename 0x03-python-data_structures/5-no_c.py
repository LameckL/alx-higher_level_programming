#!/usr/bin/python3

def no_c(my_string):
    """func removing all characters c and C in a string"""
    copy = [x for x in my_string if x != 'c' and x != 'C']
    return ("".join(copy))
