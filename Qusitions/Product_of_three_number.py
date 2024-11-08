a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

# Check if all conditions are satisfied for a valid result
if a > 0 and b > 50 and c < 100:
    result = a * b * c
    print(f"The result of {a} * {b} * {c} is: {result}")

# Handle specific cases where values are incorrect
elif a <= 0:
    print("First number is wrong (it should be greater than 0)")
elif b <= 50:
    print("Second number is wrong (it should be greater than 50)")
elif c >= 100:
    print("Third number is wrong (it should be less than 100)")
