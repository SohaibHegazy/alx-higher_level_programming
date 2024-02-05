#!/usr/bin/python3

class MyList(list):
    """ class that inherets from list"""

    def print_sorted(self):
        """
        function that print the passed list sorted

        Args:
        self only

        Return: print the sorted list
        """
        print(sorted(self))
