#!/usr/bin/python3
"""Appends a string
at the end of a text file"""


def append_write(filename="", text=""):
    """returns no of characters added"""

    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
