import pandas
alphabet = pandas.read_csv("nato_phonetic_alphabet.csv")
dicionario = {row.letter: row.code for (index, row) in alphabet.iterrows()}

user_word = input("What word would you like to spell phonetically? ").upper()
nato_spelling = [dicionario[letter] for letter in user_word]
print(nato_spelling)

