import tasks
while True: 
    print("1.Add Item\n2.Display Items\n3.Remove Item\n4.Exit")
    choice=int(input("Enter your choice: "))
    if choice==1:
        tasks.add()
    elif choice==2:
        tasks.display()
    elif choice==3:
        tasks.remove()
    elif choice==4:
        break
    else:
        print("404 Error. Try Again\n")
