# Take a number as input from the user
number = int(input("Enter a number: "))

# Calculate the sum of the digits
sum_of_digits = sum(int(digit) for digit in str(abs(number)))

# Display the result
print("The sum of the digits is:", sum_of_digits)
