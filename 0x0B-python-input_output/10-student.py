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
        stud_dict = {
                "first_name": self.first_name,
                "last_name": self.last_name,
                "age": self.age
                }
        if attrs is None:
            attrs = self.__dict__.keys()
        for attr in attrs:
            if hasattr(self, attr):
                stud_dict[attr] = getattr(self, attr)
        return stud_dict
