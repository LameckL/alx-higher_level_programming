#!/usr/bin/python3
def number_keys(a_dictionary):

    mynum = 0

    list_keys = list(a_dictionary.keys())

    for i in list_keys:

        mynum += 1

    return (mynum)
