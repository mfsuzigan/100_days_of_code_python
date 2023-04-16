import random
from tkinter import *

import pandas

BACKGROUND_COLOR = "#B1DDC6"
WHITE_COLOR = "#FFFFFF"
BLACK_COLOR = "#000000"

CARD_WORD_FONT = ("Arial", 60, "bold")
CARD_TITLE_FONT = ("Arial", 40, "italic")

CARD_FLIP_DELAY_MILLIS = 3000
FOREIGN_LANGUAGE = "French"
NATIVE_LANGUAGE = "English"

words_data = pandas.read_csv("data/french_words.csv").to_dict(orient="records")
random_new_word = []

window = Tk()
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_photo_image = PhotoImage(file="images/card_front.png")
card_back_photo_image = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=card_front_photo_image)


def main():
    window.title("Flashy")
    window.resizable(False, False)
    window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

    canvas.grid(row=0, column=0, columnspan=2)
    canvas_word_text = canvas.create_text(400, 263, font=CARD_WORD_FONT, text="bla")
    canvas_title_text = canvas.create_text(400, 150, font=CARD_TITLE_FONT, text="bla")
    canvas.after(CARD_FLIP_DELAY_MILLIS, func=lambda: flip_card(canvas_title_text, canvas_word_text))

    wrong_button_image = PhotoImage(file="images/wrong.png")
    wrong_button = Button(image=wrong_button_image, highlightthickness=0,
                          command=lambda: set_new_word(canvas_title_text, canvas_word_text))
    wrong_button.grid(row=1, column=0)

    right_button_image = PhotoImage(file="images/right.png")
    right_button = Button(image=right_button_image, highlightthickness=0,
                          command=lambda: set_new_word(canvas_title_text, canvas_word_text))
    right_button.grid(row=1, column=1)

    set_new_word(canvas_title_text, canvas_word_text)
    window.mainloop()


def set_new_word(canvas_title_text, canvas_word_text):
    global random_new_word
    random_new_word = random.choice(words_data)
    canvas.itemconfig(canvas_image, image=card_front_photo_image)
    canvas.itemconfig(canvas_word_text, text=random_new_word[FOREIGN_LANGUAGE], fill=BLACK_COLOR)
    canvas.itemconfig(canvas_title_text, text=FOREIGN_LANGUAGE, fill=BLACK_COLOR)
    canvas.after(CARD_FLIP_DELAY_MILLIS, func=lambda: flip_card(canvas_title_text, canvas_word_text))


def flip_card(canvas_title_text, canvas_word_text):
    canvas.itemconfig(canvas_image, image=card_back_photo_image)
    canvas.itemconfig(canvas_word_text, text=random_new_word[NATIVE_LANGUAGE], fill=WHITE_COLOR)
    canvas.itemconfig(canvas_title_text, text=NATIVE_LANGUAGE, fill=WHITE_COLOR)


if __name__ == "__main__":
    main()
