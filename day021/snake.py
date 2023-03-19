from enum import Enum
from turtle import Screen

from snake_block import SnakeBlock


class Directions(Enum):
    UP = ("Up", 90)
    DOWN = ("Down", 270)
    RIGHT = ("Right", 0)
    LEFT = ("Left", 180)

    def __init__(self, description, heading):
        self.description = description
        self.heading = heading


class Snake:

    def __init__(self, screen: Screen):
        self.screen = screen
        self.head = None

        self.add_block(SnakeBlock())
        self.add_block(SnakeBlock())
        self.add_block(SnakeBlock())

        self.setup_controls()

    def add_block(self, block: SnakeBlock):

        if self.head is None:
            self.head = block
            self.head.setx(0)
            self.head.sety(0)

        else:
            self.head.add_block_to_tail(block)

    def setup_controls(self):

        for direction in Directions:
            print(f"{direction.description} {direction.heading}")
            self.screen.onkey(key=direction.description, fun=lambda d=direction.heading: self.head.setheading(d))

        self.screen.listen()

    def move(self):
        self.head.move()
        self.screen.update()

    def print_heading(self):
        print(f"Heading is {self.head.heading()}")
