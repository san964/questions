# Function to find HCF using Euclidean Algorithm
# To calculate the LCM (Least Common Multiple) of two numbers, we can use the relationship between LCM and HCF (GCD).


def find_hcf(x, y):
    while y:
        x, y = y, x % y
    return x

# Function to find LCM using HCF
def find_lcm(x, y):
    hcf = find_hcf(x, y)
    return abs(x * y) // hcf  # LCM formula

# Input: Two numbers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Output: LCM of the two numbers
lcm = find_lcm(num1, num2)
print(f"The LCM of {num1} and {num2} is: {lcm}")
