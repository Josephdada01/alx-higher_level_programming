#!/usr/bin/python3


def best_score(a_dictionary):
    if not a_dictionary:
        return None
    bigger_value = max(a_dictionary.values())
    for key, value in a_dictionary.items():
        if value == bigger_value:
            return key
