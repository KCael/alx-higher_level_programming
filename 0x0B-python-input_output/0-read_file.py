#!/usr/bin/python3
"""Reads a text file"""


def read_file(filename=""):
    """reads UTF* and 
    prints to stdout"""

    with open(filename, encoding="utf-8") as f:
        text = f.read()
        print(text, end="")
