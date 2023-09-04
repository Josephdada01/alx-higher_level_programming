#!/usr/bin/python3
"""
a class module that defines a rectangle
based on task 1-rectangle.py
added a public isinstance method area that returns
the rectangle area and
a public isinstance method perimeter that returns rectangle perimeter
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
        """
        I used property to retrieve width and it return
        private attribute width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        using setter to set new parameter "value" to width
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self, value):
        """
        using property to retrive height and setting it to
        private attribute height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        using setter to set new parameter "value" to height
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """
        a public isinstance that returns rectangle area
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        a public isinstance that returns the rectangle perimeter
        """
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))
