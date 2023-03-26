from enum import Enum
from turtle import Turtle


class Ball(Turtle):
    class Speed(Enum):
        NORMAL = 0.2
        LOW = 0.05
        HIGH = 0.3

    def __init__(self, speed):
        super().__init__()
        self.fillcolor("white")
        self.shape("circle")
        self.penup()
        self.vertical_direction = 1
        self.horizontal_direction = 1
        self.min_y_cor = 0
        self.max_y_cor = 0
        self.speed = speed

    def move(self):
        horizontal_increment = self.speed.value * self.horizontal_direction
        vertical_increment = self.speed.value * self.vertical_direction
        self.goto(self.xcor() + horizontal_increment, self.ycor() + vertical_increment)

    def bounce_vertically(self):
        self.vertical_direction *= -1

    def bounce_horizontally(self):
        self.horizontal_direction *= -1

    def set_vertical_bounds(self, max_ball_y_cor):
        self.max_y_cor = max_ball_y_cor
        self.min_y_cor = -max_ball_y_cor
