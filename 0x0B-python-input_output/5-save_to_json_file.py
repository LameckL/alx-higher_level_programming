#!/usr/bin/python3
"""function definition"""
import json


def save_to_json_file(my_obj, filename):
    """func writing an object to text file using JSON representation"""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
