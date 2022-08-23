#!/usr/bin/python3
for c in range(ord('z'), ord('a') - 1, -1):
    print("{:c}{:s}".format(c, chr(c - 32)), end="")
