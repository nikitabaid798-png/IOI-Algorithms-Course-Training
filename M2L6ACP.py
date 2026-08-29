# ---- Polygon Area Calculator ----

class Polygon:

    def __init__(self, name):
        self.__name = name

    # Encapsulation: getter
    def get_name(self):
        return self.__name

    # Polymorphism: same method name in different classes
    def calculate_area(self):
        return 0


class Rectangle(Polygon):

    def __init__(self, length, width):
        super().__init__("Rectangle")
        self.__length = length
        self.__width = width

    def calculate_area(self):
        return self.__length * self.__width


class Triangle(Polygon):

    def __init__(self, base, height):
        super().__init__("Triangle")
        self.__base = base
        self.__height = height

    def calculate_area(self):
        return 0.5 * self.__base * self.__height


# Create objects
rectangle = Rectangle(10, 5)
triangle = Triangle(8, 6)

# Polymorphism
print(rectangle.get_name(), "area:", rectangle.calculate_area())
print(triangle.get_name(), "area:", triangle.calculate_area())
