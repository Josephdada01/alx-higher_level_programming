#!/usr/bin/python3
""" a class module based on 8.rectangle.py """


class BaseGeometry:
    """ class that defines basegeometry """
    def area(self):
        """ a public instance method with an exception message """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ a public instance """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """ class rectangle inherited from BaseGeometry """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """ method that defines an area """
        if self.__width is not None and self.__height is not None:
            return self.__width * self.__height

    def __str__(self):
        """ string representation """
        if self.__width is not None and self.__height is not None:
            return f"[Rectangle] {self.__width}/{self.__height}"
