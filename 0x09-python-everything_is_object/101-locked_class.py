#!/usr/bin/python3
""" define locked class """


class LockedClass:
    """
    prevents the user from dynamically creating new instance attributes,
    except if the new instance attribute is called first_name.
    no class or object attribute added
    """
    __name__ = ["first_name"]
