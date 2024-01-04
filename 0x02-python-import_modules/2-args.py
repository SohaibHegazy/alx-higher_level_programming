#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    print("{} arguments:".format(len(argv)))
    for n in argv:
        print("n: {}".format(argv[n]))
