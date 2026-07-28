from abc import ABC, abstractmethod

class FlatShape(ABC):
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass

class Circle2D(FlatShape):
    def __init__(self, radius):
        self.radius = radius
    def calculate_area(self):
        area= 3.1415*self.radius * self.radius
        return area
    def calculate_perimeter(self):
        perimeter= 3.1415 * 2 * self.radius
        return perimeter

class Square2D(FlatShape):
    def __init__(self, a):
        self.a = a
    def calculate_area(self):
        area= self.a * self.a
        return area
    def calculate_perimeter(self):
        perimeter= 4* self.a
        return perimeter

class SolidShape(ABC):
    @abstractmethod
    def surface_area(self):
        pass
    @abstractmethod
    def volume(self):
        pass

class Sphere3D(SolidShape):
    def __init__(self, radius):
        self.radius = radius
    def surface_area(self):
        area= 4*3.1415 * self.radius* self.radius
        return area
    def volume(self):
        vol= (4/3)*3.1415* self.radius * self.radius* self.radius
        return vol

class Cube3D(SolidShape):
    def __init__(self, a):
        self.a = a
    def surface_area(self):
        area= 6 * self.a * self.a
        return area
    def volume(self):
        vol= self.a* self.a * self.a
        return vol

class ShapeFactory(ABC):
    @abstractmethod
    def create_flat_shape(self):
        pass
    @abstractmethod
    def create_solid_shape(self):
        pass




class CircleSphereFactory(ShapeFactory):

    def create_flat_shape(self):
        radius = float(input("enter radius: "))
        return Circle2D(radius)
    def create_solid_shape(self):
        radius = float(input("enter radius: "))
        return Sphere3D(radius)

class CircleSphereFactory(ShapeFactory):
    def create_flat_shape(self):
        a = int(input("enter a: "))
        return Square2D(a)

    def create_solid_shape(self):
        a = int(input("enter a: "))
        return Cube3D(a)

class FactoryProducer:


    def create_sphere(self):
        radius = input("enter radius: ")
    def create_Flatshape(self, shape):
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