contact={}
while True:
    print("1.Add Contact(name,phone)\n2.View Contact\n3.Exit")
    choice=int(input("Enter your choice: "))
    if choice==1:
        name=input("Enter Name: ")
        phone=input("Enter Phone Number: ")
        contact[name]=phone
        print("Contact Added Successfully.")
    elif choice==2:
        # print("Contacts List:")
        # for name,phone in contact.items():
        #     print("Name: ",name," Phone: ",phone)
        print(contact)
    elif choice==3:
        break