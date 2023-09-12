#!/usr/bin/python3
""" a module that defines Rectangle class from BaseGeometry """

BaseGeometry = __import__('7-base_geometry').BaseGeometry

    
class Rectangle(BaseGeometry):
    """ a Rectangle class inherit from Basegeometry """
    def __init__(self, width, height):
        """
        a method that takes in two parameter
        args:
            width:
            height:
        they must be private and a positive integer
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
