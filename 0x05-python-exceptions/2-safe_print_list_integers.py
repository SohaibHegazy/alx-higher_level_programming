#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    i = 0
    p = 0

    while i is not x:
        try:
            print("{:d}".format(my_list[i]))
            i = i + 1
            p = p + 1
        except (ValueError, TypeError):
            i = i + 1
        except IndexError:
            none
    print()
    return p
