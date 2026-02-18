# Inheritance

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def display(self):
        print(self.name,self.age)
class Ilyan(Person):       #inherited fron Person

    def __init__(self,name,age,height):
        super().__init__(name,age)
        self.height=height
    def display(self):
        print("Fron ilyan class",self.name,self.age,self.height)
    

p1=Person("Ilyan",19)
p1.display()
p2=Ilyan("Damon",165,7)
p2.display()