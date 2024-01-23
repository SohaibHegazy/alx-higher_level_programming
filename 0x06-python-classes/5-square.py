#!/usr/bin/python3
""" square class """


class Square:
    """ init """
    def __init__(self, size=0):
        """ init """
        self.size = size

    @property
    def size(self):
        """ property """
        return self.__size

    @size.setter
    def size(self, value):
        """ check if not integer """
        if not isinstance(value, int):
            """ raise TypeError """
            raise TypeError("size must be an integer")
        """ check if < 0 """
        if value < 0:
            """ Raise ValueError """
            raise ValueError("size must be >= 0")
        self.__size = value
    """ get area """
    def area(self):
        return self.__size * self.__size
    """ draw square """
    def my_print(self):
        for i in range(self.size):
            for j in range(self.size):
                if i is self.size - 1 and i != j:
                    print("#")
                else:
                    print("#", end="")
        print()
