# Function to calculate Fibonacci number using recursion
def fibonacci_recursive(n):
    if n <= 1:
        return n

    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

# Print the Fibonacci sequence up to a given number of terms
num_terms = int(input("Enter a number : "))  # Change this to get more terms in the sequence

for i in range(num_terms):
    print(fibonacci_recursive(i), end=" ")



# # Function to print the Fibonacci sequence up to a given limit
# def fibonacci_sequence(limit):
#     a, b = 0, 1
#     while a <= limit:
#         print(a, end=" ")
#         a, b = b, a + b
#
# # Set the limit
# limit = 50  # Change this to any limit you want
#
# # Print the Fibonacci sequence
# fibonacci_sequence(limit)
