#!/usr/bin/python3
"""Module defining the Rectangle class"""


class Rectangle:
    """
    Class Rectange that defines a rectangle based on its height and width
    area and perimeter methodes included
    """
    def __init__(self, width=0, height=0):
        """initialize rectangle with private width and height"""
        self.width = width
        self.height = height

    def area(self):
        """"instance method that returns the area"""
        return self.width * self.height

    def perimeter(self):
        """instance method that returns the rectangle's perimeter"""
        if self.height == 0 or self.width == 0:
            return 0
        else:
            return 2 * self.width + 2 * self.height

    @property
    def width(self):
        """getter for width attribute"""
        return self.__width

    @property
    def height(self):
        """getter for height attribute"""
        return self.__height

    @width.setter
    def width(self, value):
        """setter for width attribute"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """setter for height attribute"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
