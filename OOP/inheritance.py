#method overloading
class Human:
    def eat(self):
        print("eat HUMAN EAT")
class Boy(Human):
    def eat(self):
        print("eat boy eats")

boy=Boy()
boy.eat()

#single inheritance
class Car:
    @staticmethod
    def start():
        print("Car is starting...")
    @staticmethod
    def stop():
        print("Car is stopping...")
class ToyotaCar(Car):
    def __init__(self,name):
        self.name=name

#multilevel
class FortuneCar(ToyotaCar):
    def __init__(self,type):
        self.type=type
car2 = FortuneCar("dissel")
car2.stop()

#another example
class Animal:
    def eat(self):
        print("eating")

class Dog(Animal):

    def run(self):
        print("Dog is running")

class Cat(Animal):
    def run(self):
        print("Cat is running")
dog=Dog()
dog.run()
dog.eat()
cat=Cat()
cat.run()
cat.eat()




































