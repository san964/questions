# Take a list of numbers as input from the user
user_input = input("Enter a list of numbers separated by spaces: ")
numbers = list(map(int, user_input.split()))

# Check if there are at least two distinct elements
if len(set(numbers)) < 2:
    print("The list should contain at least two distinct elements.")
else:
    # Find the largest and second-largest elements
    largest = max(numbers)
    numbers.remove(largest)
    second_largest = max(numbers)

    print("The second largest element is:", second_largest)
