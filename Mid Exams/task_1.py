print("Simple calculator for mids exams.")
while True:
    num1=input("Enter 1st number: ")
    if num1=="q":
        print("exiting...")
        break
    num2=int(input("Enter 2nd number: "))
    op=input("Enter operation(+,-,*,/,%): ")
    if op=="+":
        print("The sum of both numbers is:",int(num1)+num2)
    elif op=="-":
        print("The difference of both numbers is: ",int(num1)-num2)
    elif op=="*":
        print("The product of both numbers is: ",int(num1)*num2)
    elif op=="/":
        print("The division of both numbers is: ",int(num1)/num2)
    elif op=="%":
        print("The reminder of both numbers is: ",int(num1)%num2)
    else:
        print("404 Error...Invalid operation, Try again")
        

    