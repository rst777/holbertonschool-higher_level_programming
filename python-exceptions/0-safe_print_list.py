#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    for i in range(x):
        try:
            # Essayer d'accéder et imprimer l'élément courant
            print(my_list[i], end="")
            count += 1
        except IndexError:
            # Arrêter la boucle si l'index est hors des limites de la liste
            break

    print()  # Passe à la ligne suivante après les éléments imprimés
    return count
