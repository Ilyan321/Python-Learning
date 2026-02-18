# Inheritance

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def display(self):
        print(self.name,self.age)

class Ilyan(Person):
    def display(self):
        print("Fron ilyan class",self.name,self.age)
    

p1=Person("Ilyan",19)
p1.display()
p2=Ilyan("Damon",165)
p2.display()