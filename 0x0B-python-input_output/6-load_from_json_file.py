#!/usr/bin/python3
"""function definition"""
import json


def load_from_json_file(filename):
    """func creating Python object from a JSON file"""
    with open(filename) as f:
        return json.load(f)
