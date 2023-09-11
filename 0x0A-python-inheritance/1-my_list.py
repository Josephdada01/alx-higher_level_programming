#!/usr/bin/python3
"""
A class module that inherits Mylist from list
then defines a public instances that prints the in sorted way
"""


class MyList(list):
    """ a class that was inherits from list """
    def print_sorted(self):
        """ a public instance method that list in ascending sort """
        sort_the_list = sorted(self)
        print(sort_the_list)
