def max_occurrence_char(string):
    # Dictionary to store character counts
    char_count = {}

    for char in string:
        # Increment the count for each character in the string
        char_count[char] = char_count.get(char, 0) + 1

    # Find the character with the maximum occurrence
    max_char = max(char_count, key=char_count.get)

    return max_char, char_count[max_char]


# Example usage
input_string = input("Enter a string: ")
max_char, max_count = max_occurrence_char(input_string)
print(f"The character '{max_char}' has the highest occurrence: {max_count} times.")
