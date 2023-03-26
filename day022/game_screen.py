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

    def add_paddle(self, paddle: Paddle):
        max_paddle_y_cor = self.height / 2 - (paddle.size.width * 20 / 2) - 20
        paddle.set_vertical_bounds(max_paddle_y_cor)
        self.paddles.append(paddle)

    def add_ball(self, ball: Ball):
        max_ball_y_cor = self.height / 2
        ball.set_vertical_bounds(max_ball_y_cor)

    def exit_on_click(self):
        self.screen.exitonclick()

    @staticmethod
    def horizontal_collision_detected(ball:Ball):
        upper_collision_occurred = ball.distance(ball.xcor(), ball.max_y_cor) < 15
        lower_collision_occurred = ball.distance(ball.xcor(), ball.min_y_cor) < 15

        return upper_collision_occurred or lower_collision_occurred

    @staticmethod
    def paddle_collision_detected(ball:Ball, paddle:Paddle):
        ball_is_too_far_right = paddle.xcor() > 0 and ball.horizontal_direction > 0 and ball.xcor() > (paddle.xcor() - 20)
        ball_is_too_far_left = paddle.xcor() < 0 and ball.horizontal_direction < 0 and ball.xcor() < (paddle.xcor() + 20)

        return (ball_is_too_far_right or ball_is_too_far_left) and ball.distance(paddle) < 59

    @staticmethod
    def get_info(ball: Ball, paddle: Paddle = None):
        info = f"ball({ball.xcor(): .3f}, {ball.ycor(): .3f})"

        if paddle is not None:
            info += f"; paddle({paddle.xcor(): .3f}, {paddle.ycor(): .3f}); distance={ball.distance(paddle): .3f}"

        return info