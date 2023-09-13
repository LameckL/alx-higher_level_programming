#!/usr/bin/python3
def to_subtract(list_num):

    _subt = 0

    max_list = max(list_num)


    for n in list_num:

        if max_list > n:

            _subt += n

    return (max_list - _subt)

def roman_to_int(roman_string):

    if not roman_string:

        return 0


    if not isinstance(roman_string, str):

        return 0


    rom_n = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    list_keys = list(rom_n.keys())


    num = 0

    lastRoman = 0

    lsnum = [0]


    for ch in roman_string:

        for r_num in list_keys:

            if r_num == ch:

                if rom_n.get(ch) <= lastRoman:

                    num += to_subtract(lsnum)

                    lsnum = [rom_n.get(ch)]

                else:

                    lsnum.append(rom_n.get(ch))


                lastRoman = rom_n.get(ch)


    num += to_subtract(lsnum)


    return (num)
