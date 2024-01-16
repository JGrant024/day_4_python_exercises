# Write a word_histogram program that asks the user for a sentence as its input,
# and prints a dictionary containing the tally of how many times each word in the 
# alphabet was used in the text. For example: 

# $ python3 word_histogram.py
# Please enter a sentence: To be or not to be
# {'to': 2, 'be': 2, 'or': 1, 'not': 1}

def word_histogram(sentence):
    histogram = {}

    # Split the sentence into words
    words = sentence.split()

    for word in words:
        # Convert the word to lowercase to make it case-insensitive
        word = word.lower()

        # Increment the count for each word
        histogram[word] = histogram.get(word, 0) + 1

    return histogram

# Get input from the user
user_input = input("Please enter a sentence: ")

# Call the word_histogram function
result = word_histogram(user_input)

# Print the histogram
print(result)



