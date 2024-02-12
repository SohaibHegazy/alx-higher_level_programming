#!/usr/bin/python3
""" Base module for base class"""
from json import dumps, loads


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
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        serialize dict using json
        """
        if not list_dictionaries or list_dictionaries is None:
            return "[]"
        else:
            return dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """method to return an instance with all attrs set"""
        from models.rectangle import Rectangle
        from models.square import Square

        if cls is Rectangle:
            new = Rectangle(1, 1)
        elif cls is Square:
            new = Square(1)
        else:
            new = None
        new.update(**dictionary)
        return new

    @classmethod
    def save_to_file(cls, list_objs):
        """
        method to write the json string to a file
        """
        if list_objs is not None:
            list_objs = [o.to_dictionary() for o in list_objs]
        with open("{}.json".format(cls.__name__), "w", encoding="utf-8") as f:
            f.write(cls.to_json_string(list_objs))

    @staticmethod
    def from_json_string(json_string):
        """
        method to make list of json strings
        """
        if not json_string or json_string is None:
            return []
        return loads(json_string)

    @classmethod
    def load_from_file(cls):
        """
        method to deserialize the data
        """
        from os import path
        file = "{}.json".format(cls.__name__)
        if not path.isfile(file):
            return []
        with open(file, "r", encoding="utf-8") as f:
            return [cls.create(**d) for d in cls.from_json_string(f.read())]
