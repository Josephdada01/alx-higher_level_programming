#!/usr/bin/python3
""" a function that returns the dictionary description
with simple data structure (list, dictionary, string, integer and
boolean for json serializtion of an object
"""


def class_to_json(obj):
    """ the function that returns json serialization of an object """
    return obj.__dict__
