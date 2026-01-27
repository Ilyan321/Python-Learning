# # inner and outer functions
# def outer():
#     print("A")
#     def inner():
#         print("B")
#     inner()
# outer()

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