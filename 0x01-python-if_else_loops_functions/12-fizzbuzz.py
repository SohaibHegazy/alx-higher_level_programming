#!/usr/bin/python3
def fizzbuzz():
    for n in range(101):
        if n % 3 == 0 and n % 5 == 0:
            print("FizzBuzz", end="")
        elif n % 3 == 0 and n % 5 != 0:
            print("Fizz", end="")
        elif n % 3 != 0 and n % 5 == 0 and n != 100:
            print("Buzz", end="")
        elif n == 100:
            print("Buzz")
        else:
            print("{:d}".format(n), end="")
