#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    """func finding all multiples of 2 in a list"""

    mltpls = []

    for i in range(len(my_list)):

        if my_list[i] % 2 == 0:

            mltpls.append(True)

        else:

            mltpls.append(False)

    return (mltpls)
