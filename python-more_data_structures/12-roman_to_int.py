#!/usr/bin/python3
def roman_to_int(roman_string):
#vérifie si l'entrée est valide
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
# Dictionnaire des valeurs des chiffres romains
    roman_values = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
        }
    total = 0
    prev_value = 0

    # Parcours de la chaîne de droite à gauche
    for char in reversed(roman_string):
        # Récupère la valeur du caractère romain actuel
        value = roman_values.get(char, 0)

        # Si la valeur actuelle est inférieure à la valeur précédente,
        # on la soustrait
        if value < prev_value:
            total -= value
        else:
            # Sinon, on l'ajoute au total
            total += value

        # Met à jour la valeur précédente
        prev_value = value
    return total
