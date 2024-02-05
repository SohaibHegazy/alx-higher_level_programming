#!/usr/bin/python3
""" module for square as an inheret of Rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ class of square that inherets from Rectangle """
    def __init__(self, size):
        """ constructor of square """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """ function to calculate area"""
        return self.__size * self.__size

    def __str__(self):
        """ returns the representation of the square """
        return "[Square]" + str(self.__size) + "/" + str(self.__size)
