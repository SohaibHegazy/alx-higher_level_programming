#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    res = 0
    new_list = []
    i = 0

    while i is not list_length:
        try:
            res = my_list_1[i] / my_list_2[i]
            new_list.append(res)
        except ZeroDivisionError:
            print("division by 0")
            new_list.append(0)
            i = i + 1
            continue
        except (ValueError, TypeError):
            print("wrong type")
            new_list.append(0)
            i = i + 1
            continue
        except IndexError:
            print("out of range")
            new_list.append(0)
            i = i + 1
            continue
        finally:
            pass

    return new_list
