from ball import Ball
from game_screen import PongGame
from paddle import Paddle

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


def main():
    game = PongGame(SCREEN_WIDTH, SCREEN_HEIGHT, "black", "Pong")
    game.screen.tracer(0)

    right_paddle = Paddle(size=Paddle.Size.NORMAL)
    right_paddle.goto(350, 0)
    game.add_paddle(right_paddle)

    left_paddle = Paddle(size=Paddle.Size.NORMAL, control_up_key="w", control_down_key="s")
    left_paddle.goto(-350, 0)
    game.add_paddle(left_paddle)

    ball = Ball(Ball.Speed.NORMAL)
    game.add_ball(ball)

    while True:
        ball.move()
        game.screen.update()

        if game.horizontal_collision_detected(ball):
            print(game.get_info(ball))
            ball.bounce_vertically()

        for paddle in game.paddles:

            if game.paddle_collision_detected(ball, paddle):
                print(game.get_info(ball, paddle))
                ball.bounce_horizontally()

    game.exit_on_click()


def get_saved_bugged_game1(ball, right_paddle):
    ball.goto(320.399, -40.40)
    right_paddle.goto(350, -80)
    ball.bounce_vertically()


def get_saved_bugged_game2(ball, right_paddle):
    ball.goto(341.598, -209.199)
    right_paddle.goto(350, -160)


if __name__ == "__main__":
    main()
