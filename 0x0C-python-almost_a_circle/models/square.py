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
        return "[{}] ({}) {}/{} - {}".\
               format(type(self).__name__, self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """ getter for square """
        return self.width

    @size.setter
    def size(self, value):
        """ setter for sqaure """
        self.width = value
        self.height = value

    def _update(self, id=None, size=None, x=None, y=None):
        """ method to add values to attrs"""
        if id is not None:
            self.id = id
        if size is not None:
            self.size = size
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    def update(self, *args, **kwargs):
        """ method to handle args and kwargs"""
        if args:
            self._update(*args)
        elif kwargs:
            self._update(**kwargs)

    def to_dictionary(self):
        """ method to put attrs in dict """
        return {"id": self.id, "size": self.width, "x": self.x, "y": self.y}
