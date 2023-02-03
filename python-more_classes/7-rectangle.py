#!/usr/bin/python3
"""define a class rectangle"""

class Rectangle:
    """Rectangle class with width and height as arguments"""
    number_of_instances = 0
    print_symbol = '#'
    
    def __init__(self, width = 0, height = 0):
        """inialitization of the rectangle
            args:
                height: value of the height of the rectangle
                width: value of the width of the rectangle
        """
        Rectangle.number_of_instances += 1
        self.height = height
        self.width = width
    
    @property
    def height(self):
        """set value of height"""
        return self.__height
    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
    @property
    def width(self):
        """set value of width"""
        return self.__width
    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
    def area(self):
        return self.__height * self.__width
    def perimeter(self):
        if self.__height == 0 or self.__height == 0:
            return 0
        return self.__height * 2 + self.__width * 2
    def __str__(self):
        """return a string representation of the class object"""
        if self.__width == 0 or self.__height == 0:
            return ("")
        rectangle = []
        for i in range (self.__height):
            for j in range(self.__width):
                rectangle.append(Rectangle.print_symbol)
            if i == self.height -1:
                return "".join(rectangle)
            else:
                rectangle.append("\n")
    def __repr__(self):
        """returns a string that describe the pointer to of the object"""
        return "Rectangle({}, {})".format(self.width, self.height)
    def __del__(self):
        """delete the rectangle and print a message"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")