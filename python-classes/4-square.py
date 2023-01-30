#!/usr/bin/python3
"""define a class square"""
class Square:
    """Square class with private instance attribute: size"""

    def __init__(self, size=0):
        """args: size of the square"""
        self.__size = size
        
    @property
    def size(self):
        """get and set the value of size"""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """area of the square
            args: 
                area: the area of the square
        """
        return self.__size**2
