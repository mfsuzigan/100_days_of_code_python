# Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
import pandas

nato_alphabet_data = pandas.read_csv("nato_phonetic_alphabet.csv")
codes_dictionary = {row.letter: row.code for (index, row) in nato_alphabet_data.iterrows()}
# print(codes_dictionary)

# Create a list of the phonetic code words from a word that the user inputs.
word = input("Enter a word: ")
print([codes_dictionary[letter.upper()] for letter in word])
