from turtle import Turtle

from ball import Ball
from paddle import Paddle


class PongGame(Turtle):

    def __init__(self, width, height, color, title):
        super().__init__()
        self.hideturtle()
        self.height = height
        self.width = width
        self.screen.setup(width, height)
        self.screen.bgcolor(color)
        self.screen.title(title)
        self.paddles = []
        self.ball = None

    def add_paddle(self, paddle: Paddle):
        max_paddle_y_cor = self.height / 2 - (paddle.size.width * 20 / 2) - 20
        paddle.set_vertical_bounds(max_paddle_y_cor)
        self.paddles.append(paddle)

    def add_ball(self, ball: Ball):
        max_ball_y_cor = self.height / 2
        ball.set_vertical_bounds(max_ball_y_cor)
        self.ball = ball

    def exit_on_click(self):
        self.screen.exitonclick()

    def horizontal_collision_detected(self):
        upper_collision_occurred = self.ball.distance(self.ball.xcor(), self.ball.max_y_cor) < 15
        lower_collision_occurred = self.ball.distance(self.ball.xcor(), self.ball.min_y_cor) < 15

        return upper_collision_occurred or lower_collision_occurred

    def paddle_collision_detected(self, paddle:Paddle):
        ball_is_too_far_right = paddle.xcor() > 0 and self.ball.horizontal_direction > 0 and self.ball.xcor() > (paddle.xcor() - 20)
        ball_is_too_far_left = paddle.xcor() < 0 and self.ball.horizontal_direction < 0 and self.ball.xcor() < (paddle.xcor() + 20)

        return (ball_is_too_far_right or ball_is_too_far_left) and self.ball.distance(paddle) < 59

    def get_info(self, paddle: Paddle = None):
        info = f"ball({self.ball.xcor(): .3f}, {self.ball.ycor(): .3f})"

        if paddle is not None:
            info += f"; paddle({paddle.xcor(): .3f}, {paddle.ycor(): .3f}); distance={self.ball.distance(paddle): .3f}"

        return info