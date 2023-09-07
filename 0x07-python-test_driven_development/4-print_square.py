#!/usr/bin/python3
"""
modules that print a square
size is the lenght of the square
it raises exception error if doesent meet the requirement
"""


def print_square(size):
    """ a function that print a square """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
