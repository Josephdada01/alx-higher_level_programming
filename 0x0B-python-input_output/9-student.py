#!/usr/bin/python3
""" a class student module that defines a student by:
    first_name, last_name, age
and a method that retrieves a dictionary representation
"""


class Student:
    """ a class that defines a student """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        using at poperty to retrive the student class
        and returnining the dictionary representation
        """
        stu_dict = {
                "first_name": self.first_name,
                "last_name": self.last_name,
                "age": self.age
                }
        return stu_dict
