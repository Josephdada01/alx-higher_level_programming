#!/usr/bin/python3
"""
A modules that prints first name and last name
firstname and last name must be string
otherwise raise type error
"""


def say_my_name(first_name, last_name=""):
    """ function definition """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    full_name = f"My name is {first_name} {last_name}"
    print(full_name)
