# Function to check if a number is perfect
def is_perfect(number):
    # Return False if the number is less than or equal to 1
    if number <= 1:
        return False

    # Find all divisors and sum them
    divisors_sum = 0
    for i in range(1, number):
        if number % i == 0:
            divisors_sum += i

    # Check if the sum of divisors equals the number
    return divisors_sum == number


# Take input from the user
num = int(input("Enter a number: "))

# Check if the number is perfect and display the result
if is_perfect(num):
    print(f"{num} is a perfect number.")
else:
    print(f"{num} is not a perfect number.")
