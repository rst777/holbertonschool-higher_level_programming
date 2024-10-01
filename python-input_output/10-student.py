#!/usr/bin/python3
"""Contains a method for Create Student to JSON"""


class Student:
    def __init__(self, first_name, last_name, age):
        """class Student that defines a student by:"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Public method def to_json(self):
        that retrieves a dictionary representation of a Student
        If attrs is a list of strings, only attribute names contained in
        this list must be retrieved.
        """
        if isinstance(attrs, list) and all(isinstance(attr, str)
                                           for attr in attrs):
            return {attr: getattr(self, attr)
                    for attr in attrs if hasattr(self, attr)}
        return self.__dict__
