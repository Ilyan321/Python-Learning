while True:
    try:
        num1=int(input("Enter first number: "))
        num2=int(input("Enter second number: "))
        op=input("Enter operation (+, -, *, /): ")
        if op not in ['+', '-', '*', '/']:
            print("Invalid operation")
            continue
        if op=='+':
            result=num1+num2
        elif op=='-':
            result=num1-num2
        elif op=='*':
            result=num1*num2
        elif op=='/':
            try:
                result=num1/num2
            except ZeroDivisionError:
                print("Error: Division by zero is not allowed.")
                continue
        print("Results: ",result)
        break
    except ValueError:
        print("Invalid input.Input integer.")
