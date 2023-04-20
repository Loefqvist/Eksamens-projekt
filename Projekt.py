import random

with open('input.txt', 'r', encoding='utf8') as input_file:

    with open('output.txt', 'w', encoding='utf8') as output_file:

        for line in input_file:

            words = line.split()

            for word in words:

                if len(word) <= 2:
                    output_file.write(word + ' ')
                    continue

                middle_letters = list(word[1:-1])
                random.shuffle(middle_letters)
                scrambled_word = word[0] + ''.join(middle_letters) + word[-1]

                output_file.write(scrambled_word + ' ')
                
            output_file.write('\n')