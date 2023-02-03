#!/usr/bin/python3
"""define a class square"""


class Square:
    """Square class with private instance attribute: size"""

    def __init__(self, size=0, position=(0, 0)):
        """args: size of the square"""
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        self.__position = value

    def my_print(self):
        """prints the square"""
        if self.__size == 0:
            print()
        else:
            for h in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for k in range(self.__position[0]):
                    print(' ', end='')
                for i in range(self.__size):
                    print("#", end='')
                print()
