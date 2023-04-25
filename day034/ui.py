from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
WHITE_COLOR = "#FFFFFF"
FONT = ('Arial', 20, "italic")


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.quiz_brain = quiz_brain

        self.score_label = Label(text="Score: 0", bg=THEME_COLOR, fg=WHITE_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250)
        self.canvas.grid(row=1, column=0, columnspan=2, padx=20, pady=20)
        self.question_text = self.canvas.create_text(150, 100, width=280, text="Test question", font=FONT)

        true_button_image = PhotoImage(file="images/true.png")
        true_button = Button(image=true_button_image, command=lambda: self.update(True))
        true_button.grid(row=2, column=1)

        false_button_image = PhotoImage(file="images/false.png")
        false_button = Button(image=false_button_image, command=lambda: self.update(False))
        false_button.grid(row=2, column=0)

        self.set_question_text(quiz_brain.next_question())

        self.window.mainloop()

    def set_question_text(self, text):
        self.canvas.itemconfig(self.question_text, text=text)

    def update(self, answer):
        if self.quiz_brain.answer_is_correct(answer):
            self.score_label.config(text=f"Score: {self.quiz_brain.score}")

        next_question = self.quiz_brain.next_question()

        if next_question:
            self.set_question_text(next_question)

        else:
            self.set_question_text(f"Game over!\n\nYour final score: {self.quiz_brain.score}")
