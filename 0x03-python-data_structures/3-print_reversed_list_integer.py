#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    if not my_list:
        return None
    a = my_list.reverse
    for n in a:
        print("{:d}".format(n))
