#!/usr/bin/python3
"""class definition"""


class MyInt(int):
    """inverting operators == and !="""

    def __eq__(self, value):
        """this overrides == opeartor with != behavior"""
        return self.real != value

    def __ne__(self, value):
        """this overrides != operator with == behavior"""
        return self.real == value
