from art import logo
from enum import IntEnum
import random
import os
import sys
sys.path.append(f"{os.path.dirname(__file__)}/../pyutils")
import pyutils

# assume:
# - infinite deck
# - cards are not removed from deck
# - ace can count as 1 or 11
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

class GameOutcome(IntEnum):
    PC_BLACKJACK_WIN = -2
    PC_REGULAR_WIN = -1
    DRAW = 0
    PLAYER_REGULAR_WIN = 1
    PLAYER_BLACKJACK_WIN = 2

def print_game(player_cards, pc_cards, should_conceal_pc_cards=False):
    print(logo)
    print(f"You: {player_cards} ({game_sum(player_cards)})")

    if should_conceal_pc_cards:
        print(f"Computer: [{pc_cards[0]}, ?] (?)")

    else:
        print(f"Computer: {pc_cards} ({game_sum(pc_cards)})")


def print_game_result(game_outcome):

    if game_outcome in {GameOutcome.PC_BLACKJACK_WIN, GameOutcome.PLAYER_BLACKJACK_WIN}:
        print("BLACKJACK!\n")

    if game_outcome >= GameOutcome.PLAYER_REGULAR_WIN:
        print("You win! 😎")

    elif game_outcome == GameOutcome.DRAW:
        print("Push! 🧐")

    else:
        print("You lose 😭")


def has_busted(cards):
    return game_sum(cards) > 21


def has_blackjack(cards):
    return sum(cards) == 21 and len(cards) == 2


def compare_cards(player_cards, pc_cards):
    return (21 - game_sum(player_cards)) - (21 - game_sum(pc_cards))


def normalize_aces(cards):

    if 11 in cards and sum(cards) > 21:
        modified_cards = cards.copy()
        modified_cards[modified_cards.index(11)] = 1

        return normalize_aces(modified_cards)

    else:
        return cards


def game_sum(cards):
    return sum(normalize_aces(cards))


def draw_card():
    return random.choice(cards)


def play():
    player_cards = [draw_card(), draw_card()]
    pc_cards = [draw_card(), draw_card()]
    game_outcome = None
    game_is_over = False

    while not game_is_over:
        os.system("clear")
        print_game(player_cards, pc_cards, True)

        if has_blackjack(pc_cards):
            game_is_over = True
            game_outcome = -2

        elif has_blackjack(player_cards):
            game_is_over = True
            game_outcome = 2

        else:
            print("\nHit (H) or stand (S)?")
            player_action = pyutils.get_pressed_key()

            if player_action == 'h':
                # player chose to draw another card
                player_cards.append(draw_card())
                game_is_over = has_busted(player_cards)

                if game_is_over:
                    game_outcome = GameOutcome.PC_REGULAR_WIN

            elif player_action == 's':
                # player chose to remain with their cards
                while not game_is_over:
                    cards_check = compare_cards(player_cards, pc_cards)

                    if cards_check == 0 and game_sum(pc_cards) >= 17:
                        # a draw below of 21
                        game_is_over = True
                        game_outcome = GameOutcome.DRAW

                    elif cards_check < 0 or cards_check == 0:
                        # player is winning, pc draws card
                        pc_cards.append(draw_card())

                        if has_busted(pc_cards):
                            # PC busted, player wins
                            game_is_over = True
                            game_outcome = GameOutcome.PLAYER_REGULAR_WIN

                    elif cards_check > 0:
                        # no busts but PC wins
                        game_is_over = True
                        game_outcome = GameOutcome.PC_REGULAR_WIN

    os.system("clear")
    print_game(player_cards, pc_cards)
    print("\n")
    print_game_result(game_outcome)
    print("\n")


def main():

    while True:
        play()
        print("Press any key to continue or ESC to exit... ")

        if pyutils.escape_was_pressed():
            exit()

if __name__ == "__main__":
    main()
