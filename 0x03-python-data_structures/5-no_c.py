#!/usr/bin/python3

def no_c(my_string):
    new_string = ""
    for c in range(len(my_string)):
        if my_string[c] != 'c' and my_string[c] != 'C':
            new_string += my_string[c]
    return new_string
