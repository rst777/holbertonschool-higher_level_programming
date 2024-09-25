#!/usr/bin/env python3

class VerboseList(list):
    def append(self, item):
        super().append(item)  # Appel à la méthode append de la classe list
        print(f"Added {[item]} to the list.")

    def extend(self, items):
        super().extend(items)  # Appel à la méthode extend de la classe list
        print(f"Extended the list with {[len(items)]} items.")

    def remove(self, item):
        print(f"Removed {[item]} from the list.")
        super().remove(item)  # Appel à la méthode remove de la classe list

    def pop(self, index=-1):
        item = self[index]  # Récupérer l'élément avant de le retirer
        print(f"Popped {[item]} from the list.")
        return super().pop(index)  # Appel à la méthode pop de la classe list
