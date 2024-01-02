#!/usr/bin/python3
def remove_char_at(str, n):
    if n < 0:
        cp_string = str
    else:
        cp_string = str[:n] + str[n + 1:]
    return (cp_string)
