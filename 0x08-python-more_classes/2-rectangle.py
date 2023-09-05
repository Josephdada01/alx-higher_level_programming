#!/usr/bin/python3
"""a class module that defines a rectangle"""


class Rectangle:
    """a class that defines a rectangle"""
    def __init__(self, width=0, height=0):
        """
        initialising the rectangle class
        Args:
            width: represent the width
            height: represnt the height of the rectangle
        Raises:
            TypeError: if size is not integer
            ValueError: if value is less than 0
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        I used property to retrieve width /sets it to private width"""
        return self.__width

    @width.setter
    def width(self, value):
        """ using setter to set new parameter "value" to width """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self, value):
        """
        using property to retrive height/setting it to private """
        return self.__height

    @height.setter
    def height(self, value):
        """ using setter to set new parameter "value" to height """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ a public isinstance that returns rectangle area """
        return self.__width * self.__height

    def perimeter(self):
        """ that returns the rectangle perimeter """
        if self.__width == 0 or self.__height == 0:
            return (0)
        return 2 * (self.__width  + self.__height)
