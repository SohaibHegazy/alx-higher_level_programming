#!/usr/bin/python3
""" This is a real representation of a rectangle """


class Rectangle:
    """ This class represents a rectangle """
    
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """ defines a rectangle
        Args:
        width: is the rectangle width
        height is the rectangle height
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """ width getter to retrieve it """
        return self.__width

    @width.setter
    def width(self, value):
        """ setter for width as a private instance"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ height getter as a private instance """
        return self.__height

    @height.setter
    def height(self, value):
        """ height setter as a private instance """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ to calculate the area of the rectangle """
        return self.__width * self.__height

    def perimeter(self):
        """ to calculate perimeter of the rectangle """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return ((self.__width + self.__height) * 2)

    def __str__(self):
        """ draw the rectangle using # """
        rec = ""
        if self.__width == 0 or self.__height == 0:
            rec = ""
        else:
            rec += "\n".join("#" * self.__width for j in range(self.__height))
        return rec

    def __repr__(self):
        """ represent a rectangle """
        return ("Rectangle({:d}, {:d})".format(self.__width, self.__height))

    def __del__(self):
        """ prints a message when deleting a rectangle instance """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
