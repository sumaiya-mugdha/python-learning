from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass
    @abstractmethod
    def calculate_perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def calculate_area(self):
        area= 3.1415*self.radius * self.radius
        return area
    def calculate_perimeter(self):
        perimeter= 3.1415 * 2 * self.radius
        return perimeter

class square(Shape):
    def __init__(self, a):
        self.a = a
    def calculate_area(self):
        area= self.a * self.a
        return area
    def calculate_perimeter(self):
        perimeter= 4* self.a
        return perimeter

class rectangle(Shape):
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def calculate_area(self):
        area= self.a * self.b
        return area
    def calculate_perimeter(self):
        perimeter= self.a* self.b
        return perimeter

class ShapeFactory:
    def create_shape(self, shape):
        if shape == "rectangle":
            a= input("enter height: ")
            b= input("enter width: ")
            return rectangle(int (a),int (b))
        elif shape == "circle":
            radius = input("enter radius: ")
            return Circle(float(radius))
        elif shape == "square":
            a = input("enter height: ")
            return square(int(a))
        else:
            print("enter correct shape")
factory=ShapeFactory()
shape=factory.create_shape("rectangle")
print(shape.calculate_area())