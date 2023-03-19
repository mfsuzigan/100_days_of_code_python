import time
from turtle import Screen

from snake import Snake


def main():
    screen = Screen()
    screen.screensize(600, 600)
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
