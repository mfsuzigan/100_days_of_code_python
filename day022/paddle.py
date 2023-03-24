from enum import Enum
from turtle import Turtle


class Paddle(Turtle):
    class SIZE(Enum):
        NORMAL = 5,
        SMALL = 3,
        LARGE = 8

        def __init__(self, width):
            self.width = width

    def __init__(self, control_up_key="Up", control_down_key="Down", size=SIZE.NORMAL.width):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.width = 20
        self.size = size
        self.shapesize(stretch_wid=size.width, stretch_len=1)
        self.penup()
        self.hideturtle()
        self.showturtle()
        self.screen.onkey(key=control_up_key, fun=self.move_up)
        self.screen.onkey(key=control_down_key, fun=self.move_down)
        self.screen.listen()
        self.max_y_cor = 0
        self.min_y_cor = 0

    def move_down(self):

        if self.ycor() >= self.min_y_cor:
            self.goto(self.xcor(), self.ycor() - 20)

    def move_up(self):

        if self.ycor() <= self.max_y_cor:
            self.goto(self.xcor(), self.ycor() + 20)

    def set_vertical_bounds(self, max_y_cor):
        self.max_y_cor = max_y_cor
        self.min_y_cor = -max_y_cor
