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

    def to_json(self):
        """
        Method to represent attr. of Student in dict
        """
        return self.__dict__
