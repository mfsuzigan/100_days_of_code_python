from tkinter import *

THEME_COLOR = "#375362"
WHITE_COLOR = "#FFFFFF"
FONT = ('Arial', 20, "italic")


class QuizInterface:

    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        score_label = Label(text="Score: 0", bg=THEME_COLOR, fg=WHITE_COLOR)
        score_label.grid(row=0, column=1)

        canvas = Canvas(width=300, height=250)
        canvas.grid(row=1, column=0, columnspan=2, padx=20, pady=20)
        question_text = canvas.create_text(150, 100, text="Test question", font=FONT)

        true_button_image = PhotoImage(file="images/true.png")
        true_button = Button(image=true_button_image)
        true_button.grid(row=2, column=1)

        false_button_image = PhotoImage(file="images/false.png")
        false_button = Button(image=false_button_image)
        false_button.grid(row=2, column=0)

        self.window.mainloop()
