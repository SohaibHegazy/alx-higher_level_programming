#!/usr/bin/python3
""" Module to represent square """
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    class of square inherits from Rectangle
    """

    def __init__(self, size, x=0, y=0, id=None):
        """ constructor """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        represents the square info
        """
        return "[{}] ({}) {}/{} - {}".format(type(self).__name__, self.id,\
                self.x, self.y, self.width)

    @property
    def size(self):
        """ getter for square """
        return self.width

    @size.setter
    def size(self, value):
        """ setter for sqaure """
        self.width = value
        self.height = value
