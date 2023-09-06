#!/usr/bin/python3
"""
a module that defines two integer
a must be an integer or floats else raise type error
a and b must be casted into intgers if they are float
"""


def add_integer(a, b=98):
    """
    a function that add two integers a and b must be int or float
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    return a + b
