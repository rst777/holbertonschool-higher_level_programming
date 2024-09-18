#!/usr/bin/python3
"""
Module that defines a Square class.
"""


class Square():
    """
    A class to represent a square.

    Attributes:
        __size (int): The size of the square's sides (default is 0).
    """
    def __init__(self, size=0):

        """
        Initialize the square with a given size.

        Args:
            size (int): The size of the square's sides
            (must be a non-negative integer).

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Calculate the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2
