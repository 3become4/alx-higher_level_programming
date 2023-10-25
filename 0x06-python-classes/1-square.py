#!/usr/bin/python3
""" Class Square that defines a square by:
    Private instance attribute: size
    Instantiation with size (no type/value verification)
"""


class Square:
    def __init__(self, size):
        self.__size = size
