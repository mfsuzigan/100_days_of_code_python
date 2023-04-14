import pandas

nato_alphabet_data = pandas.read_csv("nato_phonetic_alphabet.csv")
codes_dictionary = {row.letter: row.code for (index, row) in nato_alphabet_data.iterrows()}
finished = False

while not finished:
    word = input("Enter a word: ")

    try:
        print([codes_dictionary[letter.upper()] for letter in word])
        finished = True
    except KeyError:
        print("Sorry, only letters in the alphabet please")
