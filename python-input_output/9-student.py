#!/usr/bin/python3
"""Contains a method for Create Student to JSON"""


class Student:
    def __init__(self, first_name, last_name, age):
        """class Student that defines a student by:"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Public method def to_json(self):
        that retrieves a dictionary representation of a Student
        """
        return {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'age': self.age

        }
