#!/usr/bin/env python3

"""
This module defines the class SwimMixin
and FlyMixim
"""
# Définir le mixin SwimMixin
class SwimMixin:

    pass

    def swim(self):
        print("The creature swims !")

# Définir le mixin FlyMixin


class FlyMixin:

    pass

    def fly(self):
        print("The creature flies !")

# Définir la classe Dragon qui hérite de SwimMixin et FlyMixin


class Dragon(SwimMixin, FlyMixin):

    pass

    def roar(self):
        print("The dragon roars !")

# Tester les capacités du dragon


draco = Dragon()

# Appeler les méthodes
draco.swim()  # Affiche "The creature swims!"
draco.fly()   # Affiche "The creature flies!"
draco.roar()  # Affiche "The dragon roars!"
