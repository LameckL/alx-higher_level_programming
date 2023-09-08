#!/usr/bin/python3
def element_at(my_list, idx):
    """this func etrives an element from a list similar to C"""

    if idx < 0 or idx > (len(my_list) - 1):

        return None

    return (my_list[idx])
