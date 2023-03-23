import random

# Åben og læs input filen
with open('input.txt', 'r', encoding='utf8') as input_file:
# (encoding er fordi vi vil bruge en bestemt ascii )
    # Åben output filen så den kan skrive ny tekst
    with open('output.txt', 'w', encoding='utf8') as output_file:

        # Gå igennem hver linje i input filen
        for line in input_file:

            # Del linjerne til hver sit ord 
            words = line.split()

            # Gå igennem hvert ord i linjen
            for word in words:

                # Hvis ordet har 1 eller 2 bogstaber, bliver det ikke blandet i output filen
                if len(word) <= 2:
                    output_file.write(word + ' ')
                    continue

                # Eller blander den bogstaverne i midten af ordet
                middle_letters = list(word[1:-1])
                random.shuffle(middle_letters)
                scrambled_word = word[0] + ''.join(middle_letters) + word[-1]

                # Skriv de nye blandet ord ind i output filen
                output_file.write(scrambled_word + ' ')

            # Lav en ny række for at separere linjerne
            output_file.write('\n')