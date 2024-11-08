arr = [1, 2, 2, 3, 4, 4, 5]

# Remove duplicates by using dict.fromkeys()
unique_arr = list(dict.fromkeys(arr))
print("Array with duplicates removed:", unique_arr)


# Remove duplicates by converting to a set, then back to a list
unique_arr1 = list(set(arr))
print("Array with duplicates removed:", unique_arr1)


unique_arrr = []
# Loop through the array and add elements to unique_arr if not already present
for num in arr:
    if num not in unique_arrr:
        unique_arrr.append(num)

print("Array with duplicates removed:",unique_arrr)