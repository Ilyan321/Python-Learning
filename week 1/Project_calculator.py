# Python code by Ilyan khan serial number 20 
while True:
  
    num1=input("Enter first number: ")
    if num1=='q':
        break

    num2=int(input("Enter second number: "))
    choice=input("Enter operation: (+,-,*,/) ")
    if choice=='+':
        print("The addition of ",num1,"and",num2," is ",int(num1)+num2,"\n")
    elif choice=='-':
        print("The subtraction of ",num1,"and",num2," is ",int(num1)-num2,"\n")
    elif choice=='*':
        print("The multiplication of ",num1,"and",num2," is ",int(num1)*num2,"\n")
    elif choice=='/':
        print("The division of ",num1," and ",num2," is ",int(num1)/num2)
   