#!/usr/bin/python3
"""class definition"""


class Student:
    """class representantation of student"""

    def __init__(self, first_name, last_name, age):
        """initialization of new Student

        Args:
            first_name (str): first name of the student
            last_name (str): name of the student
            age (int): age of the student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """func getting a dictionary representation of a student
        
        If attribute is string lists, represent only the
        ones on in the list

        Args:
            attrs (list): attributes to represent
        """
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
