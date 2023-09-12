#!/usr/bin/python3
""" a module that defines a basegeometry """


class BaseGeometry:
    """ a basegeometry class with a public instance """

    def area(self):
        """
        a public instance method that raises an exception
        """
        raise Exception("area() is not implemented")
