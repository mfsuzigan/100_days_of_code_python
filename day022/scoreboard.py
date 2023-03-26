from turtle import Turtle
from paddle import Paddle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()

        self.left_score = 0
        self.right_score = 0

        self.update_score()

    def update_score(self, paddle_that_missed_ball:Paddle = None):
        self.clear()

        if paddle_that_missed_ball is not None:

            if paddle_that_missed_ball.xcor() > 0:
                self.left_score += 1

            else:
                self.right_score += 1

        self.goto(-100, 200)
        self.write(self.left_score, align="center", font=("Courier", 50, "bold"))

        self.goto(100, 200)
        self.write(self.right_score, align="center", font=("Courier", 50, "bold"))