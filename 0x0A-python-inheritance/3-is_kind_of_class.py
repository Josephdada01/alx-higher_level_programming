#!/usr/bin/python3
"""
checks if the object is an instance of, or if the obect is an instance
of a class that inherited from, the specific class
not allow to import modules
"""


def is_kind_of_class(obj, a_class):
    """ check if it is same class or inherit from """
    return isinstance(obj, a_class)
