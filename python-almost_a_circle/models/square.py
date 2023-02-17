#!/usr/bin/python3
"""creates a class Square that inherits from rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """class Square"""
    def __init__(self, size, x=0, y=0, id=None):
        """new Square"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """get and set the value of the dimentions of the square"""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        """return a representation of the square"""
        return(f"[Square] ({self.id}) {self.x}/{self.y} {self.height}")

    def update(self, *args, **kwargs):
        """update the square"""
        i = 1
        if args and len(args) != 0:
            for argument in args:
                if i == 1:
                    self.id = argument
                if i == 2:
                    self.size = argument
                if i == 3:
                    self.x = argument
                if i == 4:
                    self.y = argument
                i += 1
        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                    if key == 'id':
                        self.id = value
                    if key == 'size':
                        self.size = value
                    if key == 'x':
                        self.x = value
                    if key == 'y':
                        self.y = value

    def to_dictionary(self):
        """return a dictionary representation of the square"""
        new_dict = {'id': self.id,
                    'size': self.size,
                    'x': self.x,
                    'y': self.y}
        return new_dict
