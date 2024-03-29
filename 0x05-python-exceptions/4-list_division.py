#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    res = 0
    new_list = []
    i = 0

    while i is not list_length:
        try:
            res = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
            res = 0
        except (ValueError, TypeError):
            print("wrong type")
            res = 0
        except IndexError:
            print("out of range")
            res = 0
        finally:
            new_list.append(res)
            i = i + 1

    return new_list
