def bubble_sort(arr):
    n = len(arr)

    # Traverse through all elements in the array
    for i in range(n):
        # Keep track of whether any swaps were made
        swapped = False

        # Last i elements are already sorted, so we skip them
        for j in range(0, n - i - 1):
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        # If no swaps were made, the array is already sorted
        if not swapped:
            break

    return arr


# Example usage
arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = bubble_sort(arr)
print("Sorted array:", sorted_arr)


# Bubble sort has a time complexity of  𝑂(𝑛2),𝑂(n2) in the worst and average cases, so it is most effective for small or nearly sorted arrays.
