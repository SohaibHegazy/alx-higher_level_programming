#!/usr/bin/python3
""" The Rectangle Module """
from models.base import Base


class Rectangle(Base):
    """
    Rectngle class that inherits
    from Base class
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ constructor """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ method to retuen width of Rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """ setter of width of Rectangle"""
        self.__width = value

    @property
    def height(self):
        """ getter of height of Rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter of height of Rectangle"""
        self.__height = value

    @property
    def x(self):
        """ getter of x of Rectangle"""
        return self.__x

    @setter.x
    def x(self, value):
        """ setter of x of Rectangle"""
        self.__x = value

    @property
    def y(self):
        """ getter of y of Rectangle"""
        return self.__y

    def u(self, value):
        """ setter of y of Rectangle"""
        self.__y = value


