#!/usr/bin/python3
"""
Ce module définit une classe Rectangle qui hérite d'une BaseGeometry .
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Une classe représentant un rectangle.

    Cette classe hérite de BaseGeometry et implémente
    un rectangle avec une largeur et une hauteur.
    """
    def __init__(self, width, height):
        """
        Initialise un nouveau Rectangle.

        Args:
            width (int): La largeur du rectangle.
            height (int): La hauteur du rectangle.

        Raises:
            TypeError: Si width ou height n'est pas un entier.
            ValueError: Si width ou height est inférieur ou égal à 0.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
