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
            print("Head added")

        else:
            block.id += 1
            self.head.add_block_to_tail(block)

    def setup_controls(self):

        for direction in Directions:
            self.screen.onkey(key=direction.description, fun=lambda d=direction.heading: self.change_heading(d))

        self.screen.listen()

    def change_heading(self, new_heading):

        if (self.head.heading() - new_heading) not in [-180, 180]:
            self.head.setheading(new_heading)

    def move(self):
        self.head.move()
        self.screen.update()

    def has_collided_with_tail(self, block: SnakeBlock = None):

        if block is None:
            return False

        elif self.head.distance(block) > 10:
            return self.has_collided_with_tail(block.tail)

        else:
            print(f"Tail collision: block {block.id}, head distance {self.head.distance(block)}")
            return True

    def reset(self):
        block_counter = 0
        block = self.head

        while block is not None:
            next_block = block.tail

            if block_counter >= 3:
                block.head.tail = None
                block.head = None
                block.hideturtle()

            block = next_block
            block_counter += 1

        self.head.goto(0, 0)
        self.change_heading(0)
