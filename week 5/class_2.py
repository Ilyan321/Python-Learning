class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    def greet(self):
        print("Hello",self.name)


p1=Person("Ilyan",19)
print(p1.name,p1.age)
p1.greet()