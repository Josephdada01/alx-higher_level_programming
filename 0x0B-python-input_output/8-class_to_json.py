#!/usr/bin/python3
""" a function that returns the dictionary description
with simple data structure (list, dictionary, string, integer and
boolean for json serializtion of an object
"""


def class_to_json(obj):
    """ the function that returns json serialization of an object """
    if isinstance(obj,(str, int, bool)):
        return obj
    if isinstance(obj, list):
        return [serialize_to_dict(item) for item in obj]
    if isinstance(obj, dict):
        return {key: serialize_to_dict(value) for key, value in obj.item()}
