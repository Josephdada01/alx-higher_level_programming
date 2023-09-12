#!/usr/bin/python3
"""
a modules that defines a BaseGeometry
also defines a public public instance "area"
and integer_validator
"""


class BaseGeometry:
    """ a class that defines BaseGeometry """
    def area(self):
        """ public instance method with an exception message """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ a public instance """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
