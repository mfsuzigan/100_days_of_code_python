from turtle import Turtle

TEXT_ALIGNMENT = "center"
FONT = ('Courier', 20, "bold")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.hideturtle()
        self.penup()
        self.goto(0, 260)
        self.pencolor("white")
        self.display()

    def display(self):
        self.write(arg=f"Score: {self.score} High score: {self.high_score}", align=TEXT_ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score

        self.score = 0
        self.clear()
        self.display()

    def increment(self):
        self.score += 1
        self.clear()
        self.display()
