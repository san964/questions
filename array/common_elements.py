def find_common_elements(arr1, arr2):
    # Convert both lists to sets and find the intersection
    common_elements = set(arr1).intersection(set(arr2))
    return list(common_elements)

# Example usage
arr1 = [1, 2, 3, 4, 5]
arr2 = [4, 5, 6, 7, 8]
print("Common elements:", find_common_elements(arr1, arr2))
