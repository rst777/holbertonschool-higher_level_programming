#!/usr/bin/python3
"""
Module that defines a Square class.
"""


class Square():
    """
    A class to represent a square.

    Attributes:
        size (int): The size of the square's sides.
    """
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        """
        Getter for the size of the square.

        Returns:
            int: The current size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):

        """
        Setter for the size of the square.

        Args:
            value (int): The new size of the square.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculate the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Print the square using the character '#'.
        If the size is 0, print an empty line.

        Prints:
            A square of size `size` using '#'.
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.size)
