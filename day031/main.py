from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"
IDIOM_WORD_FONT = ("Arial", 60, "bold")
IDIOM_FONT = ("Arial", 40, "italic")


def main():
    window = Tk()
    window.title("Flashy")
    window.resizable(False, False)
    window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

    canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
    card_image = PhotoImage(file="images/card_back.png")
    canvas.create_image(400, 263, image=card_image)
    canvas.create_text(400, 263, text="trouve", font=IDIOM_WORD_FONT)
    canvas.create_text(400, 150, text="french", font=IDIOM_FONT)
    canvas.grid(row=0, column=0, columnspan=2)

    wrong_button_image = PhotoImage(file="images/wrong.png")
    Button(image=wrong_button_image, highlightthickness=0, command=test).grid(row=1, column=0)

    right_button_image = PhotoImage(file="images/right.png")
    Button(image=right_button_image, highlightthickness=0, command=test).grid(row=1, column=1)

    window.mainloop()


def test():
    print("Test")


if __name__ == "__main__":
    main()
