from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.fillcolor("white")
        self.shape("circle")
        self.penup()
        self.vertical_direction = 1
        self.min_y_cor = 0
        self.max_y_cor = 0

    def move(self):
        self.goto(self.xcor() + 0.2, self.ycor() + 0.2 * self.vertical_direction)

    def bounce_vertically(self):
        self.vertical_direction *= -1

    def set_vertical_bounds(self, max_ball_y_cor):
        self.max_y_cor = max_ball_y_cor
        self.min_y_cor = -max_ball_y_cor
