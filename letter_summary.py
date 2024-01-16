# Letter Summary

# Write a letter_histogram program that asks the user for input, and prints a dictionary containing the tally of how many times each letter in the alphabet was used in the word. For example:

# $ python3 letter_histogram.py
# Please enter a word: banana
# {'a': 3, 'b': 1, 'n': 2}


def letter_histogram(word):
    histogram = {}

     
    for letter in word:
        
        histogram[letter] = histogram.get(letter, 0) + 1

    return histogram

user_input = input("Please enter a word: ")

# Call the letter_histogram function
result = letter_histogram(user_input)

# Print the histogram
print(result)


