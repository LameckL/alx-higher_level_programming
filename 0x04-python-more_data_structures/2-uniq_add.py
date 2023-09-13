#!/usr/bin/python3
def uniq_add(my_list=[]):

    _lst = set(my_list)

    num = 0

    for i in _lst:

        num += i

    return (num)
