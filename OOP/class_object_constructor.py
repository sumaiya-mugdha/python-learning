class Student:
    school = "ar Soup"          #attrubite
    def __init__(self,fullname):       #contructor- self-> the object, fullname-> parameter the object pass
        self.name = fullname           #create name variable and store the fullname here
        print("We are adding new student names...")

    #method-always pass self
    @staticmethod
    def welcome(self):
        print("Welcome to the student class")   ##static method because no self used

s1 = Student("alu") ##creating object and passing values/parameter
print(s1.name, Student.school)      ##call and show the name who store the fullname ### calling attribute
s2 = Student("potol")
print(s2.name, Student.school)
s3 = Student("gajor")
print(s3.name, Student.school)
s4 = Student("mula")
print(s4.name, Student.school)
s4.welcome()                     ##calling by the object

###practice
class Stu:
    def __init__(self,name,mark_of_chemistry,mark_of_physics,mark_of_biology):
        self.stuname = name
        self.chem = mark_of_chemistry
        self.phys = mark_of_physics
        self.bio = mark_of_biology
    def avarage(self):
        return (self.chem + self.phys + self.bio)/3
s1=Stu("simi", 100,49,89)
print(s1.stuname, s1.chem, s1.phys, s1.bio, s1.avarage())


###practice
class BankAccount:
    name= "Mew"
    balance= 1000
    def deposit(self,balance):
        self.balance=balance+ self.balance
        return print(self.balance)
    def withdraw(self,amount):
        self.balance= self.balance - amount
        return print(self.balance)
    def show_balance(self):
        print (self.balance)
acc= BankAccount()
acc.deposit(500)
acc.withdraw(400)
acc.show_balance()




