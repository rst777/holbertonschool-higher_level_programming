#!/usr/bin/python3
"""Module contenant la classe MyList, une classe
personnalisée héritant de list."""


class MyList(list):
    """
    Une classe personnalisée qui hérite de la classe list.

    Cette classe ajoute une méthode pour imprimer la liste triée.
    """
    def print_sorted(self):
        """
        Imprime la liste triée en ordre ascendant.

        Cette méthode ne modifie pas la liste originale.
        """
        print(sorted(self))
