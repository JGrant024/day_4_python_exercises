# Sorting a histogram

# Given a histogram tally (one returned from either letter_histogram or word_histogram), print the top 3 words or letters.

# HINT: Lookup the sorted() built-in.

# $ python3 word_histogram_tally.py

# Please enter a sentence: To be or not to be do be do be do
# The top three words are:
# be: 4
# do: 3
# to: 2

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

def print_top_words(histogram, top_n=3):
    sorted_histogram = sorted(histogram.items(), key=lambda x: x[1], reverse=True)

    print("The top", top_n, "words are:")
    for i in range(min(top_n, len(sorted_histogram))):
        word, count = sorted_histogram[i]
        print(f"{word}: {count}")

# Get the  input from the user
user_input = input("Please enter a sentence: ")

# Call the word_histogram function
result = word_histogram(user_input)

# Print the top 3 words
print_top_words(result, top_n=3)
