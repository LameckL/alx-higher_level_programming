#!/usr/bin/python3
def weight_average(my_list=[]):

    if not my_list:

        return 0

    myNum = 0

    dns = 0

    for tup in my_list:

        myNum += tup[0] * tup[1]

        dns += tup[1]

    return (myNum / dns)
