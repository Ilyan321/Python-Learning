#write a program that asks the user to eneter 2 nbrs and perform division the program should handleinvalid outputs and division by 0 using try except block

num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")
try:
    num1 = float(num1)
    num2 = float(num2)
    result = num1 / num2
except ValueError:
    print("Invalid input. Please enter numeric values.")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
else:
    print("The result of the division is:", result)