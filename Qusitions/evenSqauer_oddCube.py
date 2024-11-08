num = int(input("Enter a number : "))


even_cube= lambda x:x**3
odd_Squer= lambda x:x**2

for i in [num]:
    if i % 2== 0:
        print(f"Cube of {num} is: {even_cube(num)}")
    else:
        print(f"Cube of {num} is: {odd_Squer(num)}")