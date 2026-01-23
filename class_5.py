num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))

for i in range(num1,num2+1):
    if i>1:
        is_prime=True
        for j in range (2,i):
    
            if i%j==0:
                is_prime=False
                break

        if is_prime:
            print(i,"is a prime number")
           
            
    