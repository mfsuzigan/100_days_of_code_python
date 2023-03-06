import random
from art import logo


def print_lives_left(lives_left):
    print(f"You have {lives_left} attempts to guess the number.")

HARD_LEVEL_LIVES = 5
EASY_LEVEL_LIVES = 10

print(logo)
print("Try to guess a number from 1 to 100.")
secret_number = random.randint(1, 100)
difficulty = str.lower(
    input("\nChoose a difficulty. Type 'e' for easy or anything else for hard: "))
lives_left = HARD_LEVEL_LIVES

if difficulty == "e":
    lives_left = EASY_LEVEL_LIVES

while lives_left > 0:
    print_lives_left(lives_left)
    guess = int(input("Make a guess: "))

    if guess > secret_number:
        print("Too high. Guess again.")
        lives_left -= 1

    elif guess < secret_number:
        print("Too low. Guess again.")
        lives_left -= 1

    else:
        break

if (lives_left > 0):
    print(f"You got it!")

else:
    print(f"You lose.")

print(f"The answer was {secret_number}")
