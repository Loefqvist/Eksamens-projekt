import random

def scramble_word(word):
    if len(word) <= 2:
        return word
    else:
        middle = list(word[1:-1])
        random.shuffle(middle)
        return word[0] + ''.join(middle) + word[-1]

def scramble_file(filename):
    with open("tekst.txt", 'r') as file:
        content = file.read()
        words = content.split()
        scrambled_words = [scramble_word(word) for word in words]
        scrambled_content = ' '.join(scrambled_words)
    with open("output.txt", 'w') as file:
        file.write(scrambled_content)
