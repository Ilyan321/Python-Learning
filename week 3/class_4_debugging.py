# def add(a,b):
#     print("Adding", a, "and", b)
#     result = a + b
#     print("Result is", result)
#     return result


# print(2)
# add(2, 3)
try:
    file = open('hello.txt', 'r+')
    content=file.read()
    file.write("\n# This is a new line added to the file.")
    print(content)
    file.close()
except FileNotFoundError:
    print("File not found error occurred")