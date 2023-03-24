from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, x_pos):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.width = 20
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.hideturtle()
        self.goto(x_pos, 0)
        self.showturtle()
