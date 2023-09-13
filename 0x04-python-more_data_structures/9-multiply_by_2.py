#!/usr/bin/python3
def multiply_by_2(a_dictionary):

    newd = a_dictionary.copy()

    list_keys = list(newd.keys())

    for i in list_keys:

        newd[i] *= 2

    return (newd)
