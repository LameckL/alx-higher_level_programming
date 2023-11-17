#!/usr/bin/python3
"""function definition"""


def class_to_json(obj):
    """func returning dictionary represntation of a data structure"""
    return obj.__dict__
