#!/usr/bin/python3
""" Module to create dict representation of a class"""


class Student:
    """ 
    class with public instance attr.
    first_name, last_name, age
    """
    def __init__(self, first_name, last_name, age):
        """
        constructor of class student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Method to represent attr. of Student in dict
        """
        try:
            for attr in attrs:
                if type(attr) is not str:
                    return self.__dict__
        except Exception:
            return self.__dict__

        my_dict = dict()
        for key, value in self.__dict__.items():
            if key in attrs:
                my_dict[key] = value
        return my_dict

    def reload_from_json(self, json):
        """
        Method to replace all attrs of Student class
        with attrs from json
        """
        for key, value in json.items():
            if key in self.__dict__:
                self.__dict__[key] = value
