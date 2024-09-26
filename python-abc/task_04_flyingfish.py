#!/usr/bin/env python3

# Définir la classe Fish
class Fish:
    def swim(self):
        print("The fish is swimming")

    def habitat(self):
        print("The fish lives in water")

# Définir la classe Bird


class Bird:
    def fly(self):
        print("The bird is flying")

    def habitat(self):
        print("The bird lives in the sky")

# Définir la classe FlyingFish qui hérite de Fish et Bird


class FlyingFish(Fish, Bird):
    def fly(self):
        print("The flying fish is soaring!")

    def swim(self):
        print("The flying fish is swimming!")

    def habitat(self):
        print("The flying fish lives both in water and the sky!")

# Tester l'héritage et les méthodes


flying_fish = FlyingFish()
