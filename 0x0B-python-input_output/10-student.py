#!/usr/bin/python3
""" a module that defines a student based on task 9-student.py """


class Student:
    """ a student class """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ a method that that retrieves dict representation of a student """
        if (type(attrs) == list and
                all(type(attr) == str for attr in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
