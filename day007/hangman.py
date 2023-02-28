import requests
import os

def getWord():
    form_data = {"num_words": "1"}
    word = requests.post("https://www.invertexto.com/ajax/words.php", data=form_data).json()
    return word["result"][0]["word"]

def printLetterSlots(word, correctly_guessed_letters):
    slots = ""

    for letter in list(word):

        if letter in correctly_guessed_letters:
            slots += f"{letter} "    

        else:
            slots += "_ " 
    
    print(slots)

word = "carinhosa" #getWord()
letters = list(word)
correctly_guessed_letters = []
number_lives = 6
guessed_right = False

while number_lives != 0 and len(correctly_guessed_letters) != len(letters):

    os.system('clear')
    print(f"{number_lives} {correctly_guessed_letters} {letters}")
    printLetterSlots(word, correctly_guessed_letters)

    letter = input(f"\nGuess a letter (lives left = {number_lives}): ")

    if letter in letters:
        correctly_guessed_letters.append(letter)
        print("\n\nRight!")

    else:
        number_lives -= 1
        print("\n\nWrong!")

print("Game over!")

if number_lives == 0:
    print(f"Word was: {word}")

else:
    print("You win!")

