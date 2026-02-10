list=[]
print("Shopping list.\n")
while True:
    print("1.Add items.\n2.Remove items.\n3.View All items.\n4.Exit")
    choice=input("Enter your choice: ")
    if choice=="1":
        task=input("Enter the task to add to list: ")
        list.append(task)
        print("Task Added.\n")
    elif choice=="2":
        task=input("Enter task to remove: ")
        if task in list: 
            list.remove(task)
            print("task removed.")
        else:
            print("No task with that name.")
        print()
    elif choice=="3":
        counter=1
        for i in list:
            print(counter,i)
            counter+=1
        print()
    elif choice=="4":
        print("Exiting...")
        break
    else:
        print("404 Error... Invalid choice, try again")