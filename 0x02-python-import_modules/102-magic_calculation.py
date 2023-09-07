#!/usr/bin/python3
def magic_calculation(a, b):
    from magic_calculation_102 import add, sub

    if a < b:
        su = add(a, b)
        for i in range(4, 6):
            su = add(su, i)
        return (su)

    else:
        return(sub(a, b))
