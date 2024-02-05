#!/usr/bin/python3
""" Module for Rectangle class """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ subclass inheret from BaseGeometry"""
    def __init__(self, width, height):
        """ initiate width and height """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """ method to calculate area of Rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """ Method to display the rectangle"""
        return "[Rectangle] " + str(self.__width) + "/" + str(self.__height)
