import pandas as pd

data = pd.read_csv("nato_phonetic_alphabet.csv")

# Create dict
# {"A": 'Alpha', ...}

d = {row.letter: row.code for (key, row) in data.iterrows()}
print(d)

# Create a list of the code words from the user input
input_word = input()
code_words = [d[letter.upper()] for letter in input_word]
print(f'code words: {code_words}')

