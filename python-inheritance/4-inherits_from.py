#!/usr/bin/python3
"""Module contenant la fonction inherits_from."""


def inherits_from(obj, a_class):
    """
    Vérifie si un objet est une instance d'une classe qui hérite de a_class.

    Args:
        obj: L'objet à vérifier.
        a_class: La classe à comparer.

    Returns:
        bool: True si obj est une instance d'une sous-classe de a_class,
              False sinon ou si obj est une instance directe de a_class.
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
