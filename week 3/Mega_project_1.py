# write a python program with functions to add delete and search in dictionaryu. each contact should have name, phone number and email address.

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
    print("!.Add contact(name,phone,email)\n2.Delete Contact\n3.Search Contact\n4.Exit")
    ch=int(input("Enter your choice: "))
    if ch==1:
        name=input("Enter Name: ")
        phone=input("Enter Phone Number: ")
        email=input("Enter Email Address: ")
        add(name,phone,email)
    elif ch==2:
        name=input("Enter Name to delete: ")
        delete(name)
    elif ch==3:
        name=input("Enter Name to search: ")
        search(name)
    elif ch==4:
        break
    else:
        print("505: Invalid Choice.")