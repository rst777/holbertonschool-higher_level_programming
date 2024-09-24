#!/usr/bin/python3
"""Module définissant la classe BaseGeometry."""


class BaseGeometry:
    """Classe de base pour les formes géométriques."""

    def area(self):
        """
        Calcule l'aire de la forme géométrique.

        Raises:
            Exception: Cette méthode n'est pas implémentée
            dans la classe de base.
        """
        raise Exception("area() is not implemented")
