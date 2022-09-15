#!/usr/bin/python3
"""Defines a square"""


class Square():
    """square class with size and proper validation"""

    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        return (self.__size)

    @size.setter
    def size(self, value):
        if(type(value) is not int):
            raise TypeError("size must be an integer")
        elif(value < 0):
            raise ValueError("size must be >= 0")
        self.__size = value

    """returns current area of the square"""

    def area(self):
        return (self.__size * self__size)
