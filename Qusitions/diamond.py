def print_diamond(n):
    # Upper half of the diamond (including middle line)
    for i in range(n):
        print(" " * (n - i - 1), end="")
        print("*" * (2 * i + 1))

    # Lower half of the diamond
    for i in range(n - 2, -1, -1):
        print(" " * (n - i - 1), end="")
        print("*" * (2 * i + 1))

n = int(input("Enter the number of rows for the half-diamond: "))
print_diamond(n)
