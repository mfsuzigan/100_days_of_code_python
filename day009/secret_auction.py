import os
from art import logo

print("Welcome to the secret auction program.")
bidders = {}
there_are_more_bidders = True
highest_bid = 0
winner = ""

while there_are_more_bidders:
    os.system("clear")
    print(logo)
    name = input("What is your name? ")
    bid = float(input("What's your bid? $"))
    bidders[name] = bid

    if bid > highest_bid:
        highest_bid = bid
        winner = name

    more_bidders_prompt = ""

    while more_bidders_prompt not in ["y", "yes", "no", "n"]:
        more_bidders_prompt = str.lower(input("\nAre there any other bidders? (y/n) "))

        if more_bidders_prompt in ['y', 'yes']:
            there_are_more_bidders = True
        
        elif more_bidders_prompt in ['n', 'no']:
            there_are_more_bidders = False

        else:
            print("Invalid input.")

os.system("clear")
print(logo)
print(f"The winner is {winner} with a bid of ${bidders[winner]}.")