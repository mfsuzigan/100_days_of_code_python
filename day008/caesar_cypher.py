import os
from math import fmod
import re
from art import logo


def normalize_shift(shift):
    return int(fmod(shift, 25))


def process_message(user_input):
    message = ""
    processable_pattern = re.compile("[a-z]")

    for letter in list(user_input[1]):

        if processable_pattern.match(letter):
            normalized_shift = normalize_shift(user_input[0])
            new_letter_index = ord(letter) + normalized_shift

            if new_letter_index > ord('z'):
                new_letter_index = (new_letter_index % ord('z')) - 1 + ord('a')

            elif new_letter_index < ord('a'):
                new_letter_index = ord('z') - (ord('a') - (normalized_shift + ord(letter) + 1))

            message += chr(new_letter_index)
        
        else:
            message += letter

    return message


def get_user_input():
    text = str.lower(input("\nType your message: "))
    # text = re.sub("\W|[0-9]|_", "", str.lower(text))
    shift = int(input("Type the shift number: "))
    return [shift, text]


def main():
    option_chosen = None

    while option_chosen != "3":
        os.system('clear')
        print(logo)

        print("Select an option: ")
        print("1 - encode")
        print("2 - decode")
        print("3 - exit")

        option_chosen = input("\n")

        match option_chosen:

            case "1":
                print(
                    "\nWARNING: Spaces, numbers and special characters will be stripped")
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
