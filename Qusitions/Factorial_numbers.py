def factorials(n):
    if n==0 or n==1:
        return 1
    else:
        return n *factorials(n-1)

num= int(input("Enter a number : "))

if num <=0:
    print("Factorial is not define for negative numbers")
else:
    result= factorials(num)
    print(f"The factorial of{num} is {result}")


# calculation factorial of 𝑛 using recursion: