import time
from turtle import Screen

from scoreboard import Scoreboard
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
    scoreboard = Scoreboard()
    game_over = False

    while not game_over:
        snake.move()
        screen.update()
        time.sleep(0.1)

        if snake.head.distance(food) < 15:
            food.update_position()
            snake.add_block(SnakeBlock())
            scoreboard.increment()

        vertical_limit = SCREEN_WIDTH / 2 - 25
        snake_hit_vertical_wall = snake.head.xcor() > vertical_limit or snake.head.xcor() < -vertical_limit

        horizontal_limit = SCREEN_HEIGHT / 2 - 25
        snake_hit_horizontal_wall = snake.head.ycor() > horizontal_limit or snake.head.ycor() < -horizontal_limit

        if snake_hit_horizontal_wall or snake_hit_vertical_wall:
            game_over = True
            scoreboard.game_over()

    screen.exitonclick()


if __name__ == "__main__":
    main()
