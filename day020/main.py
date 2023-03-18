from turtle import Screen

from models.direction import Direction
from models.snake import Snake


def main():
    screen = Screen()
    screen.screensize(600, 600)
    screen.bgcolor("black")

    snake = Snake()

    while True:
        snake.move(Direction.FORWARD)

    # screen.exitonclick()


if __name__ == "__main__":
    main()
