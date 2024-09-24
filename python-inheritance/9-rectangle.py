#!/usr/bin/python3
"""
Ce module définit une classe Rectangle qui hérite de BaseGeometry.
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Une classe pour représenter un rectangle.
    Hérite de BaseGeometry.
    """
    def __init__(self, width, height):
        """
        Initialise un nouveau Rectangle.

        Args:
            width (int): La largeur du rectangle.
            height (int): La hauteur du rectangle.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Calcule l'aire du rectangle.

        Returns:
            int: L'aire du rectangle.
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Retourne une représentation sous forme de chaîne du rectangle.

        Returns:
            str: Une chaîne au format [Rectangle] <largeur>/<hauteur>
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    def __rep__(self):
        """
        Retourne une représentation sous forme de chaîne du rectangle.

        Returns:
            str: Identique à __str__
        """
        return self.__str__()

    if __name__ == "__main__":
        r = Rectangle(3, 5)
        print(r)
        print(r.area())
