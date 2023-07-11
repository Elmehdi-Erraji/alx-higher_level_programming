#!/usr/bin/python3
"""
9-rectangle module
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Represents a rectangle.
    Inherits from BaseGeometry.
    """
    def __init__(self, width, height):
        """
        init - Initializes an instance.
        Args:
            width: width of the rectangle
            height: height of the rectangle
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        area - returns area
        """
        return self.__width * self.__height

    def __str__(self):
        """
        str - returns rectangle description
        """
        return str("[Rectangle] {}/{}".format(self.__width, self.__height))
