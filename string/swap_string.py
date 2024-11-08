# Take three numbers as input from the user
a = input("Enter the first string: ")
b = input("Enter the second string: ")
c = input("Enter the third string: ")

# Swap the numbers in a cyclic order
a, b, c = c, a, b

# Display the results
print("After swapping:")
print("First string:", a)
print("Second string:", b)
print("Third string:", c)
