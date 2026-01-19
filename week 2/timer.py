num=int(input("Enter the starting point: "))
ch=input("if u dont want the divisibles of 3 press y else n: ").lower()
while num>0:
    if ch=='y' and num%3==0:
        print(num)
        continue
    elif ch=='n':
        print(num)
    num-=1 
