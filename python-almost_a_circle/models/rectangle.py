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
        if self.width == 0 or self.height == 0:
            print("")
            return
        [print("") for y in range(self.y)]
        for h in range(self.height):
            [print(" ", end="") for x in range(self.x)]
            [print("#", end="") for w in range(self.width)]
            print("")

    def __str__(self):
        return (f"[Rectangle] ({self.id}) {self.__x}/{self.__y} -\
            {self.__width}/{self.__height}")

    def update(self, *args, **kwargs):
        """update the Rectangle"""
        i = 1
        if len(args) != 0:
            for argument in args:
                if i == 1:
                    self.id = argument
                if i == 2:
                    self.__width = argument
                if i == 3:
                    self.__height = argument
                if i == 4:
                    self.__x = argument
                if i == 5:
                    self.__y = argument
                i += 1
        elif len(kwargs) != 0:
            for key, value in kwargs.items():
                    if key == 'id':
                        self.id = value
                    if key == 'width':
                        self.__width = value
                    if key == 'height':
                        self.__height = value
                    if key == 'x':
                        self.__x = value
                    if key == 'y':
                        self.__y = value
        else:
            pass

    def to_dictionary(self):
        """return a dictionary representation of the square"""
        new_dict = {'id': self.id,
                    'width': self.width,
                    'height': self.height,
                    'x': self.x,
                    'y': self.y}
        return new_dict
