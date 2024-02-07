#!/usr/bin/python3
""" Module to read a text file """


def read_file(filename=""):
    """
    function that reads a text file (UTF8) and prints it to stdout

    Args:
    filename: the file to be read

    Raise: Nothing

    Return: print the read file to stdout
    """
    with open(filename, encoding='utf-8') as f:
        print(f.read(), end="")
