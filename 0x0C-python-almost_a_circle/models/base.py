#!/usr/bin/python3
""" Base module """


class Base:
    """ the base class """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        method to check id or assign it

        Args:
        id: is the is to be set

        Raise: none
        """
        if id is not None:
            seld.id = id
        else:
            Base.__nb_objects += 1
            seld.id = Base.__nb_objects
