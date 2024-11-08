
def count_vowels_consonants(input_string):
    # Define vowels and consonants
    vowels = "aeiouAEIOU"
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"

    # Initialize counts
    vowel_count = 0
    consonant_count = 0

    # Count vowels and consonants
    for char in input_string:
        if char in vowels:
            vowel_count += 1
        elif char in consonants:
            consonant_count += 1

    return vowel_count, consonant_count


# Example usage
string = str(input("Enter string name : "))
vowels, consonants = count_vowels_consonants(string)
print("Number of vowels:", vowels)
print("Number of consonants:", consonants)
