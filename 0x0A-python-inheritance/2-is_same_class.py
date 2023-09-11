#!/usr/bin/python3
"""
a module check is exact the same instance of the specified class
it reurns true if they are the same
or false
"""


def is_same_class(obj, a_class):
    """ a function that returns true if objrct is exactly same instance """
    return isinstance(obj, a_class)
