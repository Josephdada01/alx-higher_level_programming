#!/usr/bin/python3
""" a class modeules """


class Rectangle:
    """ a class that defines a rectangle """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """ using property to retrieve width """
        return self.__width

    @width.setter
    def width(self, value):
        """ using setter to set new parameter to width """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ using property to retrieve height"""
        return self.__height

    @height.setter
    def height(self, value):
        """ using setter to set new parameter to height """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ a public isinstance that return the area of rectangle """
        return self.__width * self.__height

    def perimeter(self):
        """ returns the rectangle perimeter """
        if self.__width == 0 or self.__height == 0:
            return (0)
        return 2 * (self.width + self.height)

    def __str__(self):
        """ returns the string represntation of rectangle using '#' """
        if self.width == 0 or self.height == 0:
            return ""
        rectangle_str = ""
        for _ in range(self.height):
            rectangle_str += "#" * self.width + "\n"
        return rectangle_str.rstrip()

    def __repr__(self):
        """ returns the string representation of rectangle """
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """ print message when deleting it self """
        print("Bye rectangle...")
