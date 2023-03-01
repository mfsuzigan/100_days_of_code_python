import requests
import os
from hangman_art import stages

def getWord():
    form_data = {"num_words": "1"}
    word = requests.post("https://www.invertexto.com/ajax/words.php", data=form_data).json()
    return word["result"][0]["word"]

def printGame(word, correctly_guessed_letters, number_lives):
    slots = ""
    os.system('clear')

    for letter in list(word):
        if letter in correctly_guessed_letters:
            slots += f"{letter} "    

        else:
            slots += "_ " 
    
    print(slots)
    print(stages[number_lives])

word = "cinemática"#getWord()
letters = list(dict.fromkeys(word))
correctly_guessed_letters = []
number_lives = 6

while number_lives != 0 and len(correctly_guessed_letters) != len(letters):
    printGame(word, correctly_guessed_letters, number_lives)

    letter = input(f"\nGuess a letter (lives left = {number_lives}): ")

    if letter in letters:
        correctly_guessed_letters.append(letter)
        print("\n\nRight!")

    else:
        number_lives -= 1
        print("\n\nWrong!")

printGame(word, correctly_guessed_letters,number_lives)

if number_lives == 0:
    print(f"Game over, you lose! Word was: {word}")

else:
    print("Game over, you win!")

