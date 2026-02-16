class add:
    x=5

class empty:# for empty class
    pass

p1=add() #create obj
print(p1.x)
del p1   #delete an obj

# init method
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

p1=Person("Ilyan",19)
print(p1.name)
print(p1.age)
