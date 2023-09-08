#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    """func replacing an element in a copied list at a given position"""

    if idx < 0 or idx > (len(my_list) - 1):

        return (my_list)

    cp = [x for x in my_list]

    cp[idx] = element

    return (cp)
