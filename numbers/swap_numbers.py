# Take three numbers as input from the user
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))

# Swap the numbers in a cyclic order
a, b, c = c, a, b

# Display the results
print("After swapping:")
print("First number:", a)
print("Second number:", b)
print("Third number:", c)
