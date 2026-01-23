num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))

for i in range(num1,num2+1):
    if i>2:

        if i%num1==0:
            continue
        else:
            print(i,"is a prime number")
    else:
        print(i,"is a prime number")
            
    