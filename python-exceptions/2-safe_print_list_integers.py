#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for i in range(x):
        try:
            # Essayer d'accéder et imprimer l'élément courant
            if isinstance(my_list[i], int):
                print("{:d}".format(my_list[i]), end="")
                count += 1
        except IndexError:
            # Lever une exception si l'index est hors de portée
            raise IndexError("Index out of range.")
    print()
    return count
