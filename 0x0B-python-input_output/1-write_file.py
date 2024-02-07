#!/usr/bin/pyrhon3
""" Module to write to file """


def write_file(filename="", text=""):
    """
    function that writes a string to a text file (UTF8)
    and returns the number of characters written

    Args:
    filename: the file to write to
    text: the text to be written

    Raise: nothing

    Return: number of characters written
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
