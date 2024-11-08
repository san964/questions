# Define two arrays
array1 = [1, 2, 3]
array2 = [4, 5, 6]

array3=array1+ array2

print(array3)
# Merge arrays by extending array1 with array2
array1.extend(array2)

print("Merged array:", array1)
