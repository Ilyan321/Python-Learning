list=[]
def add():
    task=input("Enter task: ")
    list.append(task)

def display():
    counter=1
    for i in list:
        print (counter,".",i)
        counter+=1
    print()

def remove():
    task1=input("Enter the task to remove: ")
    list.remove(task1)
    print("Item removed.")
