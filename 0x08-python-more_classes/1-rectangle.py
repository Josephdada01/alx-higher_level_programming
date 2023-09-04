#!/usr/bin/python3
"""
this module is a class that defines a rectanglethat
has two attribute width and height
if they are not int raise TypeError
if they are less than 0 raise ValueError
"""


class Rectangle:
    """
    a class that defines a rectangle
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """ I used property to retrieve width and return private width"""
        return self.__width

    @width.setter
    def width(self, value):
        """I used setter to add a new value"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """ I used property to retrieve height and retirn private height"""
        return self.__height

    @height.setter
    def height(self, value):
        """ i used setter to add a new parameter to height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
