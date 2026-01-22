print("--------------To Do list-------------- ")
tasks=[]
while True:
    print("1.Add task.\n2.Remove completed task.\n3.View tasks.\n4.Exit.")
    # add task
    choice=int(input("Enter your choice: "))
    if choice==1:  
        task=input("Enter a task to add to your to-do list (or type 'exit' to quit): ")
        if task.lower() == 'exit':
            break
        tasks.append(task)
    # remove completed task
    elif choice==2:
        print("Removing all completed tasks...")
        tasks.clear()
    # view tasks
    elif choice==3:
        print("Tasks in your to-do list: ",end=" ")
        for i in tasks:
            print(i,end=" ")
        print()
    # exit program
    elif choice==4:
        break
    else:
        print("Invalid choice. Please try again.")
    
    