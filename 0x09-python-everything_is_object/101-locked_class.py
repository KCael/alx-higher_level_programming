#!/usr/bin/python3
"""
A class that prevents dynamic attributes creation

"""

class LockedClass():

    __slots__ = ['first_name']

    def __init__(self):
        self.first_name = first_name
