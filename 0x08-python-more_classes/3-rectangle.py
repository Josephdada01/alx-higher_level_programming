#!/usr/bin/python3
""" moodules that defines a Rectangle """


class Rectangle:
    """
    a class that defines a rectangle
    args:
        width - the width
        height - the height
    returns:
        Rectangle
    raises:
        TypeError
        ValueError
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """ retrieving width with property"""
        return self.__width

    @width.setter
    def width(self, value):
        """ setting new parameter to width - value """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """" retrieving height """
        return self.__height

    @height.setter
    def height(self, value):
        """ setting new parameter to height - "value" """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ insistance that return rectangle area """
        return self.__width * self.__height

    def perimeter(self):
        """ returns the rectangle perimeter """
        if self.__width == 0 or self.__height == 0:
            return (0)
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Returns: a string representation of rectangle using '#'
        Returns:
            str: A string representation of the rectangle
        """
        string = ""
        if self.__width != 0 and self.__height != 0:
            string += "\n".join("#" * self.__width
                                for j in range(self.__height))
            return string
