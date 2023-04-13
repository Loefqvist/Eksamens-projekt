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

                # Hvis ordet er på mindre end 2 bogstaber, bliver det sprunget over
                if len(word) <= 2:
                    output_file.write(word + ' ')
                    continue

                # Eller blander den bogstaverne i midten af ordet
                middle_letters = list(word[1:-1]) # word [1.-1] siger at vi tager det første og sidste tegn
                random.shuffle(middle_letters) # random shuffler bogstaverne i midten
                scrambled_word = word[0] + ''.join(middle_letters) + word[-1] # samler ordene og laver et mellemrum efter sidste tegn

                # Skriv de nye blandet ord ind i output filen
                output_file.write(scrambled_word + ' ')

            # Lav en ny række for at separere linjerne
            output_file.write('\n')
            # backslash n er et tegn for at skrive ny linje