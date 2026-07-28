from abc import ABC, abstractmethod
class AbstractFactory(ABC):
    @abstractmethod
    def create_shape(self, choice):
        pass
    def create_color(self, choice):
        pass
#___________________________________________
class Color(ABC):
    @abstractmethod
    def fill(self):
        pass
class Red(Color):
    def fill(self):
        return "RED COLORED"
class Blue(Color):
    def fill(self):
        return "Blue COLORED"
    
class color_factory(AbstractFactory):
    def create_shape(self, choice):
        pass
    def create_color(self, choice):
        if choice == "red":
            return Red()
        elif choice == "blue":
            return Blue()
#___________________________________________-
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    def perimeter(self):
        pass
#concreteClass
class circle(Shape):
    def __init__(self, r):
        self.r = r 

        
    def area(self):
        return 3.1416 * self.r
    def perimeter(self):
        return 2*3.1416*self.r

class square(Shape):
    def area(self):
        pass
    def perimeter(self):
        pass

class shape_factory(AbstractFactory):
    def create_color(self, choice):
        pass
    def create_shape(self, choice):
        if choice == "circle":

            r = float(input("Give radius: "))
            return circle(r)
        
        elif choice == "square":
            s = input("Enter side")
            return square(s)
#________________________________________-_    

class MasterFactory:
    def create_factory(self, choice):
        if choice == "color":
            return color_factory()        
        elif choice == "shape":
            return shape_factory()


class client():
    def __init__(self):    
        choice = input("select factory: shape, color: ")
        factory = MasterFactory()
        f = factory.create_factory(choice)

        if choice == "shape":
            name = input("Enter shape: circle, square: ")
            x = f.create_shape(name)
            print(f"{name}: {x.area():.3f}")
            print(f"{name}: {x.perimeter():.3f}")
        elif choice == "color":
            name = input("Enter color: red, blue: ")
            x = f.create_color(name)

    
client()

    