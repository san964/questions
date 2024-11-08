arr = [3, 5, 7, 2, 8, 1]

# Find the largest element
largest = max(arr)

print("Largest element:", largest)

largest1 = arr[0]
# Loop through the array to find the largest element
for num in arr:
    if num > largest1:
        largest1 = num

print("Largest element:", largest1)