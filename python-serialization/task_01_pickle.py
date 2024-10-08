#!/usr/bin/env python3
"""Learn how to serialize and deserialize custom Python
objects using the pickle module.
"""

import pickle


class CustomObject:
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """Sérialise l'objet dans un fichier
        avec gestion des exceptions."""
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
        except Exception as e:
            print(f"Erreur lors de la sérialisation : {e}")
            return None

    @classmethod
    def deserialize(cls, filename):
        try:
            with open(filename, 'rb') as file:
                obj = pickle.load(file)
            print()
            return obj
        except (FileNotFoundError, pickle.UnpicklingError) as e:
            print(f"Erreur lors de la désérialisation : {e}")
            return None
