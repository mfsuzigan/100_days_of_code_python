from ball import Ball
from game_screen import GameScreen
from paddle import Paddle

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


def main():
    game_screen = GameScreen(SCREEN_WIDTH, SCREEN_HEIGHT, "gray", "Pong")
    game_screen.screen.tracer(0)

    left_paddle = Paddle(size=Paddle.SIZE.NORMAL, control_up_key="w", control_down_key="s")
    left_paddle.goto(-350, 0)
    game_screen.add_paddle(left_paddle)

    right_paddle = Paddle(size=Paddle.SIZE.NORMAL)
    right_paddle.goto(350, 0)
    game_screen.add_paddle(right_paddle)

    ball = Ball()

    while True:
        game_screen.screen.update()
        ball.goto(350, 250)

    game_screen.screen.exitonclick()


if __name__ == "__main__":
    main()
