# Function to separate even and odd numbers
# Write a python program to print even and odd numbers lists by tacking list as a input from user.¶

def separate_even_odd(numbers):
    even_numbers = []
    odd_numbers = []

    for num in numbers:
        if num % 2 == 0:
            even_numbers.append(num)
        else:
            odd_numbers.append(num)

    return even_numbers, odd_numbers


# Taking input from the user
user_input = input("Enter a list of numbers separated by spaces: ")

# Converting the input string into a list of integers
numbers_list = list(map(int, user_input.split()))

# Calling the function
even_list, odd_list = separate_even_odd(numbers_list)

# Printing the results
print("Even numbers:", even_list)
print("Odd numbers:", odd_list)

