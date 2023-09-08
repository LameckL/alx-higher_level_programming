#!/usr/bin/python3
def max_integer(my_list=[]):
    """this fun finds the maximum integer in a list"""

    if len(my_list) == 0:

        return (None)

    great = my_list[0]

    for i in range(len(my_list)):

        if my_list[i] > great:

            great = my_list[i]

    return (great)
