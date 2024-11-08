# Write a python program to print the multiplication of all elements of list using for loop also with reduce function.
# numbers = [2, 3, 4, 5]
# result = 1
# for num in numbers:
#     result *= num
# print("Multiplication using for loop:", result)



from functools import reduce

numbers = [2, 3, 4, 5]
# Using reduce to multiply all elements in the list
result = reduce(lambda x, y: x * y, numbers)
# Print the result
print("Multiplication using reduce:", result)
