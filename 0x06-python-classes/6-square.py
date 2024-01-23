#!/usr/bin/python3
""" draw square """


class Square:
    """ init """
    def __init__(self, size=0, position=(0, 0)):
        """ init attr """

        self.size = size
        self.position = position

    @property
    def size(self):
        """ getter for size """
        return self.__size

    @size.setter
    def size(self, value):
        """ size setter """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    """ position getter """
    def position(self):
        """ check """
        return self.__position

    @position.setter
    def position(self, value):
        """ check """
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)
            """ check
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(isinstance(num, int) for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(num >= 0 for num in value):
             """
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """ check """
        return self.__size * self.__size

    def my_print(self):
        """ draw square """
        if self.__size == 0:

    for i in range(0, self.__position[1]):
        print("")

    for i in range(0, self.__size):
        for j in range(0, self.__position[0]):
            print(" ", end="")
        for k in range(0, self.__size):
            print("#", end="")
        print("")
