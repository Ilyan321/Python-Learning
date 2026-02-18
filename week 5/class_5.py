class Animal:
    def __init__(self,name,age):
        self.name=name
        self.age=age
class Robot(Animal):
    def __init__(self, name, age,metal):
        Animal.__init__(self, name, age, metal)
        self.metal=metal

class dog(Robot):
    # def __init__(self, name, age, metal):
    #     Robot.__init__(self, name, age, metal)
    def display(self):
        print(self.name,self.age,self.metal)


p1=dog("jonhy",3,"iron")
p1.display()


