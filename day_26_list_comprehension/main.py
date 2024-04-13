import pandas as pd

data = pd.read_csv("nato_phonetic_alphabet.csv")

# Create dict
# {"A": 'Alpha', ...}

d = {row.letter: row.code for (key, row) in data.iterrows()}
print(d)


# Create a list of the code words from the user input
def generate_phonetic():
    input_word = input("Enter a word: ")
    try:
        code_words = [d[letter.upper()] for letter in input_word]
    except KeyError:
        print('Only alphabetic letters')
        generate_phonetic()
    else:
        print(f'code words: {code_words}')


generate_phonetic()
