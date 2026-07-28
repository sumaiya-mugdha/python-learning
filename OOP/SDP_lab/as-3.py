from abc import ABC, abstractmethod
import math

class FlatShape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class SolidShape(ABC):
    @abstractmethod
    def volume(self):
        pass

    @abstractmethod
    def surface_area(self):
        pass


#2d
class CircleFlat(FlatShape):
    def __init__(self, radius: float):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius


class SquareFlat(FlatShape):
    def __init__(self, side: float):
        self.side = side

    def area(self):
        return self.side ** 2

    def perimeter(self):
        return 4 * self.side


#3d
class SphereSolid(SolidShape):
    def __init__(self, radius: float):
        self.radius = radius

    def volume(self):
        return (4/3) * math.pi * self.radius ** 3

    def surface_area(self):
        return 4 * math.pi * self.radius ** 2


class CubeSolid(SolidShape):
    def __init__(self, side: float):
        self.side = side

    def volume(self):
        return self.side ** 3

    def surface_area(self):
        return 6 * self.side ** 2




class BaseFactory(ABC):

    @abstractmethod
    def make_2d(self, type, size):
        pass

    @abstractmethod
    def make_3d(self, type, size):
        pass



class TwoDFactory(BaseFactory):

    def make_2d(self, type, size):
        if type == "circle":
            return CircleFlat(size)
        elif type == "square":
            return SquareFlat(size)

    def make_3d(self, type, size):
        return None


class ThreeDFactory(BaseFactory):

    def make_2d(self, type, size):
        return None

    def make_3d(self, type, size):
        if type == "sphere":
            return SphereSolid(size)
        elif type == "cube":
            return CubeSolid(size)



class FactoryProvider:

    @staticmethod
    def get_factory(kind):
        if kind == "2D":
            return TwoDFactory()
        elif kind == "3D":
            return ThreeDFactory()



if __name__ == "__main__":

    # 2D Shapes
    factory2d = FactoryProvider.get_factory("2D")

    circle = factory2d.make_2d("circle", 5)
    square = factory2d.make_2d("square", 4)

    print("2D Shapes:")
    print("Circle Area:", circle.area())
    print("Circle Perimeter:", circle.perimeter())
    print("Square Area:", square.area())
    print("Square Perimeter:", square.perimeter())

    # 3D Shapes
    factory3d = FactoryProvider.get_factory("3D")

    sphere = factory3d.make_3d("sphere", 5)
    cube = factory3d.make_3d("cube", 4)

    print("\n3D Shapes:")
    print("Sphere Volume:", sphere.volume())
    print("Sphere Surface Area:", sphere.surface_area())
    print("Cube Volume:", cube.volume())
    print("Cube Surface Area:", cube.surface_area())