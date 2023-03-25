from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.fillcolor("white")
        self.shape("circle")
        self.penup()

    def move(self):
        self.goto(self.xcor() + 0.2, self.ycor() + 0.2)
