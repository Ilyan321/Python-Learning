#write a list function list_operations that takes a list of numbers  sorts the list reverses it  and return the modified list
def list_operations(numbers):
    numbers.sort()
    numbers.reverse()
    return numbers
list_numbers = [10, 20, 5, 30, 15]
result = list_operations(list_numbers)
print("Modified List:", result)
