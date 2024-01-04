#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    arg_count = len(sys.argv) - 1
    if arg_count == 0:
        print("{} arguments.".format(arg_count))
    elif arg_count == 1:
        print("{} argument:".format(arg_count))
    else:
        print("{} arguments:".format(arg_count))
    for n in range(arg_count):
        print("{}: {}".format(n + 1, sys.argv[n + 1]))
