
contacts={}
def add(name,phone,email):
    contacts[name]={"phone": phone, "email": email}
    print("Contact Added Successfully.")
def delete(name):
    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully.")
    else:
        print("404: Contact Not Found.")
def search(name):
    if name in contacts:
        print("Contact found: ",name," \nPhone: ",contacts[name]["phone"]," \nEmail: ",contacts[name]["email"])
    else:
        print("404: Contact Not Found.")
while True:
    print("1.Add contact(name,phone,email)\n2.Update Contact\n3.Delete Contact\n4.Search Contact\n5.Exit")
    ch=int(input("Enter your choice: "))
    if ch==1:
        name=input("Enter Name: ")
        if name in contacts:
            print("Contact already exists.")
        else:
            phone=input("Enter Phone Number: ")
            email=input("Enter Email Address: ")
            add(name,phone,email)
    elif ch==2:
        name=input("Enter Name to update: ")
        phone=input("Enter new Phone Number: ")
        email=input("Enter new Email Address: ")
        add(name,phone,email)
    elif ch==3:
        name=input("Enter Name to delete: ")
        delete(name)
    elif ch==4:
        name=input("Enter Name to search: ")
        search(name)
    elif ch==5:
        break
    else:
        print("505: Invalid Choice.")