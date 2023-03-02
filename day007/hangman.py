import requests
import os
from hangman_art import stages
from hangman_art import logo
import unicodedata

def getWord():
    form_data = {"num_words": "1"}
    wordResponse = requests.post("https://www.invertexto.com/ajax/words.php", data=form_data).json()
    word = wordResponse["result"][0]["word"]
    return unicodedata.normalize(u'NFKD', word).encode('ascii', 'ignore').decode('utf8')

def printGame(word, correctly_guessed_letters, number_lives, message):
    slots = ""
    os.system('clear')

    for letter in list(word):
        if letter in correctly_guessed_letters:
            slots += f"{letter} "    

        else:
            slots += "_ " 
    
    print(logo)
    print(stages[number_lives])
    print(slots)

    if (message != ""):
        print(f"\n{message}")

def gameIsOver(number_lives, correctly_guessed_letters, letters):
    return number_lives == 0 or len(correctly_guessed_letters) == len(letters)

def main():
    word = getWord()
    letters = list(dict.fromkeys(word))
    correctly_guessed_letters = []
    already_guessed_letters = []
    number_lives = 6
    message = ""

    while not gameIsOver(number_lives, correctly_guessed_letters, letters):
        printGame(word, correctly_guessed_letters, number_lives, message)

        letter = input(f"\nGuess a letter (lives left = {number_lives}): ")

        if (letter in already_guessed_letters):
            message = f"'{letter}' has already been guessed!"

        else:
            already_guessed_letters.append(letter)

            if letter in letters:
                message = "Right!"
                correctly_guessed_letters.append(letter)

            else:
                message = f"Wrong, '{letter}' is not in the word!"
                number_lives -= 1

    if number_lives == 0:
        message = f"Game over, you lose! Word was: '{word}'"

    else:
        message = "Game over, you win!"

    printGame(word, correctly_guessed_letters,number_lives, message)

if __name__ == "__main__":
    main()