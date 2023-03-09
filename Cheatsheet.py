import random

# Define a function that scrambles the middle letters of a word
def scramble_word(word):
    # If the word has only 2 or fewer characters, we can't scramble it
    if len(word) <= 2:
        return word
    else:
        # Split the word into its first, middle, and last letters
        first, middle, last = word[0], word[1:-1], word[-1]
        # Shuffle the middle letters randomly
        shuffled_middle = ''.join(random.sample(middle, len(middle)))
        # Return the word with its middle letters shuffled
        return first + shuffled_middle + last

# Define a function that scrambles the contents of a text file
def scramble_file(filename):
    # Open the file for reading and read its contents
    with open(filename, 'r') as file:
        content = file.read()
    # Split the contents into words, scramble each word, and join the scrambled words back into a string
    scrambled_content = ' '.join([scramble_word(word) for word in content.split()])
    # Open the file for writing and write the scrambled contents
    with open(filename, 'w') as file:
        file.write(scrambled_content)
