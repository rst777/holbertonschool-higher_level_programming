#!/usr/bin/env python3
from abc import ABC, abstractmethod
import math

# Classe abstraite Shape


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

# Classe Circle


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

# class Rectangle


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

# Fonction shape_info


def shape_info(shape):
    print(f"Area : {shape.area():}")
    print(f"Perimeter : {shape.perimeter():}")

# Test


if __name__ == "__main__":
    # Test avec un cercle
    circle = Circle(5)
    print("information du cercle :")
    shape_info(circle)

    # Test avec un rectangle
    rectangle = Rectangle(4, 7)
    print("Information du rectangle :")
    shape_info(rectangle)
