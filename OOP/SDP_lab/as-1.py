from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def calculate_perimeter(self):
        pass


class Color(ABC):
    @abstractmethod
    def fill(self):
        pass

class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def calculate_area(self):
        return 3.1416 * self.r * self.r

    def calculate_perimeter(self):
        return 2 * 3.1416 * self.r


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def calculate_area(self):
        return self.side * self.side

    def calculate_perimeter(self):
        return 4 * self.side


class Rectangle(Shape):
    def __init__(self, h, w):
        self.h = h
        self.w = w

    def calculate_area(self):
        return self.h * self.w

    def calculate_perimeter(self):
        return 2 * (self.h + self.w)   # fixed

class Red(Color):
    def fill(self):
        print("Filling with Red color")


class Green(Color):
    def fill(self):
        print("Filling with Green color")


class Blue(Color):
    def fill(self):
        print("Filling with Blue color")


#abs factory
class AbstractFactory(ABC):
    @abstractmethod
    def create_shape(self, shape_name):
        pass

    @abstractmethod
    def create_color(self, color_name):
        pass


#shape factory
class ShapeFactory(AbstractFactory):

    def create_shape(self, shape_name):
        if shape_name == "Circle":
            r = float(input("Enter radius: "))
            return Circle(r)

        elif shape_name == "Square":
            s = float(input("Enter side: "))
            return Square(s)

        elif shape_name == "Rectangle":
            h = float(input("Enter height: "))
            w = float(input("Enter width: "))
            return Rectangle(h, w)

        else:
            return None

    def create_color(self, color_name):
        return None


#color factory
class ColorFactory(AbstractFactory):

    def create_shape(self, shape_name):
        return None

    def create_color(self, color_name):
        if color_name == "Red":
            return Red()
        elif color_name == "Green":
            return Green()
        elif color_name == "Blue":
            return Blue()
        else:
            return None


#factory
class Factory:
    def createFactory(self, choice):
        if choice == "shape":
            return ShapeFactory()
        elif choice == "color":
            return ColorFactory()
        else:
            return None

def client():
    f = Factory()

    choice = input("Enter what you want (shape/color): ")

    factory = f.createFactory(choice)

    if choice == "shape":
        name = input("Enter shape (Circle/Square/Rectangle): ")
        obj = factory.create_shape(name)

        if obj:
            print("Area:", obj.calculate_area())
            print("Perimeter:", obj.calculate_perimeter())

    elif choice == "color":
        name = input("Enter color (Red/Green/Blue): ")
        obj = factory.create_color(name)

        if obj:
            obj.fill()

client()