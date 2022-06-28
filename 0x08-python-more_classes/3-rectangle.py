#!/usr/bin/python3
"""Modify 2-rectangle
Defines a Rectangle class.
"""


class Rectangle:
    """Rectangle class with private instance
    attributes: width and height."""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    def __str__(self):
        total = ""
        if self.__height == 0 or self.width == 0:
            return total
        rec_str = total
        for i in range(self.__height):
            for j in range(self.__width):
                rec_str += '#'
            rec_str += '\n'
        return rec_str[:-1]

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        """initializes the rectangle's width"""
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        """initializes the rectangle's height"""
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return (2 * self.__width) + (2 * self.__height)
