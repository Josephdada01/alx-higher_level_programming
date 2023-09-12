#!/usr/bin/python3
"""
a function that return true if object is an instance of a class
that inherited from specified class; otherwise false.
not importing any module
"""


def inherits_from(obj, a_class):
    """ is it subclass or not """
    return (issubclass(type(obj), a_class) and type(obj) != a_class)
