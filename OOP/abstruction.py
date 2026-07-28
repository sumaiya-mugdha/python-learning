#abstruction
from abc import ABC, abstractmethod
from os import name


class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        print("Bark")
class Cat(Animal):
    def sound(self):
        print("Cat")

dog = Dog()

dog.sound()

#interface
class Employee(ABC):
    def __init__(self, name):
        self.name=name
        print (name+" check in")

    def check_in(self):
        print("check in")
    @abstractmethod
    def work(self):
        pass
class Delivaryboy(Employee):
    def work(self):
        print("delivaring food")

class chef(Employee):

    def work(self):
        print("cooking food")
boy=Delivaryboy("Ramim")
cook=chef("karim")
boy.work()
cook.work()


#interface
class Notification(ABC):
    @abstractmethod
    def send(self, massage):
        pass

class Email(Notification):
    def send(self, massage):
        print("Email sent"+massage)


class SMS(Notification):
    def send(self, massage):
        print("SMS sent "+massage)
email=Email()
email.send("hwllo")
sms=SMS()
sms.send("hello")
