#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arg_c = len(sys.argv) - 1
    if arg_c == 0:
        print("{} arguments.".format(arg_c)))
    elif arg_c == 1:
        print("{} argument:".format(arg_c)))
    else:
        print("{} arguments:".format(arg_c)))
    for n in range(arg_c):
        print("n + 1: {}".format(sys.argv[n + 1]))
