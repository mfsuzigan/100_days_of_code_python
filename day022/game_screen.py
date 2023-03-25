from turtle import Turtle

from ball import Ball
from paddle import Paddle


class GameScreen(Turtle):

    def __init__(self, width, height, color, title):
        super().__init__()
        self.hideturtle()
        self.height = height
        self.width = width
        self.screen.setup(width, height)
        self.screen.bgcolor(color)
        self.screen.title(title)

    def add_paddle(self, paddle: Paddle):
        max_paddle_y_cor = self.height / 2 - (paddle.size.width * 20 / 2) - 20
        paddle.set_vertical_bounds(max_paddle_y_cor)

    def add_ball(self, ball: Ball):
        max_ball_y_cor = self.height / 2
        ball.set_vertical_bounds(max_ball_y_cor)

    def exit_on_click(self):
        self.screen.exitonclick()
