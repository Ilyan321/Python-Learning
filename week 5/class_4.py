# Inheritance

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def display(self):
        print(self.name,self.age)
class Ilyan(Person):       #inherited fron Person

    def __init__(self,name,age,height):
        super().__init__(name,age)     # Super() tells it to run 1st parent function first
        self.height=height
    def display(self):
        print("Fron ilyan class",self.name,self.age,self.height)

class Student(Person):
    def display(self,greet="Hello"):
        print(greet,"From Student class",self.name,self.age)

    
def Display(Person):
        print("From Student class",Person.name,Person.age)

# p1=Person("Ilyan",19)
# p1.display()
p2=Ilyan("Damon",165,7)
Display(p2)
p3=Student("Elijah",1065)
Display(p3)