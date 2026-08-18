from abc import ABC, abstractmethod


# =========================
# Abstract Product: 2D Shape
# =========================

class FlatShape(ABC):

    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def calculate_perimeter(self):
        pass


# =========================
# Concrete Products: 2D
# =========================

class Circle2D(FlatShape):

    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.1415 * self.radius * self.radius

    def calculate_perimeter(self):
        return 2 * 3.1415 * self.radius


class Square2D(FlatShape):

    def __init__(self, a):
        self.a = a

    def calculate_area(self):
        return self.a * self.a

    def calculate_perimeter(self):
        return 4 * self.a


# =========================
# Abstract Product: 3D Shape
# =========================

class SolidShape(ABC):

    @abstractmethod
    def surface_area(self):
        pass

    @abstractmethod
    def volume(self):
        pass


# =========================
# Concrete Products: 3D
# =========================

class Sphere3D(SolidShape):

    def __init__(self, radius):
        self.radius = radius

    def surface_area(self):
        return 4 * 3.1415 * self.radius * self.radius

    def volume(self):
        return (4 / 3) * 3.1415 * self.radius ** 3


class Cube3D(SolidShape):

    def __init__(self, a):
        self.a = a

    def surface_area(self):
        return 6 * self.a * self.a

    def volume(self):
        return self.a ** 3


# =========================
# Abstract Factory
# =========================

class ShapeFactory(ABC):

    @abstractmethod
    def create_flat_shape(self):
        pass

    @abstractmethod
    def create_solid_shape(self):
        pass


# =========================
# Concrete Factory 1
# Creates Circle + Sphere
# =========================

class CircleSphereFactory(ShapeFactory):

    def create_flat_shape(self):
        radius = float(input("Enter circle radius: "))
        return Circle2D(radius)

    def create_solid_shape(self):
        radius = float(input("Enter sphere radius: "))
        return Sphere3D(radius)


# =========================
# Concrete Factory 2
# Creates Square + Cube
# =========================

class SquareCubeFactory(ShapeFactory):

    def create_flat_shape(self):
        a = float(input("Enter square side: "))
        return Square2D(a)

    def create_solid_shape(self):
        a = float(input("Enter cube side: "))
        return Cube3D(a)


# =========================
# MAIN PROGRAM
# =========================

print("Choose factory:")
print("1. Circle + Sphere")
print("2. Square + Cube")

choice = input("Enter choice: ")

if choice == "1":
    factory = CircleSphereFactory()

elif choice == "2":
    factory = SquareCubeFactory()

else:
    print("Invalid choice")
    exit()


print("\nChoose shape:")
print("1. 2D Shape")
print("2. 3D Shape")

shape_choice = input("Enter choice: ")


if shape_choice == "1":

    shape = factory.create_flat_shape()

    print("Area:", shape.calculate_area())
    print("Perimeter:", shape.calculate_perimeter())


elif shape_choice == "2":

    shape = factory.create_solid_shape()

    print("Surface Area:", shape.surface_area())
    print("Volume:", shape.volume())


else:
    print("Invalid choice")