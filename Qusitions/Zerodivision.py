n1 = int(input("Enter your first number"))
n2 = int(input("Enter your second number"))


def zerodivision(x, y):
    try:
        result = x / y
        print(result)
    except:
        print("zerodivision error")


zerodivision(n1, n2)
