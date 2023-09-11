#!/usr/bin/python3
"""
a modules that returns the list of available
attributes and methods of an object
Returns list of obejcts
"""


def lookup(obj):
    """ afunction that returns the list of availabe attribute """
    return dir(obj)
