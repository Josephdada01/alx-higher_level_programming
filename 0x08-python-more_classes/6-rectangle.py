#!/usr/bin/python3
""" a class module that defines a Rectangle """


class Rectangle:
    """ a class that defines a Rectangle """
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """ retrieving width """
        return self.__width

    @width.setter
    def width(self, value):
        """ setting new parameter to width """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
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
        """ returns the area of rectangle """
        return self.__width * self__height

    def perimeter(self):
        """ return the perimeter of a rectagle """
        if self.__width == 0 or self.__height == 0:
            return (0)
        return 2 * (self.width + self.height)

    def __str__(self):
        """ returns the string representation of rectangle using '#' """
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
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
