#!/usr/bin/python3
""" Module for Rectangle class """


class Rectangle(BaseGeometry):
    """ subclass inheret from BaseGeometry"""
    def __init__(self, width, height):
        """ initiate width and height """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
