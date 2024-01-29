#!/usr/bin/python3
""" This is a real representation of a rectangle """


class Rectangle:
    """ This class represents a rectangle """

    number_of_instances = 0

    print_symbol = "#"
    """ print symbol to represent the rectangle """

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
            return ""
        else:
            return ((str(self.print_symbol) * self.__width + "\n") *
                    self.__height)[:-1]

    def __repr__(self):
        """ represent a rectangle """
        return ("Rectangle({:d}, {:d})".format(self.__width, self.__height))

    def __del__(self):
        """ prints a message when deleting a rectangle instance """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    def bigger_or_equal(rect_1, rect_2):
        """ to print the bigger rectangle of two rectangles

        Args:
        rect_1: first rectangle to be compared
        rect_2: second rectangle to be compared

        Raise: 
        TypeError("rect_1 must be an instance of Rectangle")
        when rect_1 is not instance of Rectangle
        OR
        TypeError("rect_2 must be an instance of Rectangle")
        when rext_2 is not instance of Rectangle

        Return: the bigger area, or rect_1 if both are equal
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")

        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_2.area() > rect_1.area():
            return rect_2.area()
        else:
            return rect_1.area()
