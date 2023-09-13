#!/usr/bin/python3
""" a function that creates object fom JSON file """

import json


def load_from_json_file(filename):
    """create an object from Jspn file """
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
