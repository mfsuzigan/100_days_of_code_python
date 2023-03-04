import os
from math import fmod
from re import sub

def normalize_shift(shift):
    return int(fmod(shift, 25))

def process_message(user_input):
    message = ""
    
    for letter in list(user_input[1]):
        message += chr(ord(letter) + normalize_shift(user_input[0]))

    return message

def get_user_input():
    text = input("\nType your message: ")
    text = sub("\W|[0-9]|_", "", str.lower(text))
    shift = int(input("Type the shift number: "))
    return [shift, text]

def main():
    option_chosen = None

    while option_chosen != "3":
        os.system('clear')

        print("Select an option: ")
        print("1 - encode")
        print("2 - decode")
        print("3 - exit")

        option_chosen = input("\n")

        match option_chosen:

            case "1":
                print("\nWARNING: Spaces, numbers and special characters will be stripped")
                user_input = get_user_input()
                print(f"\nEncrypted message: {process_message(user_input)}")
                input("\nPress enter to continue....")

            case "2":
                user_input = get_user_input()
                user_input[0] = -user_input[0]
                print(f"\nDecrypted message: {process_message(user_input)}")
                input("\nPress enter to continue....")


if __name__ == "__main__":
    main()
