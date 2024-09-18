#!/usr/bin/python3
"""
Module that defines a Rectangle class.
"""

class Rectangle:
    """
    A class to represent a rectangle.
    Class Attributes:
        number_of_instances (int): Tracks the number of
        instances created or deleted.
    print_symbol: Symbol used for string representation of the rectangle.
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initialize the rectangle with a given width and height.
        """
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

    @property
    def height(self):
        """
        Getter for the height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter for the height of the rectangle.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        """
        Getter for the width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter for the width of the rectangle.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def area(self):
        """
        Calculate the area of the rectangle.
        """
        return self.__height * self.__width

    def perimeter(self):
        """
        Calculate the perimeter of the rectangle.

        Returns:
            int: The perimeter, or 0 if either the width or height is 0.
        """
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Return a string representation of the rectangle using the character(s)
        stored in print_symbol.
        """
        if self.__height == 0 or self.__width == 0:
            return ("")
        
        if isinstance(self.print_symbol, list):
            symbol = ", ".join(map(str, self.print_symbol))
        else:
            symbol = str(self.print_symbol)

        return '\n'.join([symbol * self.__width for _ in range(self.__height)])

    def __repr__(self):
        """
        Return a string representation that can recreate a new instance
        of the rectangle using eval().
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """
        Print a message when an instance of Rectangle is deleted.
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
