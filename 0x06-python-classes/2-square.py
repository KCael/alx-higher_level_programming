#!/usr/bin/python3
"""Defines an empty square."""


class Square:
    """Represents a square."""

    def __init__(self, size=0):
        """Initializes the data.
        Private instance attribute: size.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
