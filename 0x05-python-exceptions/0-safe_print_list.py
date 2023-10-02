#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """this func prints elememts of a list
    Args:
    my_list (list): list from which the elements are being print from
    x (int): no. of elements of my_list to print
    Returns:
    no. of elements being printed
    """


el = 0
for i in range(x):
    try:
        print("{}".format(my_list[i]), end="")
        el += 1
    except IndexError:
        break
print("")
return (el)
