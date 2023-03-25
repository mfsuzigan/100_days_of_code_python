from ball import Ball
from game_screen import GameScreen
from paddle import Paddle

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


def main():
    game_screen = GameScreen(SCREEN_WIDTH, SCREEN_HEIGHT, "black", "Pong")
    game_screen.screen.tracer(0)

    left_paddle = Paddle(size=Paddle.SIZE.NORMAL, control_up_key="w", control_down_key="s")
    left_paddle.goto(-350, 0)
    game_screen.add_paddle(left_paddle)

    right_paddle = Paddle(size=Paddle.SIZE.NORMAL)
    right_paddle.goto(350, 0)
    game_screen.add_paddle(right_paddle)

    ball = Ball()
    game_screen.add_ball(ball)

    while True:
        ball.move()
        game_screen.screen.update()

        if ball_has_horizontally_collided(ball):
            ball.bounce_vertically()

    game_screen.screen.exitonclick()


def ball_has_horizontally_collided(ball: Ball):
    upper_collision_happened = ball.distance(ball.xcor(), ball.max_y_cor) < 15
    lower_collision_happened = ball.distance(ball.xcor(), ball.min_y_cor) < 15

    return upper_collision_happened or lower_collision_happened


if __name__ == "__main__":
    main()
