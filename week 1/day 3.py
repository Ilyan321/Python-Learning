name="Ilyan khan"
age=19

print(f"Hello, {name}, your age is {age} years.")
print("Hello, {}, your age is {} years.".format(name,age))

num1=int(input("Enter 1st number: "))
num2=int(input("Enter 2nd number: "))
print("The sum of both numbers is:",num1+num2)
print("The difference of both numbers is:",num1-num2)
print("The product of both numbers is:",num1*num2)
print("The division of both numbers is:",round(num1/num2,3))

l=int(input("Enter length: "))
b=int(input("Enter breadth: "))
area=l*b
perimeter=2*(l+b)
print("The area of rectangle is:",area)
print("The perimeter of rectangle is: ",perimeter)

price=int(input("Enter the price of an item: "))
quantity=float(input("Enter the quantity of item: "))
total=price*quantity
print("Total before discount is: ",total)
discount=total-(total*0.1)                      #10% discount
print("The total cost is: ",discount)

name1="Ilyan"
print("name1 uppercase: ",name1.upper())
print("name1 lowercase: ",name1.lower())
print("name1 title: ",name1.title())

pitp=input("enter: ")
print("Lowercase: ",pitp.lower())
print("Uppercase: ",pitp.upper())
print("Title case: ",pitp.title())













