import random

# Definer en funktion som scrambler bogstaverne i midten af et ord
def scramble_word(word):
    # Hvis ordet kun har 2 bogstaver, så kan det ikke scrambles
    if len(word) <= 2:
        return word
    else:
        # Split ordet op i start, midt, og sidst bogstav
        first, middle, last = word[0], word[1:-1], word[-1]
        # blande midten af bogstaverne random
        shuffled_middle = ''.join(random.sample(middle, len(middle)))
        # Return ordet hvor den har blandet bogstaverne i midten
        return first + shuffled_middle + last

# Definer en funktion som blander indholdet i en text fil
def scramble_file(filename):
    # Åben filen for at læse indholdet
    with open(filename, 'r') as file:
        content = file.read()
    # Split indholdet ind i ord, blande hvert ord, og samle de blandede ord tilbage til en String
    scrambled_content = ' '.join([scramble_word(word) for word in content.split()])
    # Åben filen for at skrive de blandede ord
    with open(filename, 'w') as file:
        file.write(scrambled_content)
