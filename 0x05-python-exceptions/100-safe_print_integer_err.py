#!/usr/bin/python3

def safe_print_integer_err(value):
    bool = True

    try:
        print("{:d}".format(value))
    except Exception as er:
        print("Exception:", er, file=sys.stderr)
        bool = False

    return bool
