#!/usr/bin/python3
"""
Module that defines a Square class.
"""


class Square():
    """
    A class that defines a square.

    This class allows the creation of square objects with a given size
    and position. It provides methods to calculate the area and print
    the square.

    Attributes:
        size (int): The size of the square (default is 0).
        position (tuple): The position of the square as a tuple
        of 2 positive integers (default is (0, 0)).
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize the square with a given size and position.

        Args:
            size (int): The size of the square's sides.
            position (tuple): The position of the square.
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter for the position of the square.

        Args:
            value (tuple): The new position of the square.

        Raises:
            TypeError: If the value is not a tuple of 2 positive integers.
        """
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Calculate the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Print the square using the '#' character.

        If the size is 0, it prints an empty line.
        The position is used to add space before the square.
        """
        if self.__size == 0:
            print("")
            return

        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")
