#!/usr/bin/python3
"""class square that inherits from rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """create a square class"""

    def __init__(self, size):
        """initialize a square"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
        self.__width = size
        self.__height = size

    def area(self):
        return self.__width * self.__height
