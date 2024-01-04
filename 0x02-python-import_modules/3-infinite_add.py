#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    arg_count = len(sys.argv) - 1
    sum = 0
    for n in range(arg_count):
        sum = sum + int(sys.argv[n + 1])
    print("{}".format(sum))
