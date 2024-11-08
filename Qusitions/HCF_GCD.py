# HCF (Highest Common Factor), also known as GCD (Greatest Common Divisor), of two numbers is the largest number that divides both of them without leaving a remainder.


# Function to find HCF using Euclidean Algorithm
def find_hcf(x, y):
    while y:
        x, y = y, x % y  # Swap x with y, and y with x % y
    return x

# Input: Two numbers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Output: HCF (GCD) of the two numbers
hcf = find_hcf(num1, num2)
print(f"The HCF of {num1} and {num2} is: {hcf}")
