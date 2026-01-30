contact={}
while True:
    print("1.Add Contact(name,phone)\n2.View Contact\n3.Search Contact\n4.Exit")
    choice=int(input("Enter your choice: "))
    if choice==1:
        name=input("Enter Name: ")
        phone=input("Enter Phone Number: ")
        contact[name]=phone
        print("Contact Added Successfully.")
    elif choice==2:
        print("Contacts List:")
        for name,phone in contact.items():
            print("Name: ",name," Phone: ",phone)
    elif choice==3:
        #search
        search_name=input("Enter the name to search: ")
        if search_name in contact:
            print("Contact Found: ",search_name," Phone: ",contact[search_name])
        else:
            print("Contact Not Found.")
    elif choice==4:
        break
    else: 
        print("Invalid Choice. Please try again.")










