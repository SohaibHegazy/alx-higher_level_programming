#!/usr/bin/python3
""" square class """


class Square:
    """ init """
    def __init__(self, size=0):
        """ check if not integer """
        if not isinstance(size, int):
            """ raise TypeError """
            raise TypeError("size must be an integer")
        """ check if < 0 """
        if size < 0:
            """ Raise ValueError """
            raise ValueError("size must be >= 0")
        self.__size = size
    """ get area """
    def area(self):
        return self.__size * self.__size
