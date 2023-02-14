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
        return(f"[Square] ({id} {self.x}/{self.y} {self.height}")
