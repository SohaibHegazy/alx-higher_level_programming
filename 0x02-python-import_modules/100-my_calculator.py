#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div

    arg_count = len(sys.argv) - 1
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    op = sys.argv[2]
    if arg_count != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    if sys.argv[2] == "+":
        print("{} + {} = {}".format(a, b, add(a, b)))
    elif sys.argv[2] == "-":
        print("{} - {} = {}".format(a, b, sub(a, b)))
    elif sys.argv[2] == "*":
        print("{} * {} = {}".format(a, b, mul(a, b)))
    elif sys.argv[2] == "/":
        print("{} / {} = {}".format(a, b, div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
