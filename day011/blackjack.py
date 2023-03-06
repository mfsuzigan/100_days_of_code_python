import random
import os

# assume:
# - infinite deck
# - cards are not removed from deck
# - ace can count as 1 or 11

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def print_cards(player_cards, pc_cards, should_conceal_pc_cards = False):
    print("\n")
    print(f"You: {player_cards} ({game_sum(player_cards)})")

    if should_conceal_pc_cards:
        print(f"Computer: [{pc_cards[0]}, ?] (?)")

    else:
        print(f"Computer: {pc_cards} ({game_sum(pc_cards)})")

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
    return cards[random.randint(0, 12)]

def play():
    player_cards = []
    pc_cards = []

    player_cards.append(draw_card())
    player_cards.append(draw_card())

    pc_cards.append(draw_card())
    pc_cards.append(draw_card())
    
    # -2: PC blackjack
    # -1: PC wins
    # 0: draw (push)
    # 1: player wins
    # 2: player blackjack
    game_outcome = -1

    game_is_over = False
    
    while not game_is_over:
        os.system("clear")
        print_cards(player_cards, pc_cards, True)

        if has_blackjack(pc_cards):
            game_is_over = True
            game_outcome = -2

        elif has_blackjack(player_cards):
            game_is_over = True
            game_outcome = 2

        else:
            player_action = str.lower(input("\nHit (H) or stand (S)? "))

            if player_action == 'h':
                # player chose to draw another card
                player_cards.append(draw_card())
                game_is_over = has_busted(player_cards)

            elif player_action == 's':
                # player chose to remain with their cards

                while not game_is_over:
                    cards_check = compare_cards(player_cards, pc_cards)

                    if cards_check == 0 and game_sum(pc_cards) >= 17:
                        # draw below of 21
                        game_is_over = True
                        game_outcome = 0

                    elif cards_check < 0 or cards_check == 0:
                        #player is winning, draw card
                        pc_cards.append(draw_card())

                        if has_busted(pc_cards):
                            # PC busted, player wins
                            game_is_over = True
                            game_outcome = 1

                    elif cards_check > 0:
                        game_is_over = True

    os.system("clear")
    print_cards(player_cards, pc_cards)
    print("\n")

    if game_outcome == -2 or game_outcome == 2:
        print("BLACKJACK!\n")

    if game_outcome >= 1:
        print("You win! 😎")

    elif game_outcome ==  0:
        print("Push! 🧐")

    else:
        print("You lose 😭")

    print("\n")

def main():
    play()

if __name__ == "__main__":
    main()  