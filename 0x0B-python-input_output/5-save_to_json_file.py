#!/usr/bin/python3
""" a module that writes an object to a file using json repr """

import json


def save_to_json_file(my_obj, filename):
    """ a function that write to a text using json repr """
    with open(filename, 'w') as f:
        return json.dump(my_obj, f)
