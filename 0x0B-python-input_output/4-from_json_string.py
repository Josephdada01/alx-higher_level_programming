#!/usr/bin/python3
""" a function that returns an object(data structure) rep by a json """

import json


def from_json_string(my_str):
    """ changing python object to json string """
    return json.loads(my_str)
