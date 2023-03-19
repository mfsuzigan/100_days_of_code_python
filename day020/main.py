import time
from turtle import Screen

from snake import Snake

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 600


def main():
    screen = Screen()
    screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
    screen.bgcolor("black")
    screen.tracer(0)

    snake = Snake(screen)

    while True:
        snake.move()
        screen.update()
        time.sleep(0.1)

    screen.exitonclick()


if __name__ == "__main__":
    main()
