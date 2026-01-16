
i = 10
while i<100:
    print("hello", i)
    i+=10

while True:
    num=int(input("Enetr number: "))
    if(num==0):
        break
    print("U entered",num)

for i in range(1,11):
    if i%3==0:
        continue
    print("")

# prime or not
num=int(input("Enter a number: "))
if (num>1):
    for i in range(2,num):
        if num%2==0:
            print("Not a prime.")
            break
        else:
            print("Prime")
    else:
        print("Prime")
   
total=0
for i in range(1,101):
    total=total+i
print("Total is: ",total)

num3=int(input("Enter num: "))
sum=1
for i in range(1,num3+1):
    sum*=i
print("The factorial is: ",sum)



s=input("Enter word: ")
# print("The reverse of string is: ",s[4:3:-1])

if(s==s[::-1]):
    print("this is  palindrome.")
else:
    print("Not palindrome")

num4=int(input("Enter the number u want to start tables: "))
num5=int(input("Enter the number u want to end tables: "))

for i in range(num4,num5+1):
    print("The table of number ",i)
    for j in range(1,11):
        print(i,"*",j,"=",i*j)


total=0
for i in range(2,101,2):
    total+=i
    print("Even nbr sum: ",i,total)


num6=int(input("Enter the number: "))
num7=int(input("Enter the number: "))
num8=int(input("Enter the number: "))

max=max(num6,num7,num8)
print(max)

str=input("Enter string: ")
vowel="aeiouAEIOU"
vcount=0
for char in str:
    if char in vowel:
        vcount+=1
        
print(vcount)