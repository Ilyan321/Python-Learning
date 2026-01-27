amount=0

# check balance
def check_balance():
    print("Total Amount: ",amount)
# deposit

def deposit(val):
    global amount
    amount+=val
    print("Amount deposited. Total Amount: ",amount)
# withdraw
def withdraw(val):
    global amount
    amount-=val
    print("Amount withdrawn. Total Amount now: ",amount)

def bank_system():
    while True:
        print("Simple banking system.")
        
        print("1.Check balance.\n2.Deposit amount.\n3. Withdraw Amount.\n4.Exit")
        choice=int(input("Enter your choice: "))
        if choice==1:
            check_balance()
        elif choice==2:
            num1=int(input("Enter the Amount to deposit: "))
            deposit(num1)
        elif choice==3:
            num2=int(input("Enter the Amount to deposit: "))
            withdraw(num2)
        elif choice==4:
            return

bank_system()