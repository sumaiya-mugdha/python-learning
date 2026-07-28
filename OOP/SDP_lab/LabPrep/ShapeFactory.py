from abc import ABC, abstractmethod

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

class shape_factory():
    def create_shape(self, choice):
        if choice == "circle":

            r = float(input("Give radius: "))
            return circle(r)
        
        elif choice == "square":
            s = input("Enter side")
            return square(s)
        
def client():
    choice = input("Enter choice: ")
    f = shape_factory()
    x = f.create_shape(choice)
    print(f"{choice} area: {x.area()}")
    print(f"{choice} perimeter: {x.perimeter()}")
    
client()

    