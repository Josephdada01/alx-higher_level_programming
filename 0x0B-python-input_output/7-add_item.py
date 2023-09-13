#!/usr/bin/python3
""" a module tha adds all arguments to a python list """

import sys
import json
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = 'add_item.json'
try:
    existing_items = load_from_json_file(filename)
except FileNotFoundError:
    existing_items = []

for arg in sys.argv[1:]:
    existing_items.append(arg)

save_to_json_file(existing_items, filename)
