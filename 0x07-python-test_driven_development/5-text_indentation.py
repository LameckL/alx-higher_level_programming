#!/usr/bin/python3
"""
text_indentation module
puts 2 new lines after a char set
"""


def text_indentation(text):
    """func printing text with extra two newlines just
    after these chars ['.', '?', ':']
    """

    if type(text) is not str:
        raise TypeError("text must be a string")

    for delim in ".:?":
        text = (delim + "\n\n").join(
            [line.strip(" ") for line in text.split(delim)])

    print("{}".format(text), end="")
