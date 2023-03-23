import random

# Open the input file for reading
with open('tekst.txt', 'r') as input_file:

    # Open the output file for writing
    with open('output.txt', 'w') as output_file:

        # Loop over each line in the input file
        for line in input_file:

            # Split the line into individual words
            words = line.split()

            # Loop over each word in the line
            for word in words:

                # If the word has length 1 or 2, write it unchanged to the output file
                if len(word) <= 2:
                    output_file.write(word + ' ')
                    continue

                # Otherwise, scramble the word by shuffling the middle letters
                middle_letters = list(word[1:-1])
                random.shuffle(middle_letters)
                scrambled_word = word[0] + ''.join(middle_letters) + word[-1]

                # Write the scrambled word to the output file
                output_file.write(scrambled_word + ' ')

            # Write a newline character to the output file to separate lines
            output_file.write('\n')