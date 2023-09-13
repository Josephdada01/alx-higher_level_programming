#!/usr/bin/python3
""" a module similar to 10-student.py
this time it adds a new methof tha replace all attribut instance
"""


class Student:
    """ a class that defines student """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ a method that dictionary representation """
        if attrs is None:
            return self.__dict__
        new_dict = {}
        for attr in attrs:
            try:
                new_dict[a] = self.__dict__[a]
            except FileNotFoundError:
                pass
        return new_dict

    def reload_from_json(self, json):
        """ a method that replaces all attributes of the student """
        for key in json:
            try:
                setattr(self, key, json[key])
            except FileNotFoundError:
                pass
