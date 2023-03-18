from direction import Direction
from snake_block import SnakeBlock


class Snake:

    def __init__(self):
        self.head = SnakeBlock(head=None)
        body = SnakeBlock(head=self.head)
        tail = SnakeBlock(head=body)

        # self.blocks = [self.head, body, tail]

    def add_block(self, block: SnakeBlock):
        pass

    def move(self, direction: Direction):
        self.head.move_to_direction(direction)
