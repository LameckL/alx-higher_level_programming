#!/usr/bin/python3
def multiple_returns(sentence):
    """func returning str length and its first char"""
    if sentence == "":
        return (0, None)
    return (len(sentence), sentence [0])
