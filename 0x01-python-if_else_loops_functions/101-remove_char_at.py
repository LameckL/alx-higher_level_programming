#!/usr/bin/python3
def remove_char_at(str, n):
    """this func creates copy of the str without the char at position n"""
    if n < 0:
        return (str)
    return (str[:n] + str[n+1:])
