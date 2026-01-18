# countdown from num to 0
print("Countdown Timer")
num=int(input("Enter a number: "))

while num>0:
    print(num)
    num-=1
print("Hurrah you reached the countdown end")

# password checker
print("\nPassword Checker")
while True:
    password=input("Enter your password: ")
    if password=="ilyan123":
        print("Access Granted.")
        break
    else:
        print("Access denied. Try again.")

sum1=0
print("\nSum of n numbers entil u press 0.")
while True:
    num1=int(input("Enter a number: "))
    if (num1==0):
        print("Exiting the loop.")
        break
    sum1+=num1
print("The total sum of numbers is: ",sum1)
        