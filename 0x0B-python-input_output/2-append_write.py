#!/usr/bin/python3
"""function definition"""


def append_write(filename="", text=""):
    """func appending a string to the end of a UTF8 text file

    Args:
        filename (str): filename to append to
        text (str): string being appended
    Returns:
        number of characters appended
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
