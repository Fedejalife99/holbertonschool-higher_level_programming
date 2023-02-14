#!/usr/bin/python3
"""define a class rectangle that inherits from base class"""
from models.base import Base


class Rectangle(Base):
    """class Rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def height(self):
        """set the value of height"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def width(self):
        """set the value of width"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def x(self):
        """set the value of x"""
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """set the value of y"""
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """return the area of the Rectangle"""
        return self.__width * self.__height

    def display(self):
        """display the rectangle printing #"""
        for j in range(self.__height):
            for i in range(self.__width):
                print("#", end='')
            print()

    def __str__(self):
        return (f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - {self.__width}/{self.__height}")
    
    def update(self, *args):
        """update the Rectangle"""
        if len(args) is not 0:
            for i in range(1, len(args)):
                if i == 1:
                    self.__id = args[1]
                if i == 2:
                    self.__width = args[2]
                if i == 3:
                    self.__height = args[3]
                if i  == 4:
                    self.__x = args[4]
                if i == 5:
                    self.__y = args[5]
