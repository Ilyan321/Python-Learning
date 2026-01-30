# write a function tuple_operations that takes a tuple numbers finds maximum and minimum and sum and returns these values
def tuple_operations(numbers):
    maximum = max(numbers)
    minimum = min(numbers)
    total_sum = sum(numbers)

    return maximum, minimum, total_sum

tuple_numbers = (10, 20, 5, 30, 15)
result = tuple_operations(tuple_numbers)
print("Maximum:", result[0])
print("Minimum:", result[1])
print("Sum:", result[2])