from turtle import Screen

from paddle import Paddle

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


def main():
    screen = Screen()
    screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
    screen.bgcolor("black")
    screen.title("Pong")

    right_paddle = Paddle(x_pos=350)
    left_paddle = Paddle(x_pos=-350)

    screen.exitonclick()


if __name__ == "__main__":
    main()
