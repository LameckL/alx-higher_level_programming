#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):

    """func printing all integers of a list in a reverse order"""

    if isinstance(my_list, list):

        my_list.reverse()

        for i in my_list:

            print("{:d}".format(i))
