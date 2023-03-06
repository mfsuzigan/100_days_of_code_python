from game_data import data
from art import logo, vs
import random
import os


def print_elements(element1, element2):
    print(
        f"Compare A: {element1['name']}, a {element1['description']}, from {element1['country']}")
    print(vs)
    print(
        f"Against B: {element2['name']}, a {element2['description']}, from {element2['country']}")

def guess_was_right(guess, element1, element2):
    return (element1["follower_count"] > element2["follower_count"] and guess == 'a') or (
            element2["follower_count"] > element1["follower_count"] and guess == 'b')


def main():
    element1 = random.choice(data)
    element2 = None
    message = ""
    score = 0
    game_is_over = False
    while not game_is_over:

        while element2 is None or element2 is element1:
            element2 = random.choice(data)

        os.system("clear")

        print(logo)
        print(message)
        print_elements(element1, element2)

        player_guess = str.lower(
            input("\nWho has more followers? Type 'A' or 'B': "))

        if guess_was_right(player_guess, element1, element2):

            if player_guess == 'b':
                element1 = element2

            element2 = None
            score += 1
            message = f"You're right! Current score: {score}"

        else:
            os.system("clear")
            print(logo)
            print(f"Sorry, that's wrong. Final score: {score}")
            game_is_over = True

if __name__ == "__main__":
    main()