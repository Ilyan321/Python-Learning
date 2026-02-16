class Person:
    name=""
    age=0
    def __init__(self,name,age):    #constructur
        self.name=name
        self.age=age
    
    def greet(self):     #to greet 
        print("Hello",self.name)

    def display(self):   #to display or print 
        print(self.name,self.age)
    # def display1():
    #     print(name,age)

p1=Person("Ilyan",19)
p2=Person("Damon",165)
p1.display()
p2.display()
p1.greet()
p2.greet()

# p3=Person
# p3.name="Elijah"
# p3.age=1065
# print(p3.name,p3.age)
# p3.greet()