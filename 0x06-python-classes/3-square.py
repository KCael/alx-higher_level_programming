#!/usr/bin/python3
"""Defines Area of a square"""


class square():
    """square class with size and proper validation"""

    def __init__(self, size=0):
        if(type(size) is not int):
            raise TypeError("size must be a integer")
        elif(size < 0):
            raise ValueError("size must be >= 0")
        self._size = size

    """returns the current square area"""

    def area(self):
        return self._size ** 2
