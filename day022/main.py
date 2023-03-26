import time

from ball import Ball
from pong_game import PongGame
from paddle import Paddle
from scoreboard import Scoreboard

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

def main():
    game = PongGame(SCREEN_WIDTH, SCREEN_HEIGHT, "black", "Pong")
    game.screen.tracer(0)
    game.screen.onkeypress(fun=lambda: game.screen.bye(), key="Escape")

    right_paddle = Paddle(size=Paddle.Size.NORMAL)
    right_paddle.goto(350, 0)
    game.add_paddle(right_paddle)

    left_paddle = Paddle(size=Paddle.Size.NORMAL, control_up_key="w", control_down_key="s")
    left_paddle.goto(-350, 0)
    game.add_paddle(left_paddle)

    ball = Ball(Ball.Speed.NORMAL)
    game.add_ball(ball)

    scoreboard = Scoreboard()

    while True:
        ball.move()
        game.screen.update()

        if game.horizontal_collision_detected():
            print(game.get_info())
            ball.bounce_vertically()

        for paddle in game.paddles:

            if game.paddle_collision_detected(paddle):
                print(game.get_info(paddle))
                ball.bounce_horizontally()
                ball.increase_speed(percentage=3)

            if game.ball_is_off_edges(paddle):
                opposite_paddle = game.paddles[1] if game.paddles[0] == paddle else game.paddles[0]
                game.reset_towards_paddle(opposite_paddle)

                scoreboard.update_score(paddle_that_missed_ball=paddle)

                game.screen.update()
                time.sleep(2)

def get_saved_bugged_game1(ball, right_paddle):
    ball.goto(320.399, -40.40)
    right_paddle.goto(350, -80)
    ball.bounce_vertically()


def get_saved_bugged_game2(ball, right_paddle):
    ball.goto(341.598, -209.199)
    right_paddle.goto(350, -160)


if __name__ == "__main__":
    main()
