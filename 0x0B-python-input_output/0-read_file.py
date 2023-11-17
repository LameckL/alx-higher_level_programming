#!/usr/bin/python3
"""func definition"""


def read_file(filename=""):
    """func printing contents of a UTF8 text file to stdout"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
