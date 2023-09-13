#!/usr/bin/python3
""" a function that returns the json representation of object(string) """

import json


def to_json_string(my_obj):
    """ a funtion that return json representation """
    return json.dumps(my_obj)
