# ---- Polygon Area Calculator ----

from abc import ABC, abstractmethod


# Parent class
class Polygon(ABC):

    # Abstract method
    @abstractmethod
    def calculate_area(self):
        pass


# Child class - Rectangle
class Rectangle(Polygon):

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width


# Child class - Triangle
class Triangle(Polygon):

    def __init__(self, base, height):
        self.base = base
        self.height = height

    def calculate_area(self):
        return 0.5 * self.base * self.height


# Create objects
rectangle = Rectangle(10, 5)
triangle = Triangle(8, 6)

# Display areas
print("Area of Rectangle:", rectangle.calculate_area())
print("Area of Triangle:", triangle.calculate_area())
