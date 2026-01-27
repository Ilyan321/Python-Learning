list=[]
while True:
    print("Shopping list.")
    print("1.Add item.\n2.Remove item.\n3.View All items.\n4.exit")
    num=int(input("Enter your choice: "))
    if num==1:
        item=input("Enter your item: ")
        list.append(item)
        print("Item successfully added.")
    elif num==2:
        item=input("Enter your item to remove: ")
        list.remove(item)
        print("Item successfully removed.")
    elif num==3:
        print("All items in list: ",list)
    elif num==4:
        exit()
    