#!/usr/bin/python3
"""
Ce module définit une classe Square qui hérite de Rectangle.
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Une classe pour représenter un carré.
    Hérite de Rectangle.
    """

    def __init__(self, size):
        """
        Initialise un nouveau carré.

        Args:
            size (int): La taille du côté du carré.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """
        Calcule l'aire du carré.

        Returns:
            int: L'aire du carré.
        """
        return self.__size ** 2

    def __str__(self):
        """
        Retourne une représentation sous forme de chaîne du carré.

        Returns:
            str: Une chaîne au format [Square] <width>/<height>
        """
        return "[Square] {}/{}".format(self.__size, self.__size)

    def __repr__(self):
        """
        Retourne une représentation sous forme de chaîne du carré.

        Returns:
            str: Identique à __str__
        """
        return self.__str__()


if __name__ == "__main__":
    s = Square(13)
    print(s)
    print(s.area())
