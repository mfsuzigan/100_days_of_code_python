import os.path
import random
import argparse
from tkinter import *

import pandas

BACKGROUND_COLOR = "#B1DDC6"
WHITE_COLOR = "#FFFFFF"
BLACK_COLOR = "#000000"

CARD_WORD_FONT = ("Arial", 60, "bold")
CARD_TITLE_FONT = ("Arial", 40, "italic")
CARD_FLIP_DELAY_MILLIS = 3000

SUPPORTED_LANGUAGES = {
    "de": {"name": "German", "original_words_file": "data/german_words.csv",
           "words_to_learn_file": "data/words_to_learn__de.csv"},
    "fr": {"name": "French", "original_words_file": "data/french_words.csv",
           "words_to_learn_file": "data/words_to_learn__fr.csv"}
}

foreign_language = ""
NATIVE_LANGUAGE = "English"

original_words_file_path = ""
words_to_learn_file_path = ""

words_data = {}
random_new_word = []

window = Tk()
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_photo_image = PhotoImage(file="images/card_front.png")
card_back_photo_image = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=card_front_photo_image)
flip_timer = -1


def main():
    window.title("Flashy")
    window.resizable(False, False)
    window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

    canvas.grid(row=0, column=0, columnspan=2)
    canvas_word_text = canvas.create_text(400, 263, font=CARD_WORD_FONT)
    canvas_title_text = canvas.create_text(400, 150, font=CARD_TITLE_FONT)

    wrong_button_image = PhotoImage(file="images/wrong.png")
    wrong_button = Button(image=wrong_button_image, highlightthickness=0,
                          command=lambda: show_new_word(canvas_title_text, canvas_word_text))
    wrong_button.grid(row=1, column=0)

    right_button_image = PhotoImage(file="images/right.png")
    right_button = Button(image=right_button_image, highlightthickness=0,
                          command=lambda: right_button_command(canvas_title_text, canvas_word_text))
    right_button.grid(row=1, column=1)

    load_words()
    show_new_word(canvas_title_text, canvas_word_text)
    window.mainloop()


def load_words():
    parser = argparse.ArgumentParser()
    parser.add_argument("--language", "-l", default="fr", help="Foreign language to practice")
    language_code = parser.parse_args().language

    global words_to_learn_file_path
    words_to_learn_file_path = SUPPORTED_LANGUAGES[language_code]["words_to_learn_file"]

    global original_words_file_path
    original_words_file_path = SUPPORTED_LANGUAGES[language_code]["original_words_file"]

    global foreign_language
    foreign_language = SUPPORTED_LANGUAGES[language_code]["name"]

    global words_data
    try:
        words_data = pandas.read_csv(words_to_learn_file_path).to_dict(orient="records")

    except FileNotFoundError:
        words_data = pandas.read_csv(original_words_file_path).to_dict(orient="records")


def right_button_command(canvas_title_text, canvas_word_text):
    show_new_word(canvas_title_text, canvas_word_text)
    mark_word_as_known(canvas.itemcget(canvas_word_text, "text"))


def mark_word_as_known(word):
    words_file_path = words_to_learn_file_path

    if not os.path.isfile(words_file_path):
        words_file_path = original_words_file_path

    try:
        with open(words_file_path, "r") as file:
            words_to_learn = pandas.read_csv(file)
            words_to_learn[words_to_learn[foreign_language] != word].to_csv(words_to_learn_file_path, index=False)

    except FileNotFoundError:
        pass


def show_new_word(canvas_title_text, canvas_word_text):
    global flip_timer
    canvas.after_cancel(flip_timer)

    global random_new_word
    random_new_word = random.choice(words_data)
    canvas.itemconfig(canvas_image, image=card_front_photo_image)
    canvas.itemconfig(canvas_word_text, text=random_new_word[foreign_language], fill=BLACK_COLOR)
    canvas.itemconfig(canvas_title_text, text=foreign_language, fill=BLACK_COLOR)

    flip_timer = canvas.after(CARD_FLIP_DELAY_MILLIS, func=lambda: flip_card(canvas_title_text, canvas_word_text))


def flip_card(canvas_title_text, canvas_word_text):
    canvas.itemconfig(canvas_image, image=card_back_photo_image)
    canvas.itemconfig(canvas_word_text, text=random_new_word[NATIVE_LANGUAGE], fill=WHITE_COLOR)
    canvas.itemconfig(canvas_title_text, text=NATIVE_LANGUAGE, fill=WHITE_COLOR)


if __name__ == "__main__":
    main()
