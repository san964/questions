# Take a list of numbers as input from the user
user_input = input("Enter a list of numbers separated by spaces: ")
numbers = list(map(int, user_input.split()))

# Separate even and odd numbers
even_numbers = [num for num in numbers if num % 2 == 0]
odd_numbers = [num for num in numbers if num % 2 != 0]

# Print the lists
print("Even numbers:", even_numbers)
print("Odd numbers:", odd_numbers)




