# inner and outer functions
def outer():
    print("A")
    def inner():
        print("B")
    inner()
outer()

# calculator function
def calculator (num1,num2,op):
    if op == "+":
        return num1 + num2
    elif op == "-":
        return num1 - num2
    elif op == "*":
        return num1 * num2
    elif op == "/":
        return num1 / num2
    elif op =="%":
        return num1 % num2
    else:
        return "Invalid operation"
    
result = calculator(4,2,"%")
print(result)

# print items
def display(items):
    for i in items:
        print(i)
items = ["apple","banana","cherry"]
display(items)


 #find minimum
def find_min(numbers):
    minimum=min(numbers)
    return minimum
numbers=[5,3,8,1,4]
print(find_min(numbers))

# factorial recursive function
def factorial(n):
    if n==0:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(5))

# fibonacci recursive function
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
print(fibonacci(6))

# lambda
add= lambda x,y : x+y
print(add(3,5))

list=[1,2,3,4,5]
list[3]=299
print(list)
list[2]=100