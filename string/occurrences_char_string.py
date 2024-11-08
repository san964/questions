def count_characters(string):
    # Dictionary to store character counts
    char_count = {}

    for char in string:
        # If the character is already in the dictionary, increment the count
        if char in char_count:
            char_count[char] += 1
        else:
            # Otherwise, add the character with a count of 1
            char_count[char] = 1

    return char_count


# Example usage
input_string = input("Enter a string: ")
result = count_characters(input_string)

print("Character counts:")
for char, count in result.items():
    print(f"'{char}': {count}")
