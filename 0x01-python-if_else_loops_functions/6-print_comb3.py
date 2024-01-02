#!/usr/bin/python3
for n in range(9):
    for m in range(n, 10):
        if n < m and n < 8:
            print("{:d}{:d}".format(n, m), end=", ")
print("89")
