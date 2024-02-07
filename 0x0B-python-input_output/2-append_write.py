#!/usr/bin/python3
""" Module to append file """


def append_write(filename="", text=""):
    """
     function that appends a string at the end of a text file (UTF8)

     Args:
     filename: the file to be appended
     text: the text to append

     raise: Nothing

     return: number of characters added
     """
     with open('filename', 'a', encoding="utf-8") as f:
         return f.write(text)
