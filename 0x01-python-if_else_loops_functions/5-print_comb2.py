#!/usr/bin/python3
for n in range(99):
    d1 = n / 10
    d2 = n % 10
    print("{:d}{:d}".format(d1, d2), end=", ")

print("99")
