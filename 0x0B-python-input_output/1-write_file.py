#!/usr/bin/python3
"""function function"""


def write_file(filename="", text=""):
    """func writing a string to a UTF8 text file

    Args:
        filename (str): filename to write
        text (str): text to write to the file
    Returns:
        number of characters written
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
