#!/usr/bin/python3
""" a class module that defines a Rectangle """


class Rectangle:
    """ a rectangle class """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """ retrieving width """
        return self.__width

    @width.setter
    def width(self, value):
        """ setting a parameter to width """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self, value):
        """ retrieving height """
        return self.__height

    @height.setter
    def height(self, value):
        """ setting new parameter to height """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ a new instance that returns the rectangle area """
        return self.__width * self.__height

    def perimeter(self):
        """ instance that return the rectangle perimeter """
        if self.__width == 0 or self.__height == 0:
            return (0)
        return 2 * (self.__width + self.__height)
