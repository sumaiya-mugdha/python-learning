class Burger:
    def prepare(self):
        pass
class Beefburger(Burger):
    def prepare(self):
        print("creating beefburger")
class Chickenburger(Burger):
    def prepare(self):
        print("creating Chickenburger")
class Veggieburger(Burger):
    def prepare(self):
        print("creating Veggieburger")

class Burgerfactory:
    def create_burger(self, burger_type):
        if burger_type.lower() == "beef":
            return Beefburger()
        elif burger_type.lower() == "chicken":
            return Chickenburger()
        elif burger_type.lower() == "veggie":
            return Veggieburger()
        else:
            return None

factory= Burgerfactory()
burger1= factory.create_burger("Beef")
burger2= factory.create_burger("Chicken")
burger3= factory.create_burger("Veggie")
burger1.prepare()
