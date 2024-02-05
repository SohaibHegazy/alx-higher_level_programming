#!/usr/bin/python3
""" Module for BaseGEometry class """


class BaseGeometry:
    """ class of BaseGeometry """
    def area(self):
        """
        function that raises an exception

        Args:
        self

        Return: Raise an exception
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        function to validate value

        Args:
        name: a string
        value: an int

        Raise:
        if not int: raise TypeError("<name> must be an integer")
        if < 0: raise ValueError("<name> must be greater than 0")
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

class Rectangle(BaseGeometry):
    """ subclass inheret from BaseGeometry"""
    def __init__(self, width, height):
        """ initiate width and height """
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height
