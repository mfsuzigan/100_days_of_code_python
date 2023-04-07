# Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

def main():
    with open("Input/Names/invited_names.txt") as names_file:
        invited_names = [name.strip() for name in names_file.readlines()]

    with open("Input/Letters/starting_letter.txt") as letter_template_file:
        starting_letter = letter_template_file.read()

    for invited_name in invited_names:
        with open(f"Output/ReadyToSend/letter_for_{invited_name}.txt", "w") as letter_file:
            letter_text = starting_letter.replace("[name]", invited_name)
            letter_file.write(letter_text)
            print(f"Letter for {invited_name} ready")


if __name__ == "__main__":
    main()
