from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
WHITE_COLOR = "#FFFFFF"
WRONG_ANSWER_COLOR = "#e7305b"
RIGHT_ANSWER_COLOR = "#9bdeac"

FONT = ('Arial', 20, "italic")
FEEDBACK_DURATION_MILLIS = 2000


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
        self.true_button = Button(image=true_button_image, command=lambda: self.check_answer(True))
        self.true_button.grid(row=2, column=1)

        false_button_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_button_image, command=lambda: self.check_answer(False))
        self.false_button.grid(row=2, column=0)

        self.game_is_over = False
        self.set_question_text(quiz_brain.next_question())

        self.window.mainloop()

    def set_question_text(self, text):
        self.canvas.itemconfig(self.question_text, text=text)

    def check_answer(self, answer):

        if not self.game_is_over:

            if self.quiz_brain.answer_is_correct(answer):
                self.canvas.config(bg=RIGHT_ANSWER_COLOR)
                self.score_label.config(text=f"Score: {self.quiz_brain.score}")

            else:
                self.canvas.config(bg=WRONG_ANSWER_COLOR)

            self.canvas.after(ms=FEEDBACK_DURATION_MILLIS, func=lambda: self.display_next_question())

    def display_next_question(self):
        self.canvas.config(bg=WHITE_COLOR)
        next_question = self.quiz_brain.next_question()

        if next_question:
            self.set_question_text(next_question)

        else:
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
            self.set_question_text(f"Game over!\n\nYour final score: {self.quiz_brain.score}")
