# Function to print a pyramid pattern
def print_pyramid(n):
    for i in range(1, n+1):
        # Print spaces
        print(' ' * (n - i), end='')
        # Print stars
        print('*' * (2 * i - 1))

# Taking input from the user
height = int(input("Enter the height of the pyramid: "))

# Calling the function to print the pyramid
print_pyramid(height)
