# Take a list of numbers as input from the user
user_input = input("Enter a list of numbers separated by spaces: ")
numbers = list(map(int, user_input.split()))

# Print the number of digits for each number
print("Number of digits in each number:")
for num in numbers:
    count = len(str(abs(num)))  # Count the digits
    print(f"{num} has {count} digits")

# 1 1 digit
# 12 2 digits
# 123 3 digit