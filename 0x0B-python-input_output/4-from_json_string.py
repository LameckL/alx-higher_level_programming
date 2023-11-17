#!/usr/bin/python3
# 6-from_json_string.py
"""function definition"""
import json


def from_json_string(my_str):
    """fun returning Python object representation of JSON string"""
    return json.loads(my_str)
