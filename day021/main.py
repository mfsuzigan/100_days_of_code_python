import time
from turtle import Screen

from snake import Snake
from snake_block import SnakeBlock
from snake_food import SnakeFood

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 600


def main():
    screen = Screen()
    screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
    screen.bgcolor("black")
    screen.tracer(0)

    snake = Snake(screen)
    food = SnakeFood(SCREEN_WIDTH, SCREEN_HEIGHT)

    while True:
        snake.move()
        screen.update()
        time.sleep(0.1)

        if snake.head.distance(food) < 15:
            food.update_position()
            snake.add_block(SnakeBlock())

    screen.exitonclick()


if __name__ == "__main__":
    main()
