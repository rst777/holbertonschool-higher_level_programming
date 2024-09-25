#!/usr/bin/python3
"""Module définissant la classe BaseGeometry."""


class BaseGeometry:
    """Classe de base pour les formes géométriques."""
    def area(self):
        raise Exception("area() n'est pas implémentée")
        """
        Calcule l'aire de la forme géométrique.

        Raises:
            Exception: Cette méthode n'est pas implémentée
            dans la classe de base.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Valide que la valeur est un entier positif.

        Args:
            name (str): Le nom de la variable à valider.
            value: La valeur à valider.

        Raises:
            TypeError: Si la valeur n'est pas un entier.
            ValueError: Si la valeur est inférieure ou égale à 0.
        """
        if not isinstance(value, int):
            raise TypeError("{} must be integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
