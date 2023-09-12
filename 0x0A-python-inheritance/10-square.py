#!/usr/bin/python3
""" a class square modules that inherit from Rectangle """

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ a class that defines a square, inherits from Rectangle """
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """ a method that defines an area """
        return self.__size ** 2
