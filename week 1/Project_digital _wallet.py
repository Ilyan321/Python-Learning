amount_list=[]
reason_list=[]
while True:
    print("Digital wallet options: ")
    print("1. Add amount and reason.\n2. View Total amount and reasons.\n3. Exit.")
    choice=int(input("Enter your choice: "))
    if choice==1:
        amount=int(input("Enter the amount to add: "))
        reason=input("Enter the reason for this amount: ")
        amount_list.append(amount)
        reason_list.append(reason)
        print("Amount added successfully.\n")
    elif(choice==2):
        total=sum(amount_list)
        print("Total amount in wallet: ",total)
        print("Reasons for amounts added: ",reason_list)
    elif(choice==3):
        print("Exiting the digital wallet.")
        break
    
    else:
        print("Invalid choice. Please try again.\n")