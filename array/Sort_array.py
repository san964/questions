# arr = [5, 2, 9, 1, 5, 6]
# arr.sort()  # This will sort the array in place
# print("Sorted array (in-place):", arr)
from itertools import count

# Take input from the user
user_input = input("Enter numbers separated by spaces: ")

# Convert input string to a list of integers
arr = list(map(int, user_input.split()))

arr.sort() # This will sort the array in place

print("Array entered by user:", arr)


print(len(arr))
