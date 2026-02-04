import os
if os.path.exists("hello.txt"):
    os.remove("hello.txt")
    print("File deleted")
else:
    print("File doesnt exists")


with open('hello.txt','r') as source:
    content=source.read()
with open("dest.txt",'w') as file:
    file.write(content)


name= input("Enter  ame: ")
age=input("Enter age: ")
with open('hello.txt','a') as file:
    file.append(name, age)


